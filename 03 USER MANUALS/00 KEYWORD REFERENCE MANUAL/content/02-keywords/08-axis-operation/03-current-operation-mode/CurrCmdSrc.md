---
keyword: CurrCmdSrc
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 330
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
# CurrCmdSrc

**Definition:**

Under current operation mode, CurrCmdSrc is used to set the source of current command, as shown below.

| Value | Source |
|----|----|
| 0 | Analog current command input (defined by [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md)) |
| 1 or 2 | User defined values (CurrCmdVal), each with specific timing (CurrCmdHTime) |
| 3 | Master axis current command (axis defined by [CurrRefMaster](../../../02-keywords/08-axis-operation/03-current-operation-mode/CurrRefMaster.md)\] |
