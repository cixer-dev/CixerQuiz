#!/usr/bin/env bash

set -euo pipefail


SETUP_POETRY_DEPENDENCIES_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="$(cd -- "$(dirname -- "$SETUP_POETRY_DEPENDENCIES_DIR")" && pwd)"
GITHUB_DIR="$(cd -- "$(dirname -- "$SCRIPTS_DIR")" && pwd)"
PROJECT_DIR="$(cd -- "$(dirname -- "$GITHUB_DIR")" && pwd)"

cd "$PROJECT_DIR"

poetry export \
    --format requirements.txt \
    --output requirements.txt
