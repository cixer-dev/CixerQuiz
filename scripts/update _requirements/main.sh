#!/usr/bin/env bash

set -euo pipefail

bash scripts/setup_poetry_dependencies/main.sh
bash scripts/update _requirements/install_poetry-export-plugin.sh
bash scripts/update _requirements/update_requirements.sh