---
keyword: FwdPLim
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 83
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 2000000000
  scaling: 1.0
  implemented: final
overrides: {}
---
# FwdPLim

**Definition:**

FwdPLim specifies forward software travel limit, in units of count.

Upper limit of reference position will be capped at FwdPLim. As a result, motion stops at FwdPLim if reference position is higher than this limit. Any positive/forward motion with final target position above FwdPLim is disallowed.
