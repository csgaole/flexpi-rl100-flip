# SCHEMA — demos_grid5x5_v1 (stub)

> Placeholder until the real 1000-demo export is attached. Do not invent episode metrics here.

## Episode record (planned)

| Field | Type | Meaning |
|-------|------|---------|
| `sku_id` | str / int | One of 20 SKUs |
| `grid_i`, `grid_j` | int | 5×5 cell indices |
| `repeat` | int | 0 or 1 (×2) |
| `ic_dx_m`, `ic_dy_m`, `ic_yaw_rad` | float | IC within ±0.100 m / ±20° |
| `success` | bool | label-up flip criterion |
| `rgb/*` or camera groups | uint8 video/frames | 3 cameras |
| `proprio` | float32 [T, D] | proprio stream |
| `actions` | float32 [T, 14] | absolute joint targets |

Exact HDF5 key names must match what `scripts/convert_rl100_h5_to_flexpi.py` documents once wired against a real episode.
