---
keyword: CurrPosThDir
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 427
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrPosThDir

**Condition:**

It is used only while axis is in velocity or position operation mode (OperationMode = 2 or 3).

**Definition:**

CurrPosThDir defines the trigger direction for the first condition check to enter current operation mode.

See [CurrPosTh](../../../02-keywords/08-axis-operation/03-current-operation-mode/CurrPosTh.md) and [Current operation mode](../../../02-keywords/08-axis-operation/03-current-operation-mode/00-overview.md) for more information.
