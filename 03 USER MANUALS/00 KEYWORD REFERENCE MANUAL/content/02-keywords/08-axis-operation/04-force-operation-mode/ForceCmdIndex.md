---
keyword: ForceCmdIndex
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 573
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
# ForceCmdIndex

**Condition:**

This keyword is only applicable when ForceCmdSrc = 1 or 2.

**Definition:**

ForceCmdIndex is the index of existing ForceCmdVal and ForceCmdHTime values in use.

ForceCmdIndex will reset to 1 only

1.  upon receipt of GoToForceMode command,

2.  upon automatic condition switching, or

3.  upon digital input for switching to force operation mode.

This means if OperationMode is directly assigned, user can configure it to any initial value so that the reference table starts from desired ForceCmdVal and ForceCmdHTime pair.

%%
Note DN: User can overwrite ForceCmdIndex at any time under force operation mode. This will cause sudden switch of ForceCmdVal in use, without reset of ForceCmdCntr timer.
%%
