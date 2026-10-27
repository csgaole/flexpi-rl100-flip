# Stage-3 Online RL — flywheel on identical IC

## Goal

Online collect → train → gate on the **same** sim / flip task / **IC ±100 mm / ±20°**.

## Hard rules

1. **Keep failed rollouts** — no retry-until-success that biases the buffer (Bill RL100 rule).
2. Demos / offline / online share **identical IC** (`docs/IC_SPEC.md`).
3. Gate with closed-loop eval (`eval/eval_closed_loop.sh`) before promoting to `checkpoints/`.

## Entrypoints

```bash
bash train/stage3_online/start.sh
# pieces:
bash train/stage3_online/collect.sh
bash train/stage3_online/train.sh
bash train/stage3_online/gate.sh
```
