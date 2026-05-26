---
keyword: Abort
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 133
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Abort

**Definition:**

Abort is a command that immediately stops axis motion using the emergency deceleration rate (EmrgDec), halting the move as quickly as possible. It can be issued at any time during motion and is typically used for safety or fault recovery. It is an axis-related command function.

**See also:**

[Stop](Stop.md), [EmrgDec](../03-kinematics-configuration/EmrgDec.md)
