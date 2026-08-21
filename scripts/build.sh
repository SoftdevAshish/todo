#!/bin/bash

  set -e
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  PROJECT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"      # todo/
  WHEELS_DIR="$(cd "${PROJECT_DIR}/../wheels" && pwd)" # wheels/
#  ================================================
  # Project Directory
#  ================================================
  echo "Project directory: ${PROJECT_DIR}"
#  ================================================
  # Wheels Directory
#  ================================================
  echo "Wheels directory:  ${WHEELS_DIR}"

  echo "Freezing installed packages to requirements.txt..."
  pip freeze > "${PROJECT_DIR}/requirements.txt"

  echo "Downloads all library in wheels folder."
  echo "Downloading all packages listed in requirements.txt as wheels..."
  pip download \
    -r "${PROJECT_DIR}/requirements.txt" \
    -d "${WHEELS_DIR}" \
    --no-cache-dir

  echo "Done. requirements.txt updated, wheels saved to ${WHEELS_DIR}"
