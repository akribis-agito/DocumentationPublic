---
keyword: CurrKi
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 105
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
  - 200000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# CurrKi

**Definition:**

CurrKi is the integral gain of current loop control, acting on the integral of current error.
