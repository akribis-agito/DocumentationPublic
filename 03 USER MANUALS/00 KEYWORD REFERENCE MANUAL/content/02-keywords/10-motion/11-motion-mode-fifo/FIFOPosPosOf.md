---
keyword: FIFOPosPosOf
summary: Position offset added to every FIFO position segment.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 662
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPosPosOf

Position offset added to every FIFO position segment.

## Overview

`FIFOPosPosOf` is a constant position offset, in position counts, added to every streamed target before it becomes the axis position reference. It shifts the entire position-tracking trajectory bodily without changing the queued targets or [FIFOPosTrgt](FIFOPosTrgt.md). It is the position member of the three position-tracking offsets, alongside the velocity offset [FIFOPosVelOf](FIFOPosVelOf.md) and the current offset [FIFOPosCurrOf](FIFOPosCurrOf.md). It is not saved to flash and can be changed at any time, including during motion.

## How it works

On every sample, the interpolated target (the working target plus the interpolation toward the next target) is summed with `FIFOPosPosOf` to form the commanded position reference:

```text
position reference = interpolated target + FIFOPosPosOf
```

The sum is then clamped by the software position limits. Because the offset is applied after interpolation, changing it shifts the whole path uniformly; a step change produces a step in the reference, so change it gradually if the axis is tracking. The offset affects only the position reference and is independent of the velocity and current feedforward offsets.

A common use is to apply a live correction (for example from an external sensor or a master axis) on top of a fixed streamed profile.

When the axis enters position-tracking mode, `FIFOPosPosOf` is reset to 0 (along with [FIFOPosVelOf](FIFOPosVelOf.md) and [FIFOPosCurrOf](FIFOPosCurrOf.md)), so each run starts with no position offset. Set it again after the mode is entered if a non-zero shift is required.

## Examples

```text
AFIFOPosPosOf=5000   ; shift the whole position trajectory by 5000 counts
AFIFOPosPosOf=0      ; remove the offset
```

## See also

- [FIFOPosTrgt](FIFOPosTrgt.md) — working target position
- [FIFOPosVelOf](FIFOPosVelOf.md) — velocity feedforward offset
- [FIFOPosCurrOf](FIFOPosCurrOf.md) — current feedforward offset
- [PosRef](../01-kinematics-status/PosRef.md) — resulting position reference
