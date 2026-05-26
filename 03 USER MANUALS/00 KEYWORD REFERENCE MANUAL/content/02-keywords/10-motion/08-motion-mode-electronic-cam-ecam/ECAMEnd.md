---
keyword: ECAMEnd
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 303
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
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
---
# ECAMEnd

**Definition:**

ECAMEnd defines the GenData index where the cam pattern ends. It is an array of size 10, where each element corresponds to a cam pattern.

ECAMEnd must match the following order where the overall cam pattern is derived.

$$
ECAMStart \leq ECAMStartCyc < ECAMEndCyc \leq ECAMEnd
$$
