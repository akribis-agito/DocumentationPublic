---
keyword: StepInPosCurr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 254
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 32000
  default: 50
  scaling: 1.0
  implemented: final
overrides: {}
---
# StepInPosCurr

**Condition:**

This keyword is only used when MotorType = 6 or 7.

**Definition:**

StepInPosCurr is the phase current command (in milliampere) when stepper motor is in standstill (holding current).
