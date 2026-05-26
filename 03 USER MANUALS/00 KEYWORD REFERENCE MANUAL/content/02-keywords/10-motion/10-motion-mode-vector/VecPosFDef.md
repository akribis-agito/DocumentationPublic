---
keyword: VecPosFDef
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 647
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecPosFDef

**Definition:**

VecPosFDef is an array that defines the position filter configuration applied to the vector motion reference output. It specifies the filter coefficients or parameters used to smooth the vector position reference before it is fed to the individual axis servo loops. It is an axis-related array saved to flash, and cannot be changed while the axis is in motion.

**See also:**

[VecPosFOn](VecPosFOn.md), [VecSpeed](VecSpeed.md)
