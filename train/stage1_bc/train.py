#!/usr/bin/env python3
"""Stage-1 BC stub: Flex-π fine-tune on demos_grid5x5_v1.

Refuses to invent metrics. Wire to Flex-π training entry once FLEXPI_ROOT + demos exist.
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


def main() -> int:
    p = argparse.ArgumentParser(description="Stage-1 BC Flex-π fine-tune (stub)")
    p.add_argument("--config", type=Path, default=Path(__file__).with_name("config.yaml"))
    args = p.parse_args()

    flexpi_root = os.environ.get("FLEXPI_ROOT", "").strip()
    demos = REPO / "data" / "demos" / "demos_grid5x5_v1"
    missing = []

    if not flexpi_root:
        missing.append("FLEXPI_ROOT is unset (export FLEXPI_ROOT=/workspace/flex-pi or third_party/flex-pi)")
    elif not Path(flexpi_root).is_dir():
        missing.append(f"FLEXPI_ROOT does not exist: {flexpi_root}")

    if not demos.is_dir() or not any(demos.iterdir()):
        missing.append(
            f"demos missing or empty: {demos} "
            "(symlink demos_grid5x5_v1 — see data/README.md)"
        )

    if not args.config.is_file():
        missing.append(f"config not found: {args.config}")

    if missing:
        print("Stage-1 BC stub: refusing to start — dependencies missing:", file=sys.stderr)
        for m in missing:
            print(f"  - {m}", file=sys.stderr)
        print(
            "\nNext: install Flex-π, place/symlink demos, then replace this stub "
            "with a call into Flex-π's train entry (see /workspace/flex-pi/scripts/train_flexpi_*.sh).",
            file=sys.stderr,
        )
        return 2

    print(
        "Stage-1 BC stub: deps present, but training launch is not wired yet.\n"
        f"  FLEXPI_ROOT={flexpi_root}\n"
        f"  demos={demos}\n"
        f"  config={args.config}\n"
        "Implement: freeze visual backbone, fine-tune ActionDiT on IC±100 demos "
        "(action-only eval OK).",
        file=sys.stderr,
    )
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
