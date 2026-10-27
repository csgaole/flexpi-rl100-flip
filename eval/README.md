# eval/ — closed-loop grid eval

## Intent

Evaluate a Flex-π (or stage) checkpoint on the flip task under **IC ±100 mm / ±20°**, same contract as training.

## 500/ckpt style notes

Bill’s RL100 gates often use large episode grids (e.g. hundreds per candidate). A common pattern:

- **Screen**: fewer episodes / cheaper sampler for candidate filtering
- **Formal**: ~**500 episodes per checkpoint** (or a documented grid covering SKU × IC cells) before promote

This scaffold does **not** hard-code a fake success rate. Set `N_EPISODES` explicitly when running.

```bash
N_EPISODES=500 CKPT=checkpoints/stage3_online_best.pt bash eval/eval_closed_loop.sh
```

Success criterion: label-up flip (`flip_pose_no_drop_v2` spirit) — see `docs/INTERFACE.md`.
