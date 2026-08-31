#!/usr/bin/env bash
set -euo pipefail

LANGUAGES_SUFFIX_LIST=(es)
APP_DOMAIN="CixerQuiz"

BUILDER_TRANSLATIONS_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
TRANSLATIONS_DIR="$(cd -- "$(dirname -- "$BUILDER_TRANSLATIONS_DIR")" && pwd)"
POT_PATH="${TRANSLATIONS_DIR%/}/${APP_DOMAIN}.pot"

fix_po_charset() {
  local po_filepath="$1"
  perl -0777 -i -pe 's/(Content-Type:\s*text\/plain;\s*charset=)[^\\n"]+/$1UTF-8/g' "$po_filepath"
}

for lang in "${LANGUAGES_SUFFIX_LIST[@]}"; do
  po_dir="${TRANSLATIONS_DIR}/locale/${lang}/LC_MESSAGES"
  po_filepath="${po_dir}/${APP_DOMAIN}.po"

  mkdir -p "$po_dir"

  if [[ ! -f "$po_filepath" ]]; then
    msginit --input="$POT_PATH" --locale="$lang" --output-file="$po_filepath"
    fix_po_charset "$po_filepath"
    echo "Created PO for $lang: $po_filepath"
  fi

  msgmerge -U "$po_filepath" "$POT_PATH"
  fix_po_charset "$po_filepath"
  echo "Merged PO for $lang successfully at: $po_filepath"
done

echo "Press q to exit."
while IFS= read -r -n 1 key; do
  [[ "$key" == "q" ]] && break
done
echo


