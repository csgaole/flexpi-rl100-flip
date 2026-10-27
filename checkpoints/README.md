# checkpoints/ — curated stage ckpts (LFS later)

Promote only **gated** checkpoints:

```text
checkpoints/
  stage1_bc_<tag>.pt           # or .safetensors
  stage2_offline_kl6_<tag>.pt  # encode KL / H in the name
  stage3_online_best_<tag>.pt
```

Full `runs/` trees stay gitignored. See `UPLOAD_PLAN.md`.
