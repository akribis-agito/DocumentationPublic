---
keyword: Begin
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 131
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Begin

**Definition:**

Begin is a command that starts motion on the axis according to the current motion mode and target settings. The axis must not already be in motion when Begin is issued. It is an axis-related command function.

**See also:**

[Abort](Abort.md), [Stop](Stop.md), [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md), [RelTrgt](../13-motion-mode-ptp/RelTrgt.md)
