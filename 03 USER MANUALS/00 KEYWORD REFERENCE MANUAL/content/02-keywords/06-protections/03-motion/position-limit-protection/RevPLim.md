---
keyword: RevPLim
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 82
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
  default: -2000000000
  scaling: 1.0
  implemented: final
overrides: {}
---
# RevPLim

**Definition:**

RevPLim specifies reverse software travel limit, in unit of count.

Lower limit of reference position will be capped at RevPLim. As a result, motion stops at RevPLim if reference position is lower than this limit. Any negative/reverse motion with final target position above RevPLim is disallowed.
