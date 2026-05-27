---
keyword: Accel
summary: Acceleration rate for point-to-point motion, in user units per second squared.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 136
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
# Accel

Acceleration rate for point-to-point motion, in user units per second squared.

## Overview

`Accel` defines how quickly the axis ramps up from rest toward the commanded [Speed](Speed.md) at the start of a move. It is one of the core kinematic limits the motion profiler stays within when generating a profile. The deceleration side is set separately by [Decel](Decel.md), the effective acceleration can be scaled by [AccelFact](AccelFact.md), and the smoothness of the acceleration transition is governed by [Jerk](Jerk.md). It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## Examples

```text
Accel=200000        ; acceleration (user units/s^2)
Accel?              ; query current acceleration
```

## See also

- [Decel](Decel.md) — deceleration rate for the end of a move
- [Speed](Speed.md) — target velocity that acceleration ramps toward
- [Jerk](Jerk.md) — rate of change of acceleration (S-curve smoothing)
- [AccelFact](AccelFact.md) — scaling factor applied to `Accel`
