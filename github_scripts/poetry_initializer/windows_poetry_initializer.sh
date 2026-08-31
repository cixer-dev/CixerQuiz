#!/usr/bin/env bash

set -Eeuo pipefail

exit_code=0

trap '
    exit_code=$?
    printf "Error: command failed with exit code %s: %s\n" \
        "$exit_code" "$BASH_COMMAND" >&2
    exit "$exit_code"
' ERR

echo "Checking Python installation..."
python --version

echo "Installing and updating pip..."
python -m pip install --upgrade pip

echo "Installing or updating Poetry..."
python -m pip install --upgrade poetry

echo "Poetry version:"
poetry --version

echo "Installing project dependencies..."
poetry install

echo "Dependencies installed successfully."
