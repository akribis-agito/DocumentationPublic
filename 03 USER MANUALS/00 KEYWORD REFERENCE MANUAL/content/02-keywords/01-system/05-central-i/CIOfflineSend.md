---
keyword: CIOfflineSend
availability:
  standalone:
  - v4
  central-i: []
can_code: 502
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CIOfflineSend

**Definition:**

CIOfflineSend is a command that transmits the offline data package (defined by [CIOfflineDef](CIOfflineDef.md) and populated in [CIOfflineData](CIOfflineData.md)) to the Central-i device on the selected axis port. It is used to pre-load or simulate device data when a live connection is not available.

**See also:**

[CIOfflineData](CIOfflineData.md), [CIOfflineDef](CIOfflineDef.md), [CIConnect](CIConnect.md)
