# UPLOAD_PLAN — public GitHub `flexpi-rl100-flip`

Prepared for follow-trainable release. Initial push is **code + docs + stubs only**.

## Include later (Git LFS)

| Path | Role | Notes |
|------|------|-------|
| `data/demos/demos_grid5x5_v1/` | 1000 H5 (or Flex-π converted) demos | 20 SKU × 5×5 × 2; IC ±100mm/±20° |
| `models/pretrained/` | Flex-π pretrained / ActionDiT backbone ckpts | Do **not** dump full 6B tree into git casually; prefer LFS + HF mirror pointer |
| `checkpoints/stage1_*.pt` (or `.safetensors`) | Curated Stage-1 BC | After BC gate |
| `checkpoints/stage2_*.pt` | Curated Stage-2 offline | After offline gate (document KL used) |
| `checkpoints/stage3_*.pt` | Curated Stage-3 online best | After online gate |

Approximate sizes TBD when measured on `/data02` — fill this table before the LFS commit.

## Exclude always

- Entire `runs/` / `outputs/` / `wandb/` (full training trees)
- Raw scratch under `data/demos_raw/`, `data/raw/`
- Intermediate critic dumps not promoted to `checkpoints/`
- Copied Flex-π 6B weight trees under `third_party/` (submodule **source** only)

## Initial scaffold commit

- Markdown docs, shell/Python stubs, `.gitignore`, `.gitattributes` (LFS patterns ready)
- Empty `data/demos/`, `models/`, `checkpoints/` placeholders (`.gitkeep`)
- **No** `*.h5` / `*.pt` / `*.safetensors` payloads

## Procedure when ready

1. `git lfs install` (local)
2. Symlink or hardlink curated demos/ckpts into the paths above
3. `git add` only curated paths; confirm `git lfs ls-files`
4. Commit + push (no force-push, no `--no-verify`)
