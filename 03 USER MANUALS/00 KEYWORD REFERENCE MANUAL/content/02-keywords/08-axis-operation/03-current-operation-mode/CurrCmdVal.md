---
keyword: CurrCmdVal
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 331
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
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
# CurrCmdVal

**Condition:**

This keyword is only applicable when CurrCmdSrc = 1 or 2.

**Definition:**

CurrCmdVal defines a sequence of user-defined current references to be used, in milliamperes. It is used in pair with holding time (CurrCmdHTime).
