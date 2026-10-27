#!/usr/bin/env bash
# Stage-2: critic → offline RL (RL100 order)
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"
export FLEXPI_ROOT="${FLEXPI_ROOT:-/workspace/flex-pi}"
echo "[stage2_offline] running critic then offline RL stubs"
bash train/stage2_offline/train_critic.sh
bash train/stage2_offline/train_offline_rl.sh
