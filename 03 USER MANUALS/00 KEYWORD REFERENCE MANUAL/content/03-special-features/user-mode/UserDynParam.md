---
keyword: UserDynParam
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 371
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 51
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# UserDynParam

**Definition:**

UserDynParam is a general-purpose data array used by special user-defined processing modes. Each element holds a value that the active user-mode algorithm reads or writes at runtime (for example, captured positions or sensor data). The array provides 50 elements, indexed [1] through [50]. It cannot be changed while the axis is in motion or with the motor on. It is a non-axis array parameter and is not saved to flash.

**See also:**

[GenData](../../02-keywords/20-arrays/GenData.md), [UserParam](../../02-keywords/20-arrays/UserParam.md)
