---
keyword: VecNumCircles
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 646
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 100
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecNumCircles

**Definition:**

VecNumCircles sets the number of complete circular arcs to execute in vector arc motion mode. Setting it to zero causes the arc to run indefinitely until a StopVec command is issued. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

**See also:**

[VecSpeed](VecSpeed.md), [StopVec](StopVec.md)
