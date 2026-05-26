---
keyword: ForceCmdSrc
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 570
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
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceCmdSrc

**Definition:**

ForceCmdSrc is used to set the source of force reference (ForceRef), as shown below.

| Value | Source |
|----|----|
| 0 | Analog force reference input (defined by [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md)) |
| 1 or 2 | User defined values (ForceCmdVal), each with specific timing (ForceCmdHTime) |
