#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
echo "[stage3_online/train] stub"
case "train" in
  collect)
    echo "  keep_failed_rollouts=true  retry_until_success=false  IC=±100mm/±20°"
    ;;
  train)
    echo "  would update ActionDiT from online buffer (visual frozen by default)"
    ;;
  gate)
    echo "  would call eval/eval_closed_loop.sh before promoting ckpt"
    ;;
esac
if [[ ! -d "${FLEXPI_ROOT:-/workspace/flex-pi}" ]]; then
  echo "ERROR: FLEXPI_ROOT missing" >&2
  exit 2
fi
# Env presence check (pointer only)
if [[ ! -d "$ROOT/env" ]]; then
  echo "ERROR: env/ missing" >&2
  exit 2
fi
echo "ERROR: stage3 train not wired yet (stub). See train/stage3_online/README.md" >&2
exit 3
