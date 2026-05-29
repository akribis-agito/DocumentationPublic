---
keyword: DualLoopFact
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 270
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 1
  - 6553600
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
---
# DualLoopFact

Scaling factor that unit-matches the velocity-loop signals in dual-loop control.

## Overview

`DualLoopFact` scales the velocity-loop signals so that the velocity reference and the velocity feedback share the same unit, even though the position (load) feedback and the velocity (motor) feedback may have different resolutions. The position-loop output and the velocity reference are expressed in load units, while the velocity feedback comes from the motor encoder; `DualLoopFact` reconciles the two.

`DualLoopFact` is set to `65536` (the default) when the load and motor feedback share the same resolution (scaling factor of 1). It cannot be changed while the axis is in motion or the motor is on.

## How it works

`DualLoopFact` is a fixed-point factor with `65536` representing a ratio of 1. The controller derives the working velocity-loop scaling from it as described below, and applies the same factor when scaling the dual-loop position limits and the shaped position reference.

To keep precision, the controller chooses where to apply the scaling based on whether `DualLoopFact` is at least `65536` (ratio ≥ 1) or below it (ratio &lt; 1):

| `DualLoopFact` | Velocity-loop reference scaling | Velocity feedback scaling | Common unit |
|---|---|---|---|
| ≥ 65536 (ratio ≥ 1) | unchanged (gain 1) | motor velocity × (`DualLoopFact` / 65536) | main/load encoder counts |
| &lt; 65536 (ratio &lt; 1) | × (65536 / `DualLoopFact`) | unchanged (gain 1) | auxiliary/motor encoder counts |

In both cases the reference and the feedback end up in the same unit — the finer-resolution of the two — so the velocity loop operates on matched signals.

The scaling factor in use, $k$ will be

$$
k = \frac{65536}{\text{DualLoopFact}}
$$

$k$ is defined as follows.

$$
k = \frac{\text{motor feedback count per physical unit}}{\text{load feedback count per physical unit}} = \frac{\text{load feedback physical unit per count}}{\text{motor feedback physical unit per count}}
$$

DualLoopFact is therefore

$$
\text{DualLoopFact} = \frac{65536 \cdot \text{motor feedback physical unit per count}}{\text{load feedback physical unit per count}}
$$

## Examples

The motor feedback uses 4µm SINCOS encoder at 4096x interpolation factor (0.97656nm per count).

The load feedback uses 200nm SINCOS encoder at 8192x interpolation factor (24.41pm per count).

Then,

$$
\text{DualLoopFact} = \frac{65536 \cdot 0.97656}{24.41 \cdot 0.001} = 2621440
$$

```text
ADualLoopFact=2621440  ; set the load-to-motor scaling factor
ADualLoopFact          ; read back the factor
```

## See also

- [DualLoopOn](DualLoopOn.md) — enable dual-loop control
- [DualLoopStat](DualLoopStat.md) — active dual-loop status
- [DualEncSwapOn](DualEncSwapOn.md) — pseudo dual-loop, which uses this factor to scale the auxiliary feedback into load units
