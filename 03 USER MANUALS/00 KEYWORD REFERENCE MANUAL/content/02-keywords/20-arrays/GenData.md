---
keyword: GenData
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 237
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 1001
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GenData

**Definition:**

GenData is a general-purpose integer array that provides shared storage accessible by both the user program and the host. It can be read and written at any time, is not axis-related, and is saved to flash.

**See also:**

[GenDataD](GenDataD.md), [GenDataF](GenDataF.md), [GenDataLL](GenDataLL.md), [UserParam](UserParam.md)
