---
keyword: UserParam
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 624
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 251
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
# UserParam

**Definition:**

UserParam is an axis-related general-purpose integer array that provides per-axis storage accessible by the user program and host. It can be read and written at any time and is saved to flash.

**See also:**

[UserParamD](UserParamD.md), [UserParamF](UserParamF.md), [UserParamLL](UserParamLL.md), [GenData](GenData.md)
