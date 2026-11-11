#!/usr/bin/env bash
# Validate every skill plus the repository index. No third-party deps required.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required to run the validator" >&2
  exit 1
fi

python3 "$ROOT/scripts/validate.py" --check-readme
python3 -m json.tool "$ROOT/.claude-plugin/marketplace.json" >/dev/null
echo "marketplace.json is valid JSON."
