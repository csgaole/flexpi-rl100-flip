#!/usr/bin/env bash
# Stage-1 BC launcher stub — fails clearly if deps/data missing.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"
export FLEXPI_ROOT="${FLEXPI_ROOT:-/workspace/flex-pi}"
echo "[stage1_bc] ROOT=$ROOT FLEXPI_ROOT=$FLEXPI_ROOT"
exec python3 train/stage1_bc/train.py --config train/stage1_bc/config.yaml "$@"
