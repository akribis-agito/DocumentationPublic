---
keyword: HallsAngle
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

**Definition:**

HallsAngle is an array that stores the commutation angle associated with each Hall-sensor state transition. Each element maps one of the six valid Hall state combinations to the corresponding electrical angle used for FOC commutation. It is an axis-related array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[HallsValue](HallsValue.md), [HallsAngleSw](HallsAngleSw.md), [HallOnlyFilt](HallOnlyFilt.md)
