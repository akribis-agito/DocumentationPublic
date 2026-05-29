---
keyword: OfflineALog
summary: Reserved offline (mailbox) message log for Central-i offline mailbox 1; not currently populated by the firmware, so it stays at 0.
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

Reserved offline (mailbox) message log for Central-i **offline mailbox 1**; not currently populated by the firmware.

## Overview

`OfflineALog` is a non-axis array that is **reserved** as the log for Central-i **offline mailbox 1** (the priority, firmware-driven channel). It is **not currently populated** by the firmware, so all of its elements stay at their default of `0`; reading it does not return offline-message data.

The offline transactions that are actually logged are recorded in [OfflineBLog](OfflineBLog.md) (offline mailbox 2). Use that log to inspect the offline messages that were exchanged and their results.

## How it works

The array is dimensioned the same way as [OfflineBLog](OfflineBLog.md): up to **5 messages of 9 fields** each (45 used elements, indices `[1]`…`[45]`). Because nothing currently writes to it, every element reads `0`. The intended per-message field layout (which [OfflineBLog](OfflineBLog.md) does populate) is, in order:

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

Message slot *k* (k = 0…4) would occupy elements `[9k+1]` … `[9k+9]`. The same field layout is populated for [OfflineBLog](OfflineBLog.md).

## Examples

```text
AOfflineALog[3]     ; reserved slot; currently reads 0 (not populated)
AOfflineALog[12]    ; reserved slot; currently reads 0 (not populated)
```

## See also

- [OfflineBLog](OfflineBLog.md) — the offline mailbox 2 log, which is the one the firmware actually populates
- [CIOfflineData](CIOfflineData.md) / [CIOfflineSend](CIOfflineSend.md) — offline transactions
- [CIStatus](CIStatus.md) — offline error counters and last-error code
