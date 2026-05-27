---
keyword: HallsAngle
summary: Array mapping each Hall-sensor state to the electrical angle used for commutation.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 384
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 7
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 360
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# HallsAngle

Array mapping each Hall-sensor state to the electrical angle used for commutation.

## Overview

`HallsAngle` is an array that stores the commutation angle associated with each Hall-sensor state. Each valid Hall state combination (the six legal states reported by [HallsValue](HallsValue.md)) is mapped to the corresponding electrical angle used for commutation. This table lets the controller derive the motor electrical angle directly from the Hall sensors. The raw angle can be smoothed with [HallOnlyFilt](HallOnlyFilt.md) when running in Hall-only commutation mode (selected via [ComtMode](ComtMode.md)), and the resulting angle is reported by [ComtAng](ComtAng.md). Being an array, axis-scope, and flash-saved, it cannot be changed while the motor is on or in motion (per-element range 0–360).

## Examples

```text
HallsAngle[1]?      ; query the angle mapped to the first Hall state
HallsAngle[1]=30    ; set the electrical angle (deg) for that Hall state
```

## See also

- [HallsValue](HallsValue.md) — current raw Hall sensor state (the index source)
- [HallsAngleSw](HallsAngleSw.md) — Hall-to-encoder commutation switch-over angle
- [HallOnlyFilt](HallOnlyFilt.md) — filter for the Hall-based commutation angle
- [ComtMode](ComtMode.md) — selects the commutation method
