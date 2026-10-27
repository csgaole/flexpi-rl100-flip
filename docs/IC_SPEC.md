# IC_SPEC — initial condition (±100 mm / ±20°)

## Contract (Bill wide-IC line)

| Parameter | Range | Notes |
|-----------|-------|-------|
| Position jitter | **±100 mm** in plane (dx, dy) | Uniform unless a grid cell says otherwise |
| Yaw jitter | **±20°** | Relative to the flip-task nominal yaw |
| Train / eval / online | **Identical IC distribution** | No hidden tightening at eval |

This differs from the older **nominal** RL100 cell (`±5 mm / ±2°`, e.g. `p5_y2`). This repo’s default line is the **wide** IC.

## demos_grid5x5_v1

| Factor | Count |
|--------|-------|
| SKUs | **20** |
| Position/yaw grid | **5×5** cells spanning the ±100 mm / ±20° box |
| Repeats / variants | **×2** |
| **Total demos** | **20 × 5 × 5 × 2 = 1000** |

Expected on-disk name: `data/demos/demos_grid5x5_v1/` (see `data/README.md`).

## Stage identity rule

1. Stage-1 BC trains on demos drawn from this IC.
2. Stage-2 offline improves on buffers whose IC matches (demos ± offline rollouts with same sampler).
3. Stage-3 online **collects with the same IC**; **keeps failed rollouts** (no retry-until-success that would bias IC / success).

Violating IC identity across stages makes gates incomparable — treat as a bug.

## Checker

```bash
python scripts/check_ic_distribution.py --demos data/demos/demos_grid5x5_v1 \
  --pos-mm 100 --yaw-deg 20
```

Stub exits non-zero with a clear message until demos exist and schema fields are wired.
