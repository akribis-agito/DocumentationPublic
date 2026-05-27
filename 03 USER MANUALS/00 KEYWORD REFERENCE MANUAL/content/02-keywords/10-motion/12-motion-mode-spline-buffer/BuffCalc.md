---
keyword: BuffCalc
summary: Command that pre-computes the spline coefficients from the buffer waypoints.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 547
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BuffCalc

Command that pre-computes the spline coefficients from the buffer waypoints.

## Overview

`BuffCalc` pre-computes the spline coefficients from the waypoint data in [BuffPos](BuffPos.md) and [BuffTime](BuffTime.md) before motion begins. It must be called after the waypoint arrays are loaded and before a `Begin` command is issued in spline buffer mode, so the controller has a ready trajectory to execute. The interpolation mode used is set by [BuffSplineMod](BuffSplineMod.md) and the edge conditions by [BuffEdgeMode](BuffEdgeMode.md). It cannot be issued while the axis is in motion.

## Examples

```text
ABuffCalc=0          ; compute spline coefficients from BuffPos and BuffTime
```

## See also

- [BuffPos](BuffPos.md) — waypoint positions
- [BuffTime](BuffTime.md) — per-segment durations
- [BuffSplineMod](BuffSplineMod.md) — spline interpolation mode
- [BuffStatus](BuffStatus.md) — spline buffer status
