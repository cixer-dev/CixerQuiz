#!/usr/bin/env bash

set -Eeuo pipefail

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

if [[ $# -ne 3 ]]; then
    printf "Usage: %s APP_NAME EXE_PATH APP_LOGO_PATH\n" "$0" >&2
    exit 2
fi

APP_NAME="$1"
EXE_PATH="$2"
APP_LOGO_PATH="$3"
DIST_PATH="$(dirname "$EXE_PATH")"

poetry run pyinstaller \
    --clean \
    --onefile \
    --windowed \
    --name "$APP_NAME" \
    --icon "$APP_LOGO_PATH" \
    --distpath "$DIST_PATH" \
    --hidden-import PySide6.QtMultimedia \
    --hidden-import PySide6.QtMultimediaWidgets \
    main.py

if [[ ! -f "$EXE_PATH" ]]; then
    printf "ERROR: Expected executable was not created: %s\n" "$EXE_PATH" >&2
    exit 1
fi
