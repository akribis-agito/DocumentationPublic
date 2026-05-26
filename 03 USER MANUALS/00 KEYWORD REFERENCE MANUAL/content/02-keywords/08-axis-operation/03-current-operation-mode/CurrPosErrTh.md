---
keyword: CurrPosErrTh
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 337
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -327680
  - 327680
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrPosErrTh

**Condition:**

It is used only while axis is in position operation mode (OperationMode = 3).

**Definition:**

CurrPosErrTh is the threshold position error (PosErr) value used in the second condition check to enter current operation mode.

| Value | Descriptions                                             |
|-------|----------------------------------------------------------|
| \< 0  | Second condition is fulfilled if PosErr \< CurrPosErrTh. |
| 0     | Second condition is not fulfilled.                       |
| \> 0  | Second condition is fulfilled if PosErr \> CurrPosErrTh. |

**Note:**

Entry into current operation mode still subjects to the first condition check. If the first and second conditions are fulfilled, axis enters current operation mode and CurrPosErrTh is cleared to 0 to avoid undesired future switching. User needs to reconfigure its value for next switch. See Current operation mode for the overview.
