---
keyword: ForceRefFilt
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 586
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
  - 1
  - 500000
  default: 10000
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceRefFilt

**Definition:**

ForceRefFilt defines the first-order low-pass filter cut-off frequency of force command, in terms of Hz/100. The filtered result is represented as ForceRef.

For example, if the cut-off frequency is 500Hz, then ForceRefFilt = 50000.
