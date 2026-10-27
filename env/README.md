# env/ — logistics-sorting-sim / flip task (adapter notes)

## Do not invent a fake sim

This directory is a **pointer + adapter contract**, not a reimplementation of MuJoCo logistics-sorting-sim.

Reuse the **same** env / task line as Bill’s RL100 SKU flip stack:

- Public mirror: [csgaole/rl100-sim-repro](https://github.com/csgaole/rl100-sim-repro) → `env/logistics-sorting-sim`, `env/sku09-task-success`
- Local / cluster: typically under `/data02/kemove/...` or a vendored copy next to training hosts
- ASPIRE-adjacent reference on this box: `/workspace/aspire-rl100-flip/vendor/rl100_stack/logistics-sorting-sim` (if present)

## Adapter responsibilities

When wiring Flex-π training / eval:

1. Construct the real `LogisticsSortingEnv` (or equivalent) with the correct SKU scene.
2. Apply **IC ±100 mm / ±20°** (see `docs/IC_SPEC.md`) — not the nominal ±5 mm / ±2° cell unless ablating.
3. Map obs → Flex-π batch format (3×RGB + proprio).
4. Map Flex-π 14-D absolute joint outputs → env `step` / command path (respect slew / grip overrides if the skill line requires them).
5. Score with **label-up flip** success (`flip_pose_no_drop_v2` spirit) — see `docs/INTERFACE.md`.

## Suggested layout (when you copy for real)

```text
env/
  README.md                 # this file
  adapter_flexpi.py         # TODO: thin wrapper (not present in scaffold)
  # optional: submodule or copy of logistics-sorting-sim
```

Until the real sim is available on the machine, stage `start.sh` scripts must **exit with a clear error** rather than silently using a stub physics engine.
