---
keyword: ECAMStartCyc
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 301
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
  - 1000
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ECAMStartCyc

**Definition:**

ECAMStartCyc defines the GenData index where the cyclical/repeating cam pattern starts. It is an array of size 10, where each element corresponds to a cam pattern.

ECAMStartCyc must match the following order where the overall cam pattern is derived.

$$
ECAMStart \leq ECAMStartCyc < ECAMEndCyc \leq ECAMEnd
$$
