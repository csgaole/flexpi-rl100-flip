#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"
export FLEXPI_ROOT="${FLEXPI_ROOT:-/workspace/flex-pi}"
echo "[stage3_online] collect → train → gate (stubs; keep failures; identical IC)"
bash train/stage3_online/collect.sh
bash train/stage3_online/train.sh
bash train/stage3_online/gate.sh
