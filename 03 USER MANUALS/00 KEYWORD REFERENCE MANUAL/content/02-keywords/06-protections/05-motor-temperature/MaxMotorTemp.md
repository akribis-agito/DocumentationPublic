---
keyword: MaxMotorTemp
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 399
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
  - 10
  - 150
  default: 80
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxMotorTemp

**Condition:**

MaxMotorTemp is only applicable for PT100 temperature sensors (MotorTempUsed == 1).

**Definition:**

MotorTempOffset defines an offset that is applied to MotorTemp. It is used to offset errors in temperature reading due to cable resistance.
