#!/bin/sh

# target directory and the URL of Scripts repo
TARGET_DIR="scripts"
SCRIPTS_REPO="https://clonescriptrepo:FrGQpqmSzy6uJjwcbHC9@gitlab.espressif.cn:6688/idf/scripts.git"

# check whether the Scripts repo exists or not. If not exist, clone the Scripts repo.
if [ -d "$TARGET_DIR" ]; then
  echo "Directory '$TARGET_DIR' exists. Entering and updating repository..."
  cd "$TARGET_DIR"
  git pull
  cd ..
else
  echo "Directory '$TARGET_DIR' does not exist. Cloning repository..."
  git clone -b new_check_format "$SCRIPTS_REPO"
fi

LANG=""

# Inspect each file passed to the script
for file in "$@"; do
  if echo "$file" | grep -q "en/"; then
    LANG="en"
    break
  elif echo "$file" | grep -q "zh_CN/"; then
    LANG="zh_CN"
    break
  fi
done

echo "Start checking the rst format for file(s) '$@'."

python3 scripts/check_docs_format.py "$LANG" "$@"
