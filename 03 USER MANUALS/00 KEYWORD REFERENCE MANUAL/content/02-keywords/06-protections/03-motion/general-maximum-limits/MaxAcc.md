---
keyword: MaxAcc
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 81
attributes:
  access: '0'
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# MaxAcc

**Definition:**

MaxAcc defines the maximum allowable acceleration/deceleration checked before a motion is started. If acceleration or deceleration exceeds the limit, command error is reported and recorded in ErrLog.
