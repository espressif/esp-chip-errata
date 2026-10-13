#!/usr/bin/env python3
"""Comment on the errata merge request when packaging sync fails.

The GitLab username is PACKAGING_MR_ASSIGNEE_USERNAME. The note uses
GITLAB_MR_NOTE_TOKEN. CI_JOB_TOKEN can read merge requests but cannot
create notes. Exits 0 when there is nothing to comment on, so after_script
does not hide the original job failure.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


def api(method: str, path: str, token: str, data: dict | None = None) -> object:
    base = os.environ.get("CI_API_V4_URL", "").rstrip("/")
    if not base:
        server = os.environ.get("CI_SERVER_URL", "").rstrip("/")
        base = f"{server}/api/v4"
    body = None
    headers = {"PRIVATE-TOKEN": token}
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(
        base + path, data=body, headers=headers, method=method
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read().decode("utf-8")
        return json.loads(raw) if raw else None


def main() -> int:
    username = os.environ.get("PACKAGING_MR_ASSIGNEE_USERNAME", "").strip().lstrip("@")
    if not username:
        print("PACKAGING_MR_ASSIGNEE_USERNAME is unset; skip failure note.")
        return 0

    token = os.environ.get("GITLAB_MR_NOTE_TOKEN", "")
    project_id = os.environ.get("CI_PROJECT_ID", "")
    sha = os.environ.get("CI_COMMIT_SHA", "")
    job_url = os.environ.get("CI_JOB_URL", "")
    if not token:
        print("GITLAB_MR_NOTE_TOKEN is unset; skip failure note.")
        return 0
    if not project_id or not sha:
        print("CI job context is incomplete; skip failure note.")
        return 0

    try:
        found = api(
            "GET",
            f"/projects/{project_id}/repository/commits/{urllib.parse.quote(sha, safe='')}/merge_requests",
            token,
        )
    except urllib.error.HTTPError as exc:
        print(f"could not look up merge request: HTTP {exc.code}", file=sys.stderr)
        return 0
    except Exception as exc:
        print(f"could not look up merge request: {type(exc).__name__}", file=sys.stderr)
        return 0

    if not isinstance(found, list) or not found:
        print("No merge request for this commit; skip failure note.")
        return 0

    merge_request = next(
        (item for item in found if item.get("state") == "merged"),
        found[0],
    )
    iid = merge_request.get("iid")
    if not iid:
        print("Merge request has no iid; skip failure note.")
        return 0

    body = (
        f"@{username} `sync_marking_to_packaging` failed.\n\n"
        f"Job: {job_url}\n"
    )
    try:
        api(
            "POST",
            f"/projects/{project_id}/merge_requests/{iid}/notes",
            token,
            {"body": body},
        )
    except urllib.error.HTTPError as exc:
        print(f"could not post merge request note: HTTP {exc.code}", file=sys.stderr)
        return 0
    except Exception as exc:
        print(f"could not post merge request note: {type(exc).__name__}", file=sys.stderr)
        return 0

    print(f"Posted sync failure note on !{iid}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
