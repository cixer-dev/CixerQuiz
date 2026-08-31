#!/usr/bin/env bash
set -Eeuo pipefail

exit_code=0

error_handler() {
    local exit_code=$?
    printf \
        'BASH ERROR: command failed with exit code %d\nCommand: %s\n' \
        "$exit_code" \
        "$BASH_COMMAND" \
        >&2
    exit "$exit_code"
}
trap error_handler ERR

echo "Installing and updating pip..."
sudo apt-get update
sudo apt-get install -y python3-pip
python3 -m pip install --upgrade pip

echo "Installing Poetry..."
python3 -m pip install --upgrade poetry
poetry --version
echo "Poetry is installed."

echo "Resolving project dependencies with Poetry..."
poetry lock
echo "Poetry dependencies have been resolved."

echo "Installing Poetry dependencies..."
poetry install
echo "Poetry dependencies are installed"