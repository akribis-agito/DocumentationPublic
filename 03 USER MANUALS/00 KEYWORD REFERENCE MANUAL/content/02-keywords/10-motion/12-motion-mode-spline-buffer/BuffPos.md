---
keyword: BuffPos
summary: Array of waypoint positions (user units) that define the spline buffer trajectory.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 543
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 10001
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BuffPos

Array of waypoint positions (user units) that define the spline buffer trajectory.

## Overview

`BuffPos` stores the waypoint positions, in user units, for the spline buffer motion profile. Together with the per-segment durations in [BuffTime](BuffTime.md), it defines the trajectory: the controller fits a spline through these waypoints and executes a smooth motion between them. The waypoints are turned into spline coefficients by [BuffCalc](BuffCalc.md) before motion begins. It is not saved to flash and can be changed at any time.

## Examples

```text
BuffPos[1]=0        ; first waypoint position (user units)
BuffPos[2]=10000    ; second waypoint position
```

## See also

- [BuffTime](BuffTime.md) — per-segment durations paired with these waypoints
- [BuffCalc](BuffCalc.md) — pre-compute the spline coefficients
- [BuffSplineMod](BuffSplineMod.md) — spline interpolation mode
