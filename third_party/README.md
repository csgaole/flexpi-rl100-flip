# third_party/ — Flex-π vendor / submodule

## Preferred: submodule or sibling clone

```bash
# Option A — submodule (source only)
git submodule add https://github.com/geyan21/flex-pi third_party/flex-pi

# Option B — env pointer to local clone (this box)
export FLEXPI_ROOT=/workspace/flex-pi
```

Reference remote: https://github.com/geyan21/flex-pi  
Local scaffold reference: `/workspace/flex-pi`

## Do not

- Copy entire **6B** weight trees into `third_party/` or git
- Strip Flex-π `LICENSE` / notices when vendoring source
- Pretend a minimal fake package named `flexpi` is the real model

## RL-100

Optional: submodule https://github.com/Lei-Kun/RL-100 for offline/online recipe comparison. Stage scripts in this repo are Flex-π-oriented stubs that **document** RL100 ordering (critic → offline PG → online) without requiring a full vendor on day one.
