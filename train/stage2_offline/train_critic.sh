#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
CFG="$ROOT/train/stage2_offline/config.yaml"
CKPT="${STAGE1_CKPT:-$ROOT/checkpoints/stage1_bc_latest.pt}"
echo "[stage2_offline/critic] would fit critic on action chunk H≈32"
echo "  config=$CFG"
echo "  policy_init=$CKPT"
if [[ ! -f "$CKPT" ]]; then
  echo "ERROR: Stage-1 checkpoint not found: $CKPT" >&2
  echo "Place a curated BC ckpt under checkpoints/ (LFS) or set STAGE1_CKPT=..." >&2
  exit 2
fi
echo "ERROR: critic trainer not wired yet (stub). See train/stage2_offline/README.md" >&2
exit 3
