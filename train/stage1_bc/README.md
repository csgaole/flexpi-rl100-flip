# Stage-1 BC — Flex-π fine-tune

## Goal

Fine-tune Flex-π on `demos_grid5x5_v1` (IC ±100 mm / ±20°).

**Defaults (design):**

- Freeze visual backbone; train / adapt **ActionDiT** (and any explicit action head params)
- Action-only regime OK for early closed-loop checks (`infer_joint_*=false`, ~60 ms)
- Full joint training dropout can still follow Flex-π’s flex randomization if enabled in config

## Entrypoints

```bash
bash train/stage1_bc/start.sh
# or
python train/stage1_bc/train.py --config train/stage1_bc/config.yaml
```

## Config

`config.yaml` points at a Flex-π fine-tune recipe (Hydra-style knobs mirrored from `/workspace/flex-pi/configs`). Fill real dataset paths before launch.
