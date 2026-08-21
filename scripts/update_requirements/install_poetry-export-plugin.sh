#!/usr/bin/env bash

set -euo pipefail

poetry self add poetry-plugin-export
poetry lock
poetry install
