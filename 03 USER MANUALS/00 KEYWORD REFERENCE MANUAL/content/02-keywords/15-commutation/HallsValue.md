---
keyword: HallsValue
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 383
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 6
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HallsValue

**Definition:**

HallsValue is a read-only parameter that reports the current raw Hall sensor state as a 3-bit value (bits CBA). The three Hall input signals from the motor are combined into this integer to indicate the current electrical sector for commutation. It is an axis-related, read-only parameter that is not saved to flash.

**See also:**

[HallsAngle](HallsAngle.md), [HallOnlyFilt](HallOnlyFilt.md), [ComtMode](ComtMode.md)
