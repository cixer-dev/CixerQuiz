#!/usr/bin/env bash

set -euo pipefail

bash install_pip.sh
bash install_poetry.sh
bash install_poetry-export-plugin.sh
bash update_requirements.sh