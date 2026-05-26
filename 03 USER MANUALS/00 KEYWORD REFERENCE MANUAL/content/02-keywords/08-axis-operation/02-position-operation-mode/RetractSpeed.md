---
keyword: RetractSpeed
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 608
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -1300000000
  - 1300000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
---
# RetractSpeed

**Definition:**

RetractSpeed is the maximum velocity used in the point-to-point motion upon entry to position operation mode, subject to BeginOnToPos flag.
