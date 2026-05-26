---
keyword: StepInMotCurr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 255
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
  - 50
  - 64000
  default: 50
  scaling: 1.0
  implemented: final
overrides: {}
---
# StepInMotCurr

**Condition:**

This keyword is only used when MotorType = 6 or 7.

**Definition:**

StepInMotCurr is the phase current command (in milliampere) when stepper motor is in motion (stepping current).
