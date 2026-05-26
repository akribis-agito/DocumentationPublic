---
keyword: MaxMotorCurr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 99
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
  - 76000
  default: 76000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxMotorCurr

**Definition:**

MaxMotorCurr defines the maximum allowable motor current ([MotorCurr](../../../02-keywords/09-current-and-voltage/02-motor-variables/MotorCurr.md)) in mA. If absolute value of MotorCurr exceeds MaxMotorCurr for more than 0.25ms, axis is disabled, and an error code is thrown to ConFlt.

**Note:**

For three-phase motor, MotorCurr is equal to amplitude of motor current phasor.
