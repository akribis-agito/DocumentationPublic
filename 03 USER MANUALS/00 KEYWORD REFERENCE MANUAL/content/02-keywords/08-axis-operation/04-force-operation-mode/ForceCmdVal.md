---
keyword: ForceCmdVal
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 571
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceCmdVal

**Condition:**

This keyword is only applicable when [ForceCmdSrc](../../../02-keywords/08-axis-operation/04-force-operation-mode/ForceCmdSrc.md) = 1 or 2.

**Definition:**

ForceCmdVal defines a sequence of user-defined force references to be used, in terms of units. It is used in pair with holding time (ForceCmdHTime).
