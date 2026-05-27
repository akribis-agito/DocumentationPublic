---
keyword: VecAccel
summary: Vector acceleration rate (user units/s^2) ramping the resultant velocity up to VecSpeed.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 636
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
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecAccel

Vector acceleration rate (user units/s^2) ramping the resultant velocity up to VecSpeed.

## Overview

`VecAccel` sets the acceleration rate for coordinated multi-axis vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16), in user units per second squared. It defines how quickly the resultant (vector) velocity ramps up toward [VecSpeed](VecSpeed.md), applying to the path as a whole rather than to any single axis. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

`VecAccel` governs the ramp-up; [VecDecel](VecDecel.md) governs the controlled ramp-down, and [VecJerk](VecJerk.md) optionally smooths the transitions into an S-curve.

## Examples

```text
VecAccel=100000     ; vector acceleration (user units/s^2, default)
VecAccel?           ; read the current value
```

## See also

- [VecDecel](VecDecel.md) — vector deceleration rate
- [VecSpeed](VecSpeed.md) — target resultant speed
- [VecJerk](VecJerk.md) — jerk limit for S-curve smoothing
