#!/usr/bin/env python3
"""Stub converter: RL100 H5 demos → Flex-π training format.

Implements a clear skeleton with TODOs. Does **not** pretend conversion works
without real schemas / Flex-π dataset builders.

Expected RL100-style H5 keys (document — confirm against a real episode before coding):
  - cameras / rgb streams for global, left_wrist, right_wrist
  - proprio (float32 [T, D])
  - actions or action/effective absolute joints [T, 14]
  - IC metadata: dx, dy, yaw (or equivalent) for ±100mm/±20° asserts
  - optional: success, sku_id, grid indices

Flex-π side: follow dataset builder patterns under
  /workspace/flex-pi/scripts/yam_dataset_builder/
and task configs under /workspace/flex-pi/configs/task/.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


EXPECTED_RL100_KEYS = {
    "actions": "float32 [T, 14] absolute joint targets (or nested action/effective)",
    "proprio": "float32 [T, D] proprioception",
    "rgb_global": "uint8 frames — name may differ (e.g. observations/rgb/global)",
    "rgb_left_wrist": "uint8 frames",
    "rgb_right_wrist": "uint8 frames",
    "ic_dx_m": "float — IC position x offset",
    "ic_dy_m": "float — IC position y offset",
    "ic_yaw_rad": "float — IC yaw offset",
    "sku_id": "str|int",
}


def convert_episode(src: Path, dst: Path) -> None:
    """TODO: open H5, validate keys, remap cameras/actions into Flex-π sample layout."""
    raise NotImplementedError(
        f"convert_episode not implemented (src={src}, dst={dst}). "
        "Inspect one real H5, then map keys listed in EXPECTED_RL100_KEYS."
    )


def main() -> int:
    p = argparse.ArgumentParser(description="RL100 H5 → Flex-π format (stub)")
    p.add_argument("--src", type=Path, required=True, help="demos_grid5x5_v1 root or episodes dir")
    p.add_argument("--dst", type=Path, required=True, help="output Flex-π dataset dir")
    p.add_argument("--dry-run", action="store_true", help="only print expected keys / plan")
    args = p.parse_args()

    print("Expected RL100 H5 keys (confirm on a real file before implementing):")
    for k, v in EXPECTED_RL100_KEYS.items():
        print(f"  - {k}: {v}")

    if not args.src.exists():
        print(f"ERROR: source not found: {args.src}", file=sys.stderr)
        print("Symlink demos first (data/README.md).", file=sys.stderr)
        return 2

    if args.dry_run:
        print(f"dry-run OK: would convert {args.src} → {args.dst}")
        return 0

    # TODO: iterate episodes, call convert_episode
    print(
        "ERROR: conversion skeleton only — refusing to write fake Flex-π samples.\n"
        "Next steps:\n"
        "  1) h5dump/python one episode; lock key names\n"
        "  2) map 14-D absolute actions + 3 RGB into Flex-π builder schema\n"
        "  3) preserve IC metadata for scripts/check_ic_distribution.py",
        file=sys.stderr,
    )
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
