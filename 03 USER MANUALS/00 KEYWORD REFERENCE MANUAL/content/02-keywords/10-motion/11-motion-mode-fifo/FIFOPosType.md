---
keyword: FIFOPosType
summary: Selects the operating mode of the FIFO position-tracking feature.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 659
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPosType

Selects the operating mode of the FIFO position-tracking feature.

## Overview

`FIFOPosType` selects how the position points streamed through the FIFO position-tracking queue are interpolated between successive cycles. It is the interpolation-mode setting for the position-tracking subsystem, which is enabled by [FIFOPosFIFOEn](FIFOPosFIFOEn.md) and fed by [FIFOPosPush](FIFOPosPush.md).

Unlike the main FIFO motion mode (see [FIFOType](FIFOType.md)), which builds a trajectory from velocity-type and acceleration-type *segments*, position tracking streams a series of absolute **position targets**. The controller takes one new target per cycle and produces the motion reference by interpolating between consecutive targets. `FIFOPosType` chooses the interpolation rule used for that fill-in.

It is saved to flash and cannot be changed while the axis is in motion.

## How it works

A new position target is taken from the queue at the first sample of every cycle (the cycle length, in servo samples, is set by [FIFOPosCycle](FIFOPosCycle.md)). Between cycles, the position reference is computed from the surrounding targets according to the selected mode:

| Value | Mode | Behavior |
|-------|------|----------|
| 0 | Linear interpolation (default) | The reference moves in a straight line between the target at the start of the current cycle and the target at its end. Two targets are needed. |
| 1 | Cubic-spline interpolation | The reference follows a smooth cubic curve fitted through four consecutive targets (the previous start, the current start, the current end, and the next end). This produces continuous velocity across cycle boundaries at the cost of one extra cycle of look-ahead latency. |

In both modes the interpolated reference is shifted by [FIFOPosPosOf](FIFOPosPosOf.md) before it is used, and the resulting reference is still clamped by the software position limits.

When the axis enters position-tracking mode, the working target and all internal control points are initialized to the current position reference, so tracking starts smoothly from where the axis already is.

## Examples

```text
AFIFOPosType=0       ; linear interpolation between targets
AFIFOPosType=1       ; smooth cubic-spline interpolation
```

## See also

- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — enable FIFO position tracking
- [FIFOPosPush](FIFOPosPush.md) — push a position target
- [FIFOPosCycle](FIFOPosCycle.md) — samples per target (cycle length)
- [FIFOPosStatus](FIFOPosStatus.md) — position-tracking queue status
- [FIFOType](FIFOType.md) — the main (segment-based) FIFO motion mode
