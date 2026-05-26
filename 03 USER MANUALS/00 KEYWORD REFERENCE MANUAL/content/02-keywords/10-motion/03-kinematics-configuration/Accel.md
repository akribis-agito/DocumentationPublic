---
keyword: Accel
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

**Definition:**

Accel sets the acceleration rate for point-to-point motion in user units per second squared. It defines how quickly the axis ramps up from rest to the commanded Speed. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

**See also:**

[Decel](Decel.md), [Speed](Speed.md), [Jerk](Jerk.md), [AccelFact](AccelFact.md)
