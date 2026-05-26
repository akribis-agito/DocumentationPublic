---
keyword: ConFltSnapSrc
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 528
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
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
# ConFltSnapSrc

**Definition:**

ConFltSnapSrc is an array that configures which parameter values are captured (snapped) into ConFltSnapVal when a controller fault occurs. Each element specifies the CAN code of the parameter to record, allowing diagnostics data to be frozen at the moment of a fault. It is an axis-related array saved to flash.

**See also:**

[ConFltSnapVal](ConFltSnapVal.md), [ConFlt](ConFlt.md)
