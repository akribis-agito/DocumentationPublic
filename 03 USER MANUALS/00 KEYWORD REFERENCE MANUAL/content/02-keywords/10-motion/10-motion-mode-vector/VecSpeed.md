---
keyword: VecSpeed
summary: Maximum vector (resultant) speed in user units/s for coordinated multi-axis motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 635
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 10000
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecSpeed

Maximum vector (resultant) speed in user units/s for coordinated multi-axis motion.

## Overview

`VecSpeed` sets the maximum vector (resultant) speed for coordinated multi-axis vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16), in user units per second. The individual axis velocities are scaled so that the vector magnitude does not exceed this value, which is what keeps a multi-axis path moving at a controlled feed rate. The ramps to and from this speed are governed by [VecAccel](VecAccel.md) and [VecDecel](VecDecel.md). It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## Examples

```text
AVecSpeed=10000      ; maximum resultant speed (user units/s, default)
AVecSpeed           ; read the current value
```

## See also

- [VecAccel](VecAccel.md) — vector acceleration rate
- [VecDecel](VecDecel.md) — vector deceleration rate
- [VecJerk](VecJerk.md) — jerk limit for S-curve smoothing
