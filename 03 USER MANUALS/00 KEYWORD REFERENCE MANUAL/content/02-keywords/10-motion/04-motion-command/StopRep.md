---
keyword: StopRep
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 148
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
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
# StopRep

**Definition:**

StopRep is a command that stops repetitive (repeat) motion initiated in the current motion mode. It decelerates the axis to rest and clears the repeat-motion state. It is an axis-related command function that can be issued during motion.

**See also:**

[Stop](Stop.md), [RptMode](../02-motion-configuration/RptMode.md), [RptCycles](../02-motion-configuration/RptCycles.md)
