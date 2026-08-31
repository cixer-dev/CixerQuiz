#!/usr/bin/env bash
set -euo pipefail

LANGUAGES_SUFFIX_LIST=(es)
APP_DOMAIN="CixerQuiz"

BUILDER_TRANSLATIONS_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
TRANSLATIONS_DIR="$(cd -- "$(dirname -- "$BUILDER_TRANSLATIONS_DIR")" && pwd)"

for lang in "${LANGUAGES_SUFFIX_LIST[@]}"; do
  po_dir="${TRANSLATIONS_DIR}/locale/${lang}/LC_MESSAGES"
  po_filepath="${po_dir}/${APP_DOMAIN}.po"
  mo_filepath="${po_dir}/${APP_DOMAIN}.mo"

  mkdir -p "$po_dir"

  if [[ ! -f "$po_filepath" ]]; then
    echo "PO file not found for $lang: $po_filepath"
    exit 1
  fi

  msgfmt -o "$mo_filepath" "$po_filepath"
  echo "The MO file for $lang was compiled correctly at: $mo_filepath"
done

echo "Press q to exit."
while IFS= read -r -n 1 key; do
  [[ "$key" == "q" ]] && break
done
echo

