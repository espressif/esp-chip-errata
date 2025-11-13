#!/bin/bash

# Target directory and the URL of Scripts repo
TARGET_DIR="scripts"

# Clone the Scripts repo.
rm -rf "$TARGET_DIR"
git clone -b new_check_format "$SCRIPTS_REPO" "$TARGET_DIR"

# Initialize variables
EN_FILES=()
ZH_CN_FILES=()

# echo "Changed files: $@"

# Inspect each file passed to the script
for file in "$@"; do
  case "$file" in
    docs/en/*) EN_FILES+=("$file") ;;
    docs/zh_CN/*) ZH_CN_FILES+=("$file") ;;
  esac
done

# Process English files if any
if [ ${#EN_FILES[@]} -gt 0 ]; then
  echo "Start checking EMoS violations for English rst file(s): ${EN_FILES[*]}"
  for file in "${EN_FILES[@]}"; do
    result=$(python3 scripts/check_docs_format.py "en" "$file" 2>&1)
    # Print only if there's an error or warning
    if echo "$result" | grep -Eiq "Syntax check found"; then
      echo "$result"
      ERROR_FOUND=true
    fi
  done
fi

# Process Chinese files if any
if [ ${#ZH_CN_FILES[@]} -gt 0 ]; then
  echo "Start checking EMoS violations for Chinese rst file(s): ${ZH_CN_FILES[*]}"
  for file in "${ZH_CN_FILES[@]}"; do
    result=$(python3 scripts/check_docs_format.py "zh_CN" "$file" 2>&1)
    if echo "$result" | grep -Eiq "Syntax check found"; then
      echo "$result"
      ERROR_FOUND=true
    fi
  done
fi

# Handle case where no files matched
if [ ${#EN_FILES[@]} -eq 0 ] && [ ${#ZH_CN_FILES[@]} -eq 0 ]; then
  echo "No matching files found in 'en/' or 'zh_CN/' folders."
fi

# Fail if any error detected
if [ "$ERROR_FOUND" = true ]; then
  echo "❌ EMoS violations detected in one or more files."
  exit 1
else
  echo "✅ All checked files passed EMoS check."
fi
