---
keyword: IqErr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 23
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
# IqErr

**Definition:**

IqErr definition varies according to MotorType.

| Motor type | Descriptions |
|---|---|
| Single-phase motor (MotorType = 1 or 2) | IqErr equals to IaErr. |
| Three-phase motor (MotorType = 3 or 4) | IqErr is the calculated current error in the quadrature axis, in milliamperes, defined as shown. *I**q**E**r**r* [*m**A*] = *I**q**R**e**f* [*m**A*] − *I**q* [*m**A*] It is used in the dq0-domain current control. |
| Two-phase stepper motor (MotorType = 6 or 7) | Iq equals to 0. |
