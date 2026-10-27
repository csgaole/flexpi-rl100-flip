# INTERFACE — obs / action / done contract

Aligned with Bill’s RL100 SKU flip line and FlipFlow S2 / `flip_pose_no_drop_v2` spirit.
This document is a **contract**; adapters must map real env outputs into this shape.

## Observation

| Stream | Spec |
|--------|------|
| RGB cameras | **3×** RGB: typically `global`, `left_wrist`, `right_wrist` (sizes follow sim / Flex-π task config; RL100 line often 240×320 then encode/resize) |
| Proprio | Joint / gripper measurements from `physics.proprio()` (RL100 BC uses richer proprio; Flex-π adapter should document which slice is fed) |

Flex-π multi-stream training may additionally use depth / DINO / pointmap when available; **action-only** deploy can drop generated visual joints via:

```text
+EVALUATION.infer_joint_video=false
+EVALUATION.infer_joint_dino=false
+EVALUATION.infer_joint_pointmap=false
```

(see Flex-π README “Inference Regimes”; local `/workspace/flex-pi`).

## Action

| Item | Spec |
|------|------|
| Dim | **14** = dual arm × (6 joints + 1 gripper column) |
| Semantics | **Absolute joint targets** (rad), same spirit as RL100 `absolute_joint_target_v1` |
| Gripper | Often fixed-width / non-controllable in the flip skill line — document in adapter if columns are overwritten |
| Chunk | Design default for Stage-2/3 critic: horizon **H≈32** (configurable; Flex-π task configs also use 32-step action horizons on some embodiments) |

## Done / success

Success is **label-up flip**, not full outfeed sorting:

- Criterion family: **`flip_pose_no_drop_v2`** (FlipFlow S2 spirit)
- Typical signals: final `label_up` high, parcel bottom height above drop threshold, no drop during episode, episode complete
- Do **not** mix with outfeed-only success definitions when reporting flip metrics

Exact numeric thresholds live in the real `task_success` implementation on the sim host — this scaffold does not re-encode fake thresholds.

## Episode / timing (reference)

RL100 flip stack reference (for adapter authors):

- Physics / action often **240 Hz**; camera **30 Hz**
- Episode length on the order of **2 s** for the long-edge flip task

Flex-π control rate follows the chosen task config after conversion — document the mapping in the converter / env adapter when wired.
