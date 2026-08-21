#!/usr/bin/env bash

set -euo pipefail

poetry export \
    --format requirements.txt \
    --output requirements.txt
