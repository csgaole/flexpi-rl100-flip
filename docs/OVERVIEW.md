# OVERVIEW — Flex-π as cerebellum atomic skill for Laya

## Role

In the broader **Laya** stack, Flex-π is treated as a **cerebellum-style atomic skill**: a fast, low-level visuomotor policy that executes a single flip skill with tight latency, while a higher-level planner (System-2 / ASPIRE-style) can call, gate, or recover around it.

Design intent:

- **Shared visual backbone** — keep Flex-π’s multi-stream world-action backbone (video / DINO / pointmap) as the frozen or slowly updated sensory trunk.
- **Swap / focus Action head** — RL stages primarily adapt **ActionDiT** (and a critic on action chunks), matching RL100’s “improve the action policy, don’t retrain perception from scratch” discipline.
- **One checkpoint, many regimes** — Flex-π already supports action-only (~60 ms) through full joint generation via `infer_joint_*` / `infer_present_*` flags; Stage-1 may start action-only for throughput, then open joint streams if needed.

## Why Flex-π + RL100 stages

| Piece | Source | What we reuse |
|-------|--------|----------------|
| World-action VLA + ActionDiT | Flex-π ([arXiv:2608.10860](https://arxiv.org/abs/2608.10860)) | Pretrain, fine-tune recipe, inference regimes |
| BC → offline → online flywheel | RL-100 + Bill’s `rl100-sim-repro` | Stage naming, IC identity across stages, keep-failed-rollouts rule |
| Flip task / sim | logistics-sorting-sim SKU flip line | Env + `flip_pose_no_drop_v2`-style success |

## Non-goals of this scaffold

- Does **not** ship a fake MuJoCo env that pretends to be logistics-sorting-sim.
- Does **not** invent success rates or checkpoint metrics.
- Does **not** vendor 6B weights into git.

See `INTERFACE.md` for obs/action/done and `IC_SPEC.md` for the ±100mm/±20° contract.
