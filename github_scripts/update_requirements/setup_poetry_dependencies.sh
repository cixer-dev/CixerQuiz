#!/usr/bin/env bash

set -Eeuo pipefail

exit_code=0

trap '
    exit_code=$?
    printf "Error: command failed with exit code %s: %s\n" \
        "$exit_code" "$BASH_COMMAND" >&2
    exit "$exit_code"
' ERR

echo "Installing and updating pip..."
sudo apt-get update
sudo apt-get install -y python3-pip
python3 -m pip install --upgrade pip

echo "Installing Poetry..."
python3 -m pip install --upgrade poetry
poetry --version

echo "Poetry is installed."

poetry lock
poetry install
