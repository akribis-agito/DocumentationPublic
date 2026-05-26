---
keyword: ECAMMaster
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 309
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ECAMMaster

**Definition:**

ECAMMaster is the [complex CAN code](../../../01-keyword-usage-and-syntax/complex-can-code.md) (CCC) used to define the source of the master variable. It is an array of size 10, where each element corresponds to a cam pattern.
