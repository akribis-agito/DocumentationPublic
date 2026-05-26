---
keyword: Vd
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 16
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Vd

**Condition:**

Vd is only applicable for three-phase motor (MotorType = 3 or 4). Otherwise, Vd is 0.

**Definition:**

Vd is the output of PI controller of the direct axis in dq0-domain current control, in terms of internal unit. Vd is 0 if abc-domain current control is used. Please refer to [ControlMode](../../../02-keywords/09-current-and-voltage/02-motor-variables/ControlMode.md) for more information.

For dq0-domain current control, Vd and Vq will form phase voltage commands (Va, Vb, Vc) by inverse Park transform.
