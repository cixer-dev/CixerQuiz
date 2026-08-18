#!/usr/bin/env bash
set -euo pipefail

APP_DOMAIN="CixerQuiz"

BUILDER_TRANSLATIONS_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
TRANSLATIONS_DIR="$(cd -- "$(dirname -- "$BUILDER_TRANSLATIONS_DIR")" && pwd)"
PROJECT_DIR="$(cd -- "$(dirname -- "$TRANSLATIONS_DIR")" && pwd)"
POT_PATH="${TRANSLATIONS_DIR%/}/${APP_DOMAIN}.pot"

echo "The BUILDER_TRANSLATIONS_DIR is: $BUILDER_TRANSLATIONS_DIR"
echo "The PROJECT_DIR is $PROJECT_DIR"
echo "The TRANSLATIONS_DIR is $TRANSLATIONS_DIR"
echo "The POT_PATH is: $POT_PATH"

cd "$PROJECT_DIR"

if [[ -f "$POT_PATH" ]]; then
  echo "Existing pot found, deleting: $POT_PATH"
  rm -f -- "$POT_PATH"
fi

# Generate POT from Python sources
mapfile -d '' -t py_files < <(find src -type f -name '*.py' -print0)

if ((${#py_files[@]} == 0)); then
  echo "No Python files found under src; nothing to generate."
else
  xgettext \
    --language=Python \
    --keyword=_ \
    --output="$POT_PATH" \
    "${py_files[@]}"
fi

echo "Generated: $POT_PATH"

echo "Press q to exit."
while IFS= read -r -n 1 key; do
  [[ "$key" == "q" ]] && break
done
echo

