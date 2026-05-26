---
keyword: CurrCurrTh
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 339
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
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrCurrTh

**Condition:**

It is used only while axis is in velocity or position operation mode (OperationMode = 2 or 3).

**Definition:**

CurrCurrTh is the threshold current reference (CurrRef) value used in the second condition check to enter current operation mode. If the value is 0, axis will not switch operation mode.

Otherwise, the switching depends on direction keyword (CurrCurrThDir).

| CurrCurrThDir | Descriptions                                            |
|---------------|---------------------------------------------------------|
| 0             | Second condition is fulfilled if CurrRef \> CurrCurrTh. |
| 1             | Second condition is fulfilled if CurrRef \< CurrCurrTh. |

**Note:**

Entry into current operation mode still subjects to the first condition check. If the first and second conditions are fulfilled, axis enters current operation mode and CurrCurrTh is cleared to 0 to avoid undesired future switching. User needs to reconfigure its value for next switch. See Current operation mode for the overview.
