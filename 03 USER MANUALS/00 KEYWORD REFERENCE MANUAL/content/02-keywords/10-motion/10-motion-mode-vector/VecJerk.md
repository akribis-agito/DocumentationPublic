---
keyword: VecJerk
summary: Jerk limit (0-9) for vector motion, smoothing the resultant velocity into an S-curve.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 639
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
  - 9
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecJerk

Jerk limit (0-9) for vector motion, smoothing the resultant velocity into an S-curve.

## Overview

`VecJerk` sets the jerk limit for vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16), controlling the rate of change of the resultant acceleration to produce a smoother S-curve velocity profile. Higher smoothing reduces mechanical shock at the cost of slightly longer moves; it shapes the transitions between the [VecAccel](VecAccel.md) and [VecDecel](VecDecel.md) ramps. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

## Examples

```text
AVecJerk=0           ; no jerk limiting (trapezoidal profile, default)
AVecJerk=9           ; maximum S-curve smoothing
```

## See also

- [VecAccel](VecAccel.md) — vector acceleration rate
- [VecDecel](VecDecel.md) — vector deceleration rate
- [VecSpeed](VecSpeed.md) — target resultant speed
