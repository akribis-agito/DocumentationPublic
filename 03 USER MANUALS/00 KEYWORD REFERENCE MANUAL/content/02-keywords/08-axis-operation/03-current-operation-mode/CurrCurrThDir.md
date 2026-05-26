---
keyword: CurrCurrThDir
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 343
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
# CurrCurrThDir

**Condition:**

It is used only while axis is in velocity or position operation mode (OperationMode = 2 or 3).

**Definition:**

CurrCurrThDir defines the trigger direction for the second condition check (CurrRef) to enter current operation mode.

See [CurrCurrTh](../../../02-keywords/08-axis-operation/03-current-operation-mode/CurrCurrTh.md) and [Current operation mode](../../../02-keywords/08-axis-operation/03-current-operation-mode/00-overview.md) for more information.
