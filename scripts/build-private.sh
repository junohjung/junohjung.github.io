#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
bundle exec jekyll build --config _config.yml,_config.preview.yml
python3 scripts/validate-site.py dist
