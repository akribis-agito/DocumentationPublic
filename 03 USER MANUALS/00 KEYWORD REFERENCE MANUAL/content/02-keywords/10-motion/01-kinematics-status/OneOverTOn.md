---
keyword: OneOverTOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 187
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# OneOverTOn

**Condition:**

OneOverTOn is applicable when digital incremental encoder (EncType = 1) is used.

**Definition:**

OneOverTOn is used to enable (OneOverTOn = 1) or disable (OneOverTOn = 0) the 1/T velocity measurement. Vel\[4\] reports 0 if 1/T velocity measurement is disabled.

Please refer to the [Vel](../../../02-keywords/10-motion/01-kinematics-status/Vel.md) keyword for more information.
