---
keyword: OfflineBLog
summary: Rolling log of Central-i offline (mailbox) messages on channel B, the host channel used by CIOfflineSend.
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

Rolling log of Central-i offline messages sent on offline mailbox B (the host channel used by CIOfflineSend).

## Overview

`OfflineBLog` is a non-axis array that records the most recent Central-i **offline** (mailbox) transactions on **offline channel B** — the second offline mailbox, which is the host channel driven by [CIOfflineSend](CIOfflineSend.md). Every [CIOfflineSend](CIOfflineSend.md) transaction (the request and its reply) is logged here, so the host can review what was sent and what the remote returned. It mirrors [OfflineALog](OfflineALog.md), which logs the firmware-driven channel A.

## How it works

The buffer has the same shape as [OfflineALog](OfflineALog.md): up to **5 messages of 9 fields** each (45 used elements; index `[0]` is unused). A write index advances per message, overwriting the oldest entry. The nine fields per message slot are:

| Offset in slot | Field | Meaning |
|----------------|-------|---------|
| +1 | Sender | What issued the message — for this log, the host function ([CIOfflineSend](CIOfflineSend.md)) |
| +2 | Message type | `0` = query, `1` = assignment |
| +3 | Opcode | Remote register address read or written |
| +4 | Value out | Value sent (for an assignment) |
| +5 | Value in | Value returned (for a query) |
| +6 | Acknowledge / error | `0` = ok, otherwise the remote's error code |
| +7 | Time | Controller time when the message was sent (cf. [Time](../03-timing/Time.md)) |
| +8 | Sample counter | Sample counter at send time |
| +9 | Port | Axis/port number the message went to |

Message *k* (k = 0…4) occupies elements `[9k+1]` … `[9k+9]`.

## Examples

```text
AOfflineBLog[3]     ; opcode of the first logged CIOfflineSend message
AOfflineBLog[5]     ; value returned by the remote for that message
AOfflineBLog[6]     ; its acknowledge/error code (0 = ok)
```

## See also

- [OfflineALog](OfflineALog.md) — log for offline mailbox A (the firmware channel)
- [CIOfflineSend](CIOfflineSend.md) — the command whose transactions are logged here
- [CIOfflineData](CIOfflineData.md) — request/response buffer for each transaction
