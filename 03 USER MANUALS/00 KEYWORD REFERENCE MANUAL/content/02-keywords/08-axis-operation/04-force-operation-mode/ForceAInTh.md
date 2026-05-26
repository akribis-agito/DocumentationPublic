---
keyword: ForceAInTh
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 584
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
  - -100000
  - 100000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceAInTh

**Condition:**

It is used only while axis is in velocity or position operation mode (OperationMode = 2 or 3).

**Definition:**

ForceAInTh is the threshold analog force feedback value used in the second condition check to enter force operation mode.

| Value | Descriptions |
|----|----|
| \< 0 | Second condition is fulfilled if analog force feedback \< ForceAInTh. |
| 0 | Second condition is not fulfilled. |
| \> 0 | Second condition is fulfilled if analog force feedback \> ForceAInTh. |

**Note:**

Entry into force operation mode still subjects to the first condition check. If the first and second conditions are fulfilled, axis enters force operation mode and ForceAInTh is cleared to 0 to avoid undesired future switching. User needs to reconfigure its value for next switch. See Force operation mode for the overview.
