#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
KL="${KL_TARGET:-6}"
H="${ACTION_CHUNK_HORIZON:-32}"
echo "[stage2_offline/offline_rl] KL≈${KL} H≈${H} freeze_visual=1 stochastic log-prob on ActionDiT"
if [[ ! -d "${FLEXPI_ROOT:-/workspace/flex-pi}" ]]; then
  echo "ERROR: FLEXPI_ROOT missing (${FLEXPI_ROOT:-/workspace/flex-pi})" >&2
  exit 2
fi
echo "ERROR: offline RL loop not wired yet (stub). Critic must run first (RL100 order)." >&2
exit 3
