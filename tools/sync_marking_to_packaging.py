#!/usr/bin/env python3
"""Copy chip-marking identification tables from esp-chip-errata into esp-packaging.

Source (this repo)::

    docs/{en,zh_CN}/01-chip-identification/<target>/chip-marking-identification.rst

Destination (esp-packaging)::

    docs/{en,zh_CN}/01-marking/chip/identification/<target>/chip-marking-identification.txt

When a target's copied table changes, the matching EN/CN ``revision_date``
entries in esp-packaging ``.lbcf.yml`` are set to today (or ``--revision-date``).

CI usage (after cloning esp-packaging)::

    python3 tools/sync_marking_to_packaging.py \\
        --packaging-repo /path/to/esp-packaging --push-mr
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

LANGUAGES = ("en", "zh_CN")
SOURCE_REL = Path("docs") / "{lang}" / "01-chip-identification"
DEST_REL = Path("docs") / "{lang}" / "01-marking" / "chip" / "identification"
SOURCE_TABLE = "chip-marking-identification.rst"
DEST_TABLE = "chip-marking-identification.txt"

# Packaging builds ESP8266; errata has no marking table for it. A comment-only
# stub keeps ``.. include:: chip/identification/{IDF_TARGET_PATH_NAME}/...`` valid
# when Sphinx expands includes before evaluating ``only`` directives.
STUB_TARGETS = ("esp8266",)
STUB_CONTENT = (
    ".. This packaging target has no chip-marking table in esp-chip-errata.\n"
)

# Target slug -> .lbcf.yml chip_series (exact match).
TARGET_TO_CHIP_SERIES = {
    "esp32": "ESP32",
    "esp32s2": "ESP32-S2",
    "esp32s3": "ESP32-S3",
    "esp32s31": "ESP32-S31",
    "esp32c2": "ESP32-C2",
    "esp32c3": "ESP32-C3",
    "esp32c5": "ESP32-C5",
    "esp32c6": "ESP32-C6",
    "esp32c61": "ESP32-C61",
    "esp32h2": "ESP32-H2",
    "esp32p4": "ESP32-P4",
    "esp8266": "ESP8266",
}

DEFAULT_PACKAGING_PROJECT = "espressif/esp-packaging"
BOT_BRANCH = "bot/sync-chip-marking"
DOC_START_RE = re.compile(r"^    - document_name:")
CHIP_SERIES_RE = re.compile(r"^      chip_series:\s*(\S+)\s*$")
REVISION_DATE_RE = re.compile(r"^(      revision_date: )(\S+)(.*)$")


def discover_targets(errata_root: Path) -> list[str]:
    targets: set[str] = set()
    for lang in LANGUAGES:
        root = errata_root / str(SOURCE_REL).format(lang=lang)
        if not root.is_dir():
            continue
        for path in root.glob(f"*/{SOURCE_TABLE}"):
            targets.add(path.parent.name)
    return sorted(targets)


def source_path(errata_root: Path, lang: str, target: str) -> Path:
    return errata_root / str(SOURCE_REL).format(lang=lang) / target / SOURCE_TABLE


def dest_path(packaging_root: Path, lang: str, target: str) -> Path:
    return packaging_root / str(DEST_REL).format(lang=lang) / target / DEST_TABLE


INCLUDE_NEEDLE = (
    "chip/identification/{IDF_TARGET_PATH_NAME}/chip-marking-identification.txt"
)


def verify_includes(packaging_root: Path) -> None:
    for lang in LANGUAGES:
        marking = packaging_root / "docs" / lang / "01-marking" / "chip" / "marking.txt"
        if INCLUDE_NEEDLE not in marking.read_text(encoding="utf-8"):
            raise SystemExit(f"{marking} is missing: .. include:: {INCLUDE_NEEDLE}")


def copy_tables(errata_root: Path, packaging_root: Path) -> list[str]:
    """Copy tables. Return target slugs whose destination content changed."""
    changed: set[str] = set()
    targets = discover_targets(errata_root)
    if not targets:
        raise SystemExit("No chip-marking-identification.rst files found in errata.")

    for target in targets:
        for lang in LANGUAGES:
            src = source_path(errata_root, lang, target)
            if not src.is_file():
                print(f"warning: missing {src.relative_to(errata_root)}", file=sys.stderr)
                continue
            dst = dest_path(packaging_root, lang, target)
            new = src.read_text(encoding="utf-8")
            old = dst.read_text(encoding="utf-8") if dst.is_file() else None
            if old == new:
                continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(new, encoding="utf-8")
            changed.add(target)
            print(f"updated {dst.relative_to(packaging_root)}")

    for target in STUB_TARGETS:
        for lang in LANGUAGES:
            if source_path(errata_root, lang, target).is_file():
                continue
            dst = dest_path(packaging_root, lang, target)
            dst.parent.mkdir(parents=True, exist_ok=True)
            if dst.is_file():
                continue
            dst.write_text(STUB_CONTENT, encoding="utf-8")
            print(f"wrote stub {dst.relative_to(packaging_root)}")
    return sorted(changed)


def update_lbcf(lbcf_path: Path, targets: list[str], revision_date: str) -> bool:
    """Set revision_date on document entries whose chip_series matches *targets*.

    Line-based edit so comments and quoting in .lbcf.yml are preserved.
    """
    series = {TARGET_TO_CHIP_SERIES[t] for t in targets if t in TARGET_TO_CHIP_SERIES}
    unknown = [t for t in targets if t not in TARGET_TO_CHIP_SERIES]
    for slug in unknown:
        print(f"warning: no chip_series mapping for {slug}; skip lbcf", file=sys.stderr)
    if not series:
        return False

    original = lbcf_path.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)
    current_series = None
    out: list[str] = []
    updated = 0
    for line in lines:
        if DOC_START_RE.match(line):
            current_series = None
        match_series = CHIP_SERIES_RE.match(line.rstrip("\n"))
        if match_series:
            current_series = match_series.group(1)
        match_date = REVISION_DATE_RE.match(line.rstrip("\n"))
        if match_date and current_series in series:
            prefix, old_date, suffix = match_date.groups()
            if old_date != revision_date:
                newline = "\n" if line.endswith("\n") else ""
                line = f"{prefix}{revision_date}{suffix}{newline}"
                updated += 1
        out.append(line)

    new = "".join(out)
    if new == original:
        return False
    lbcf_path.write_text(new, encoding="utf-8")
    print(f"updated {updated} revision_date entries in {lbcf_path.name} -> {revision_date}")
    return True


def git(packaging_root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    result = subprocess.run(
        ["git", *args],
        cwd=packaging_root,
        check=False,
        text=True,
        capture_output=True,
    )
    if check and result.returncode != 0:
        raise SystemExit(
            f"git {' '.join(args)} failed ({result.returncode}):\n{result.stderr or result.stdout}"
        )
    return result


def gitlab_api(
    base_url: str,
    token: str,
    method: str,
    path: str,
    data: dict | None = None,
) -> object:
    url = base_url.rstrip("/") + "/api/v4" + path
    body = None
    headers = {"PRIVATE-TOKEN": token}
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"GitLab API {method} {path} failed: {exc.code} {detail}") from exc


def lookup_assignee_id(base_url: str, token: str, email: str, username: str) -> int | None:
    queries: list[str] = []
    if email:
        queries.append("/users?" + urllib.parse.urlencode({"search": email}))
    if username:
        queries.append("/users?" + urllib.parse.urlencode({"username": username}))
    for query in queries:
        users = gitlab_api(base_url, token, "GET", query)
        if not isinstance(users, list) or not users:
            continue
        for user in users:
            if (email and user.get("email") == email) or (
                username and user.get("username") == username
            ):
                return int(user["id"])
        return int(users[0]["id"])
    return None


def push_mr(
    packaging_root: Path,
    changed_targets: list[str],
    errata_sha: str,
    assignee_email: str,
    assignee_username: str,
) -> None:
    token = os.environ.get("PACKAGING_SYNC_TOKEN") or os.environ.get("GITLAB_TOKEN")
    if not token:
        raise SystemExit("PACKAGING_SYNC_TOKEN (or GITLAB_TOKEN) is not set.")

    gitlab_url = os.environ.get("GITLAB_URL") or os.environ.get("CI_SERVER_URL")
    if not gitlab_url:
        raise SystemExit("GITLAB_URL or CI_SERVER_URL is not set.")

    project_path = os.environ.get("PACKAGING_PROJECT_PATH", DEFAULT_PACKAGING_PROJECT)
    encoded = urllib.parse.quote(project_path, safe="")

    git(packaging_root, "checkout", "-B", BOT_BRANCH)
    git(packaging_root, "add", "-A")
    status = git(packaging_root, "status", "--porcelain")
    if not status.stdout.strip():
        print("No git changes to commit.")
        return

    target_list = ", ".join(changed_targets) if changed_targets else "(none)"
    message = (
        "docs: sync chip marking tables from esp-chip-errata\n\n"
        f"Updated targets: {target_list}\n"
        f"Source commit: {errata_sha}\n"
    )
    git(
        packaging_root,
        "-c",
        "user.name=esp-chip-errata CI",
        "-c",
        "user.email=esp-chip-errata-ci@espressif.com",
        "commit",
        "-m",
        message,
    )
    push = git(
        packaging_root,
        "push",
        "--force",
        "-u",
        "origin",
        BOT_BRANCH,
        check=False,
    )
    if push.returncode != 0:
        raise SystemExit(f"git push failed:\n{push.stderr}")

    opened = gitlab_api(
        gitlab_url,
        token,
        "GET",
        f"/projects/{encoded}/merge_requests?state=opened&source_branch={BOT_BRANCH}",
    )
    if isinstance(opened, list) and opened:
        print(f"Updated existing MR: {opened[0].get('web_url')}")
        return

    assignee_id = None
    if assignee_email or assignee_username:
        assignee_id = lookup_assignee_id(gitlab_url, token, assignee_email, assignee_username)
    description = (
        "Automated sync of chip revision identification tables from "
        f"`esp-chip-errata@{errata_sha}`.\n\n"
        f"**Updated targets:** {target_list}\n\n"
        "Changes:\n"
        "- Copied `chip-marking-identification` tables into "
        "`docs/{en,zh_CN}/01-marking/chip/identification/<target>/`\n"
        "- Set `.lbcf.yml` `revision_date` for the affected chip series\n"
    )
    payload = {
        "source_branch": BOT_BRANCH,
        "target_branch": os.environ.get("PACKAGING_TARGET_BRANCH", "master"),
        "title": "docs: sync chip marking tables from esp-chip-errata",
        "description": description,
        "remove_source_branch": True,
    }
    if assignee_id is not None:
        payload["assignee_id"] = assignee_id
    elif assignee_email or assignee_username:
        print(
            "warning: could not resolve GitLab assignee from "
            "PACKAGING_MR_ASSIGNEE_EMAIL / PACKAGING_MR_ASSIGNEE_USERNAME; "
            "MR will be unassigned",
            file=sys.stderr,
        )
    else:
        print(
            "No assignee configured; set PACKAGING_MR_ASSIGNEE_EMAIL and/or "
            "PACKAGING_MR_ASSIGNEE_USERNAME as CI variables if needed.",
            file=sys.stderr,
        )

    mr = gitlab_api(gitlab_url, token, "POST", f"/projects/{encoded}/merge_requests", payload)
    print(f"Created MR: {mr.get('web_url') if isinstance(mr, dict) else mr}")


def parse_args() -> argparse.Namespace:
    default_errata = Path(__file__).resolve().parents[1]
    default_packaging = default_errata.parent / "esp-packaging"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--errata-repo", type=Path, default=default_errata)
    parser.add_argument("--packaging-repo", type=Path, default=default_packaging)
    parser.add_argument(
        "--revision-date",
        default=dt.date.today().isoformat(),
        help="YYYY-MM-DD written to .lbcf.yml (default: today)",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--push-mr",
        action="store_true",
        help="Commit, push bot/sync-chip-marking, and open/update an MR",
    )
    parser.add_argument(
        "--assignee-email",
        default=os.environ.get("PACKAGING_MR_ASSIGNEE_EMAIL", ""),
        help="GitLab assignee email (or set PACKAGING_MR_ASSIGNEE_EMAIL)",
    )
    parser.add_argument(
        "--assignee-username",
        default=os.environ.get("PACKAGING_MR_ASSIGNEE_USERNAME", ""),
        help="GitLab assignee username (or set PACKAGING_MR_ASSIGNEE_USERNAME)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errata = args.errata_repo.resolve()
    packaging = args.packaging_repo.resolve()
    if not (errata / "docs").is_dir():
        raise SystemExit(f"Not an errata repo: {errata}")
    if not (packaging / ".lbcf.yml").is_file():
        raise SystemExit(f"Not an esp-packaging repo (missing .lbcf.yml): {packaging}")

    if args.dry_run:
        targets = discover_targets(errata)
        print("would sync targets:", ", ".join(targets))
        return 0

    changed = copy_tables(errata, packaging)
    verify_includes(packaging)
    lbcf_changed = False
    if changed:
        lbcf_changed = update_lbcf(packaging / ".lbcf.yml", changed, args.revision_date)
    else:
        print("Table files already up to date.")

    if args.push_mr:
        sha = os.environ.get("CI_COMMIT_SHA") or git(errata, "rev-parse", "HEAD").stdout.strip()
        # Commit even when only lbcf or stubs changed.
        status = git(packaging, "status", "--porcelain")
        if not status.stdout.strip():
            print("No packaging changes; skipping MR.")
            return 0
        push_mr(
            packaging,
            changed,
            sha,
            args.assignee_email,
            args.assignee_username,
        )
    elif not changed and not lbcf_changed:
        return 0

    print("changed targets:", ", ".join(changed) if changed else "(none)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
