---
summary: Speed percentage override applied to CNC motion group A (or B).
---
# CNCASpeedPer/CNCBSpeedPer

Speed percentage override applied to CNC motion group A (or B).

## Overview

`CNCASpeedPer` (and its `CNCBSpeedPer` counterpart) is an on-the-fly speed-percentage override for CNC group A (or B), as a percentage. Setting it to `100` runs the programmed segment speeds; lower values slow the whole path proportionally, higher values speed it up, all without reprogramming the segment queue. It is a non-axis parameter, not saved to flash, and can be changed at any time, including during motion.

The defining difference from [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) is that **`CNCASpeedPer` scales the path speed only** — it does not change the acceleration or deceleration. Lowering it therefore reduces the cruise feed rate while the ramps stay as programmed.

## How it works

Each control cycle the controller multiplies the commanded path speed [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) by `CNCASpeedPer/100` (together with the [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) factor and the per-segment speed factor) to form the cruise target that the path velocity ramps toward. Because only the **speed** target is scaled by `CNCASpeedPer` and the acceleration and deceleration are left unchanged, reducing `CNCASpeedPer` lowers the cruise feed rate but the path takes the same ramp rates to and from that lower cruise.

The segment-end speed used for cornering/look-ahead is also scaled by the same speed factor, so corner blending stays consistent as the override is changed.

This is distinct from `CNCAPercents`, which scales speed **and** the accel/decel ramps (and so effectively rescales the time of the whole motion). The two factors multiply, so the net speed scaling is `(CNCAPercents/100) × (CNCASpeedPer/100)`.

### CNCB note

`CNCBSpeedPer` is the identical override for the independent second CNC group.

## Examples

```text
ACNCASpeedPer=100    ; run at programmed segment speeds
ACNCASpeedPer=50     ; half the feed rate, same accel/decel ramps
ACNCBSpeedPer=120    ; 20 % faster on group B
```

## See also

- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — commanded path speed this scales
- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — scales speed and accel/decel (rescales time)
- [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) — resulting resultant velocity
