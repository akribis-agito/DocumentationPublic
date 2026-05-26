---
keyword: CurrLimFwd
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 393
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 64000
  default: 64000
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrLimFwd

**Condition:**

It is only used if CurrLimMode=3.

**Definition:**

CurrLimFwd defines the positive current command limit, overwriting the default PeakCL limitation. The value should be positive.
