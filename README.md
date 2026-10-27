# flexpi-rl100-flip

> Flex-π + RL100 three-stage (BC → offline → online) flip-task follow-trainable scaffold.
>
> Public scaffold (prep Asia/Shanghai). **No** 1000 demos / 6B weights / full `runs/` in the initial push — see `UPLOAD_PLAN.md` and Git LFS patterns.
> Mirror style: [csgaole/rl100-sim-repro](https://github.com/csgaole/rl100-sim-repro).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Flex-π arXiv](https://img.shields.io/badge/Flex--π-arXiv%202608.10860-b31b1b.svg)](https://arxiv.org/abs/2608.10860)
[![RL-100](https://img.shields.io/badge/RL--100-paper%20%2B%20code-2ea44f.svg)](https://github.com/Lei-Kun/RL-100)

---

## 三阶段 pipeline / Three-stage pipeline

本仓库把 **Flex-π**（[arXiv:2608.10860](https://arxiv.org/abs/2608.10860)，本地参考 `/workspace/flex-pi` → upstream [geyan21/flex-pi](https://github.com/geyan21/flex-pi)）接到 **RL-100 风格** 的三阶段训练上，任务是物流纸箱 **flip（S2）**，IC 与 Bill 宽 IC 线一致：**±100 mm / ±20°**，数据规格 **demos_grid5x5_v1**（20 SKU × 5×5 × 2 = **1000** demos）。

| Stage | 名称 | 目标 | 入口 |
|------|------|------|------|
| **1** | **BC** | 在 IC±100 示教上 fine-tune Flex-π；优先冻结 visual backbone，聚焦 **ActionDiT**；初期可用 **action-only** 推理体制（~60 ms，`infer_joint_*=false`） | `train/stage1_bc/` |
| **2** | **Offline RL** | RL100 式离线改进：ActionDiT 上随机 log-prob、冻 visual、critic 作用在 action chunk **H≈32**、默认 **KL≈6**（均可配置） | `train/stage2_offline/` |
| **3** | **Online RL** | 同一 sim / 任务 / IC 上在线 flywheel；**保留失败 rollout**（不 retry-until-success）；demos / offline / online **共享同一 IC** | `train/stage3_online/` |

```
demos_grid5x5_v1 (IC ±100mm/±20°)
        │
        ▼
┌───────────────────┐
│ Stage-1 BC        │  Flex-π fine-tune (freeze visual → ActionDiT)
└─────────┬─────────┘
          ▼
┌───────────────────┐
│ Stage-2 Offline RL│  critic → offline PG (KL≈6, H≈32)
└─────────┬─────────┘
          ▼
┌───────────────────┐
│ Stage-3 Online RL │  collect (keep fails) → train → gate
└─────────┬─────────┘
          ▼
   closed-loop eval (500/ckpt style grid)
```

English one-liner: follow-trainable scaffold that fine-tunes Flex-π on Bill’s wide-IC carton flip demos, then runs RL100-style offline and online stages on the **same** IC / env / success criterion.

---

## Task & IC (summary)

| Item | Value |
|------|-------|
| Task | Carton **flip** (S2); success ≈ label-up flip (`flip_pose_no_drop_v2` / FlipFlow S2 spirit) |
| IC | **±100 mm** position, **±20°** yaw — train / eval / online collect **identical** |
| Demos | `demos_grid5x5_v1`: 20 SKU × 5×5 grid × 2 = **1000** |
| Obs → Act | 3×RGB + proprio → **14-dim absolute joints** (dual PiPER) |
| Env | Same logistics-sorting-sim / flip line as RL100 SKU stack — **adapter only**; see `env/README.md` |

Details: `docs/IC_SPEC.md`, `docs/INTERFACE.md`, `docs/OVERVIEW.md`.

---

## Layout

```
README.md                 # this file
UPLOAD_PLAN.md            # what goes to LFS later
LICENSE                   # MIT (matches Flex-π)
docs/                     # OVERVIEW / INTERFACE / IC_SPEC
env/                      # pointer + adapter notes (no fake sim)
data/                     # demos_grid5x5_v1 layout + SCHEMA stub
models/                   # Flex-π pretrained weights (LFS later)
checkpoints/              # curated stage1/2/3 ckpts (LFS later)
train/
  stage1_bc/              # BC fine-tune stubs
  stage2_offline/         # critic → offline RL stubs
  stage3_online/          # online collect/train/gate stubs
eval/                     # closed-loop eval stub
scripts/                  # H5→Flex-π converter + IC check stubs
third_party/              # how to vendor/submodule Flex-π (no 6B weights)
```

---

## Quick start (stubs)

Stubs **fail clearly** if Flex-π, demos, or env are missing — they do **not** invent metrics.

```bash
# 1) Point at Flex-π source (local clone or submodule)
export FLEXPI_ROOT=/workspace/flex-pi   # or third_party/flex-pi

# 2) Symlink demos when available (e.g. A100 /data02)
# ln -s /data02/.../demos_grid5x5_v1 data/demos/demos_grid5x5_v1

# 3) Stage entrypoints
bash train/stage1_bc/start.sh
bash train/stage2_offline/start.sh
bash train/stage3_online/start.sh

# 4) Eval
bash eval/eval_closed_loop.sh
```

See `train/README.md` and each stage’s README for RL100 ordering and Flex-π config knobs (`infer_joint_*`, action-only vs full joint).

---

## References

- Flex-π paper: https://arxiv.org/abs/2608.10860 · code: https://github.com/geyan21/flex-pi · site: https://flex-pi.github.io/
- RL-100: https://github.com/Lei-Kun/RL-100
- Bill SKU flip follow-trainable mirror: https://github.com/csgaole/rl100-sim-repro
- Local box refs used while scaffolding: `/workspace/flex-pi`, `/workspace/RL-100`

## License

MIT — see `LICENSE`. When vendoring Flex-π, keep its MIT notice; RL-100 code (if vendored) remains Apache-2.0.
