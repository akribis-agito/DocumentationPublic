---
keyword: CIOfflineData
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 501
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
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
# CIOfflineData

**Definition:**

CIOfflineData is an axis-related array that holds the data payload to be transmitted during a Central-i offline (simulation) transaction. The values are loaded before [CIOfflineSend](CIOfflineSend.md) is called, and are saved to flash so the same offline dataset can be replayed after reset.

**See also:**

[CIOfflineDef](CIOfflineDef.md), [CIOfflineSend](CIOfflineSend.md)
