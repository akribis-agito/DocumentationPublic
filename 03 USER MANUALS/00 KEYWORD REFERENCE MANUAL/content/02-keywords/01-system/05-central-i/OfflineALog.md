---
keyword: OfflineALog
summary: Receive buffer for Central-i offline log data from device port A.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
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

Receive buffer for Central-i offline log data from device port A.

## Overview

`OfflineALog` is a non-axis array that serves as the receive buffer for Central-i offline log data from device **port A**. The firmware populates the array when the associated offline log transaction completes, and the host reads it to inspect the captured device data. The equivalent buffer for the second port is [OfflineBLog](OfflineBLog.md).

## Examples

```text
OfflineALog[1]?     ; read the first word of captured port-A log data
```

## See also

- [OfflineBLog](OfflineBLog.md) — port-B log buffer
- [CIOfflineData](CIOfflineData.md) / [CIOfflineSend](CIOfflineSend.md) — offline data exchange
