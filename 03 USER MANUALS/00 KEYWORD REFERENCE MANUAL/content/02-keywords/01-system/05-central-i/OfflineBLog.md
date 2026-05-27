---
keyword: OfflineBLog
summary: Receive buffer for Central-i offline log data from device port B.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 621
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
# OfflineBLog

Receive buffer for Central-i offline log data from device port B.

## Overview

`OfflineBLog` is a non-axis array that serves as the receive buffer for Central-i offline log data from device **port B**. It mirrors [OfflineALog](OfflineALog.md), which captures data from port A. The firmware populates the array when the offline log transaction completes, and the host reads it to inspect the captured device data.

## Examples

```text
AOfflineBLog[1]     ; read the first word of captured port-B log data
```

## See also

- [OfflineALog](OfflineALog.md) — port-A log buffer
- [CIOfflineData](CIOfflineData.md) / [CIOfflineSend](CIOfflineSend.md) — offline data exchange
