---
keyword: CurrPosTh
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 426
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrPosTh

**Condition:**

It is used only while axis is in velocity or position operation mode (OperationMode = 2 or 3).

**Definition:**

CurrPosTh is the threshold position reference (PosRef) value used in the first condition check to enter current operation mode.

The switching depends on direction keyword (CurrPosThDir).

| CurrPosThDir | Descriptions                                         |
|--------------|------------------------------------------------------|
| \< 0         | First condition is fulfilled if PosRef \< CurrPosTh. |
| 0            | First condition is fulfilled.                        |
| \> 0         | First condition is fulfilled if PosRef \> CurrPosTh. |

**Note:**

Entry into current operation mode still subjects to the second condition check. If the first and second conditions are fulfilled, axis enters current operation mode and CurrPosTh is cleared to 0 to avoid undesired future switching. User needs to reconfigure its value for next switch. See Current operation mode for the overview.
