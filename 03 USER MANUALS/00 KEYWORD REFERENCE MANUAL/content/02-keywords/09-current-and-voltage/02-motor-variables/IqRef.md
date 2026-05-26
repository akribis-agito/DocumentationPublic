---
keyword: IqRef
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 30
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# IqRef

**Definition:**

IqRef definition varies according to MotorType.

| Motor type | Descriptions |
|----|----|
| Single-phase motor (MotorType = 1 or 2) | IqRef equals to IaRef. |
| Three-phase motor (MotorType = 3 or 4) | IqRef equals to CurrRefCtrl after direction correction. It is used in dq0-domain current control. |
| Two-phase stepper motor (MotorType = 6 or 7) | Iq equals to 0. |
