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
    printf \
        'Incorrect argument number.\nUsage: %s APP_NAME DIST_PATH LAUNCHER_PATH\n' \
        "$0" \
        >&2
    exit 1
fi

APP_NAME="$1"
DIST_PATH="$2"
LAUNCHER_PATH="$3"

printf 'Installing project dependencies with Poetry...\n'

printf 'Building the application with PyInstaller...\n'
poetry run pyinstaller \
    --clean \
    --noconfirm \
    --onefile \
    --windowed \
    --name "$APP_NAME" \
    --distpath "$DIST_PATH" \
    main.py

cat > "$LAUNCHER_PATH" <<EOF
#!/usr/bin/env bash

set -Eeuo pipefail

APP_NAME="$APP_NAME"
SCRIPT_DIR="\$(dirname -- "\${BASH_SOURCE[0]}")"
cd "\$SCRIPT_DIR"
APP_BINARY_PATH="\$SCRIPT_DIR/\$APP_NAME"

if [[ ! -x "\$APP_BINARY_PATH" ]]; then
    printf 'Application binary not found or is not executable: %s\n' \
        "\$APP_BINARY_PATH" \
        >&2
    exit 1
fi

exec "\$APP_BINARY_PATH"
EOF

printf 'Application built successfully.\n'
printf 'Launcher in: %s\n' "$LAUNCHER_PATH"