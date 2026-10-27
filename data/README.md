# data/ — demos_grid5x5_v1

## Expected layout

```text
data/demos/demos_grid5x5_v1/
  SCHEMA.md            # field definitions (stub below until real export)
  manifest.jsonl       # one record per episode
  splits.json          # train / val / test (or train/eval) splits
  episodes/
    episode_0000.h5
    ...
    episode_0999.h5    # 1000 total
```

## Spec

- **Name**: `demos_grid5x5_v1`
- **Count**: 20 SKU × 5×5 × 2 = **1000**
- **IC**: ±100 mm / ±20° (train and eval identical)
- **Format**: RL100-style H5 preferred as source; convert to Flex-π training format via `scripts/convert_rl100_h5_to_flexpi.py`

## Symlink from /data02

When demos live on the training host:

```bash
# example — adjust to the real export path
ln -s /data02/<owner>/demos_grid5x5_v1 \
  /path/to/flexpi-rl100-flip/data/demos/demos_grid5x5_v1
```

Treat linked demos as **read-only**.

## SCHEMA stub

See `data/demos/SCHEMA.md`. Fill concrete HDF5 keys after the first real export; the converter stub documents the *expected* keys it will look for.
