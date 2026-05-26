---
keyword: ForceInTStat
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 735
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 4
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceInTStat

**Condition:**

This keyword is only applicable when [ForceCmdSrc](../../../02-keywords/08-axis-operation/04-force-operation-mode/ForceCmdSrc.md) = 1 or 2.

**Definition:**

ForceInTStat refers to status of force control when user-defined force reference array is defined, as shown.

| ForceInTStat | Descriptions |
|----|----|
| 0 | Motor is disabled. |
| 1 | Motor is enabled. |
| 2 | Force reference is changing/ramping to the target value (ForceCmdVal). |
| 3 | Force reference has reached the target value while force feedback is settling to within ForceInTTol window around the target value for at least ForceInTTime. |
| 4 | Force feedback has settled to within ForceInTTol of the target value for at least ForceInTTime. |
