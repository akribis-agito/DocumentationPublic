---
keyword: PosErr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 18
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
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
# PosErr

**Definition:**

PosErr reports the error between position reference and feedback, only if the axis is enabled, in position operation mode, not in open-loop condition and the axis phasing is done. The unit is in terms of main user unit.

1.  Under individual (non-gantry) mode

$$
PosErr = PosRef - Pos
$$

2.  Under gantry mode

$$
PosErr = PosRef - GantryFdbk
$$

Otherwise, PosErr reports 0.

PosErr is generally used for position feedback control, motion protection, homing, operation mode switching, etc.
