# models/ — Flex-π pretrained weights

## Where weights go

```text
models/pretrained/
  # Flex-π release ckpt(s) — Git LFS later
  # ActionDiT backbone used by Flex-π train prep, e.g.
  #   ActionDiT_linear_interp_Wan22_alphascale_1024hdim.pt
```

Upstream prep notes live in Flex-π `docs/INSTALL.md` (local `/workspace/flex-pi/docs/INSTALL.md`): Wan2.2-TI2V-5B + resampled ActionDiT backbone. **Do not** commit the full multi-GB tree into this git repo without LFS + an explicit upload plan update.

## Action-only vs full joint

| Regime | Flags (Flex-π) | Latency note |
|--------|----------------|--------------|
| Action-only | `infer_joint_video/dino/pointmap=false` | ~60 ms / call (RTX 5090, paper) |
| Full joint | all `infer_joint_*=true` | ~193 ms / call (paper) |

Stage-1 may fine-tune with full training objective but **deploy/eval** action-only for throughput; document the regime used in each run’s `REPORT.md`.
