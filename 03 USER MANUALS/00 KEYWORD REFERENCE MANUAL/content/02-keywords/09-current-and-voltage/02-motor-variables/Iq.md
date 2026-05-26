---
keyword: Iq
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 12
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Iq

**Definition:**

Iq definition varies according to MotorType.

| Motor type | Descriptions |
|----|----|
| Single-phase motor (MotorType = 1 or 2) | Iq equals to Ia. |
| Three-phase motor (MotorType = 3 or 4) | Iq is the feedback current after Park transform in the quadrature axis, in milliamperes. |
| Two-phase stepper motor (MotorType = 6 or 7) | Iq equals to 0. |
