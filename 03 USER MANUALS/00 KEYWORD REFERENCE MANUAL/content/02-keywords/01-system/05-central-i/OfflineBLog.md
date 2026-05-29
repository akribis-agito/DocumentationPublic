---
keyword: OfflineBLog
summary: Rolling log of all logged Central-i offline (mailbox) transactions, recorded on offline mailbox 2.
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

Rolling log of all logged Central-i offline (mailbox) transactions, recorded on offline mailbox 2.

## Overview

`OfflineBLog` is a non-axis array that records the most recent Central-i **offline** (mailbox) transactions on **offline mailbox 2**. This is the log that the firmware actually populates, and it captures offline traffic from more than one source, not just [CIOfflineSend](CIOfflineSend.md). The logged transactions (the request and its reply) come from:

- a user program calling [CIOfflineSend](CIOfflineSend.md) (a host function),
- background offline traffic, and
- the connect/event state machine (the "special" offline handling, e.g. during [CIConnect](CIConnect.md) and event processing).

The [Sender](#sender-field-values) field of each logged message identifies which of these issued it, so the host can review what was sent and what the remote returned. The companion array [OfflineALog](OfflineALog.md) (offline mailbox 1) is reserved but is not currently populated.

## How it works

The buffer has the same shape as [OfflineALog](OfflineALog.md): up to **5 messages of 9 fields** each (45 used elements, indices `[1]`…`[45]`). A write index advances per message, overwriting the oldest entry. The nine fields per message slot are:

| Offset in slot | Field | Meaning |
|----------------|-------|---------|
| +1 | Sender | What issued the message (see the table below) |
| +2 | Message type | `0` = query, `1` = assignment |
| +3 | Opcode | Remote register address read or written |
| +4 | Value out | Value sent (for an assignment) |
| +5 | Value in | Value returned (for a query) |
| +6 | Acknowledge / error | `0` = ok, otherwise the remote's error code |
| +7 | Time | Controller time when the message was sent (cf. [Time](../03-timing/Time.md)) |
| +8 | Sample counter | Sample counter at send time |
| +9 | Port | Axis/port number the message went to |

Message slot *k* (k = 0…4) occupies elements `[9k+1]` … `[9k+9]`.

### Sender field values

The **Sender** field (offset `+1` in each slot) identifies what issued the logged message:

| Value | Meaning |
|-------|---------|
| 2 | Host function — a user program calling [CIOfflineSend](CIOfflineSend.md) |
| 3 | Background offline traffic |
| 4 | Connect/event state machine (the "special" offline handling) |

Value `1` (interrupt) is reserved and is not currently emitted.

## Examples

```text
AOfflineBLog[1]     ; sender of the first logged message (2 = CIOfflineSend, 3 = background, 4 = special)
AOfflineBLog[3]     ; opcode of the first logged message
AOfflineBLog[5]     ; value returned by the remote for that message
AOfflineBLog[6]     ; its acknowledge/error code (0 = ok)
```

## See also

- [OfflineALog](OfflineALog.md) — the offline mailbox 1 log (reserved; not currently populated)
- [CIOfflineSend](CIOfflineSend.md) — one of the sources whose transactions are logged here
- [CIOfflineData](CIOfflineData.md) — request/response buffer for each transaction
