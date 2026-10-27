# Stage-2 Offline RL — RL100-style on ActionDiT

## Goal

Offline improvement after BC, following RL-100 two-phase discipline:

1. **Train critic** on action chunks (design default **H≈32**)
2. **Offline policy gradient** on ActionDiT with stochastic **log-prob**, **freeze visual**, KL constraint design default **KL≈6** (configurable)

## Order (document — do not skip)

```text
Stage-1 BC ckpt
    → critic fit (demo ± offline buffer)
    → offline RL (KL budget)
    → promote cand_* to checkpoints/ after gate
```

Upstream RL-100 launchers separate critic materialization from BPPO/offline steps (see `scripts/*/Offline/*two_stage*.sh` in `/workspace/RL-100`). Mirror that ordering even when the network is Flex-π ActionDiT.

## Entrypoints

```bash
bash train/stage2_offline/start.sh
# internals (stubs):
bash train/stage2_offline/train_critic.sh
bash train/stage2_offline/train_offline_rl.sh
```
