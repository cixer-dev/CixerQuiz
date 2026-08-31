#!/usr/bin/env bash

set -Eeuo pipefail

exit_code=0

trap '
    exit_code=$?
    printf "Error: command failed with exit code %s: %s\n" \
        "$exit_code" "$BASH_COMMAND" >&2
    exit "$exit_code"
' ERR

bash github_scripts/poetry_initializer/linux_poetry_initializer.sh

echo "Installing poetry-plugin-export..."

pip install poetry-plugin-export

echo "Exporting requirements.txt..."

poetry export \
    --format requirements.txt \
    --output requirements.txt

echo "Requirements.txt exported"