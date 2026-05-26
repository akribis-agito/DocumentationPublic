---
keyword: CIOfflineDef
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 507
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
# CIOfflineDef

**Definition:**

CIOfflineDef is an axis-related array that defines which parameters are included in the Central-i offline dataset — i.e., which values will be sent when [CIOfflineSend](CIOfflineSend.md) is executed. The definition is saved to flash.

**See also:**

[CIOfflineData](CIOfflineData.md), [CIOfflineSend](CIOfflineSend.md)
