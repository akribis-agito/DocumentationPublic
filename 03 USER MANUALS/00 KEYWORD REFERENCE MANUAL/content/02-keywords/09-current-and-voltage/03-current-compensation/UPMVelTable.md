---
keyword: UPMVelTable
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 628
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 361
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -20000
  - 20000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# UPMVelTable

**Condition:**

UPMVelTable is only used when MotorType = 3 or 4 (brushless motor).

**Definition:**

UPMVelTable is the parameter array that provides commutation angle related motor current compensation (e.g. for cogging compensation application).

All array elements are 0 by default (no compensation). Each index will represent the respective commutation angle (ComtAng) by increment of 1 degree. For example, UPMVelTable\[54\] represents current compensation value when ComtAng = 54 degrees.

Please refer to [Control tuning – Current control](../../../02-keywords/11-control-tuning/06-current-control/00-overview.md) for its application point.
