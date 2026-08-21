#!/usr/bin/env bash

set -euo pipefail

bash scripts/setup_poetry_dependencies/main.sh
bash scripts/update_requirements/install_poetry-export-plugin.sh
bash scripts/update_requirements/update_requirements.sh