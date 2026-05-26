---
keyword: ForceInTTol
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 734
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 2147483647
  default: 10
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceInTTol

**Condition:**

This keyword is only applicable when [ForceCmdSrc](../../../02-keywords/08-axis-operation/04-force-operation-mode/ForceCmdSrc.md) = 1 or 2.

**Definition:**

ForceInTTol is the settling window around the target value (ForceCmdVal), in terms of units, used to determine in-target status of force control.
