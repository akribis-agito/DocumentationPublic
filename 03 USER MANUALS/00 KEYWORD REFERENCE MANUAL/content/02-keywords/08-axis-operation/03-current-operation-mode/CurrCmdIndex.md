---
keyword: CurrCmdIndex
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 333
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
  - 1
  - 20
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrCmdIndex

**Condition:**

This keyword is only applicable when CurrCmdSrc = 1 or 2.

**Definition:**

CurrCmdIndex is the index of existing CurrCmdVal and CurrCmdHTime values in use.

CurrCmdIndex will reset to 1 only

1.  upon receipt of GoToCurrMode command,

2.  upon automatic condition switching, or

3.  upon digital input for switching to current operation mode.

This means if OperationMode is directly assigned, user can configure it to any initial value so that the reference table starts from desired CurrCmdVal and CurrCmdHTime pair.

%%
Note DN: User can overwrite CurrCmdIndex at any time under current operation mode. This will cause sudden switch of CurrCmdVal in use, without reset of CurrCmdCntr timer.
%%
