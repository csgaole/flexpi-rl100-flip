#!/usr/bin/env bash
# Closed-loop eval stub — 500/ckpt style when N_EPISODES is set.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

CKPT="${CKPT:-}"
N_EPISODES="${N_EPISODES:-}"
FLEXPI_ROOT="${FLEXPI_ROOT:-/workspace/flex-pi}"
IC_POS_MM="${IC_POS_MM:-100}"
IC_YAW_DEG="${IC_YAW_DEG:-20}"

echo "[eval_closed_loop] Flex-π flip closed-loop"
echo "  FLEXPI_ROOT=$FLEXPI_ROOT"
echo "  CKPT=${CKPT:-<unset>}"
echo "  N_EPISODES=${N_EPISODES:-<unset>}"
echo "  IC=±${IC_POS_MM}mm / ±${IC_YAW_DEG}°"

err=0
if [[ -z "$CKPT" ]]; then
  echo "ERROR: set CKPT=path/to/checkpoint" >&2
  err=1
elif [[ ! -f "$CKPT" ]]; then
  echo "ERROR: checkpoint not found: $CKPT" >&2
  err=1
fi
if [[ -z "$N_EPISODES" ]]; then
  echo "ERROR: set N_EPISODES (e.g. 500 for 500/ckpt-style formal eval)" >&2
  err=1
fi
if [[ ! -d "$FLEXPI_ROOT" ]]; then
  echo "ERROR: FLEXPI_ROOT missing: $FLEXPI_ROOT" >&2
  err=1
fi
if [[ "$err" -ne 0 ]]; then
  exit 2
fi

echo "ERROR: closed-loop eval not wired to real logistics-sorting-sim yet (stub)." >&2
echo "Wire: load Flex-π policy (action-only or joint), reset with IC±${IC_POS_MM}/${IC_YAW_DEG}, score flip_pose_no_drop_v2." >&2
exit 3
