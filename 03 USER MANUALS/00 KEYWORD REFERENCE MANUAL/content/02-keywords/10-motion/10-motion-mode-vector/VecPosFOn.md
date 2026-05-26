---
keyword: VecPosFOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 648
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecPosFOn

**Definition:**

VecPosFOn enables the position filter on the vector motion reference output. When set to a non-zero value, the filter defined by VecPosFDef is applied to smooth the vector position reference before it reaches the individual axis servo loops. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

**See also:**

[VecPosFDef](VecPosFDef.md), [VecSpeed](VecSpeed.md)
