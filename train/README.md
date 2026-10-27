# train/ — three-stage entrypoints

| Dir | Stage | Order dependency |
|-----|-------|------------------|
| `stage1_bc/` | BC fine-tune Flex-π | Needs demos + Flex-π pretrained |
| `stage2_offline/` | Critic → offline RL | Needs Stage-1 policy (+ demo/offline buffer) |
| `stage3_online/` | Online collect / train / gate | Needs Stage-2 policy + live env |

RL100 naming alignment: same BC → offline → online flywheel as [rl100-sim-repro](https://github.com/csgaole/rl100-sim-repro) and upstream [RL-100](https://github.com/Lei-Kun/RL-100), but the policy body is **Flex-π ActionDiT** (visual frozen by default).

Each `start.sh` is runnable and exits with a clear message if deps/data are missing.
