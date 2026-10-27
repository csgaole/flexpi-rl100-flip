#!/usr/bin/env python3
"""Stub: assert demo IC matches ±pos_mm / ±yaw_deg (default ±100 / ±20)."""
from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser(description="Check demo IC distribution (stub)")
    p.add_argument("--demos", type=Path, required=True)
    p.add_argument("--pos-mm", type=float, default=100.0)
    p.add_argument("--yaw-deg", type=float, default=20.0)
    p.add_argument("--atol-mm", type=float, default=1.0, help="tolerance beyond stated box")
    args = p.parse_args()

    if not args.demos.exists():
        print(f"ERROR: demos path not found: {args.demos}", file=sys.stderr)
        return 2

    # Detect empty placeholder (only .gitkeep / SCHEMA)
    entries = [e for e in args.demos.rglob("*") if e.is_file() and e.name != ".gitkeep"]
    h5s = [e for e in entries if e.suffix == ".h5"]
    if not h5s:
        print(
            f"ERROR: no .h5 episodes under {args.demos}. "
            f"Expected demos_grid5x5_v1 with IC ±{args.pos_mm:g}mm / ±{args.yaw_deg:g}°.",
            file=sys.stderr,
        )
        return 2

    pos_m = args.pos_mm / 1000.0
    yaw_rad = math.radians(args.yaw_deg)
    print(
        f"Would assert |dx|,|dy| ≤ {pos_m} m (+{args.atol_mm} mm tol) "
        f"and |yaw| ≤ {yaw_rad:.6f} rad on {len(h5s)} episodes."
    )
    print(
        "ERROR: IC field extraction not wired — implement after SCHEMA keys are fixed "
        "(ic_dx_m / ic_dy_m / ic_yaw_rad or equivalent).",
        file=sys.stderr,
    )
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
