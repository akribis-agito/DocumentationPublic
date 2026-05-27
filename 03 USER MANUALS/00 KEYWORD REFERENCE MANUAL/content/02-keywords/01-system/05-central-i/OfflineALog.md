---
keyword: OfflineALog
summary: Receive buffer for Central-i offline log data from device port A.
availability:
  standalone:
  - v4
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

Rolling log of Central-i offline messages sent on offline mailbox A (the firmware-driven channel).

## Overview

`OfflineALog` is a non-axis array that records the most recent Central-i **offline** (mailbox) transactions on **offline channel A** — the first offline mailbox, which the firmware uses for its own traffic (during [CIConnect](CIConnect.md), and from the control interrupt and background). The host reads it to inspect what offline messages were exchanged and their results. The companion log for the second mailbox — the host channel used by [CIOfflineSend](CIOfflineSend.md) — is [OfflineBLog](OfflineBLog.md).

## How it works

The buffer holds up to **5 messages of 9 fields** each (45 used elements; index `[0]` is unused so logging starts at `[1]`). Each new message advances a write index, overwriting the oldest entry in turn. Within each message slot the nine fields are, in order:

| Offset in slot | Field | Meaning |
|----------------|-------|---------|
| +1 | Sender | What issued the message (interrupt / host function / background / special) |
| +2 | Message type | `0` = query, `1` = assignment |
| +3 | Opcode | Remote register address read or written |
| +4 | Value out | Value sent (for an assignment) |
| +5 | Value in | Value returned (for a query) |
| +6 | Acknowledge / error | `0` = ok, otherwise the remote's error code |
| +7 | Time | Controller time when the message was sent (cf. [Time](../03-timing/Time.md)) |
| +8 | Sample counter | Sample counter at send time |
| +9 | Port | Axis/port number the message went to |

So message *k* (k = 0…4) occupies elements `[9k+1]` … `[9k+9]`. The same field layout is used for [OfflineBLog](OfflineBLog.md).

## Examples

```text
AOfflineALog[3]     ; opcode of the first logged message
AOfflineALog[6]     ; its acknowledge/error code (0 = ok)
AOfflineALog[12]    ; opcode of the second logged message ([9*1+3])
```

## See also

- [OfflineBLog](OfflineBLog.md) — log for offline mailbox B (the host channel)
- [CIOfflineData](CIOfflineData.md) / [CIOfflineSend](CIOfflineSend.md) — offline transactions
- [CIStatus](CIStatus.md) — offline error counters and last-error code
