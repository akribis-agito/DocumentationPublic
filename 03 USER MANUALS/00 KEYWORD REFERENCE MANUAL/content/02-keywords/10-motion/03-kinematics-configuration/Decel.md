---
keyword: Decel
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 137
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
# Decel

**Definition:**

Decel sets the deceleration rate for point-to-point motion in user units per second squared. It defines how quickly the axis ramps down from the commanded Speed to rest at the end of a move. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

**See also:**

[Accel](Accel.md), [Speed](Speed.md), [EmrgDec](EmrgDec.md)
