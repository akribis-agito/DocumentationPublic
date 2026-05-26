---
keyword: OfflineALog
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 620
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 46
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
# OfflineALog

**Definition:**

OfflineALog is a non-axis array that serves as the receive buffer for Central-i offline log data from device port A. The firmware populates this array when the associated offline log transaction completes, and the host can read it to inspect captured device data.

**See also:**

[OfflineBLog](OfflineBLog.md), [CIOfflineData](CIOfflineData.md), [CIOfflineSend](CIOfflineSend.md)
