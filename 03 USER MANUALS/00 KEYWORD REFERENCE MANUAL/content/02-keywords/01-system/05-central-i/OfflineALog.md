---
keyword: OfflineALog
summary: Priority offline mailbox-1 transaction log on queue-enabled AGM800 and AGM800-EC firmware.
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
last_updated: '2026-10-17'
doc_revision: '2026.10'
---
# OfflineALog

Priority offline mailbox-1 transaction log on **queue-enabled AGM800 and AGM800-EC firmware**.

## Overview

The interrupt worker records lock-position queries and event target/selector writes when each transaction completes. The log is a shared ring of five messages across all ports. Older firmware and other products may leave this reserved array at zero.

Each entry is published as a complete terminal transaction, including failures and cancellations. A request refused before admission has no entry. A zero acknowledgement/error field means successful completion; a nonzero field is the remote error or a local communication error. Time and sample fields identify completion.

## Field layout

Slot *k* (k = 0…4) occupies `[9k+1]` … `[9k+9]`.

| Offset | Field | Meaning |
|---|---|---|
| +1 | Sender | `1` = interrupt |
| +2 | Message type | `0` = query, `1` = assignment |
| +3 | Opcode | Remote register address |
| +4 | Value out | Copied assignment value |
| +5 | Value in | Successful query value; otherwise zero |
| +6 | Acknowledge / error | Zero on success; nonzero on failure |
| +7 | Time | Controller time at completion |
| +8 | Sample counter | Sample counter at completion |
| +9 | Port | Zero-based axis/port number |

## Examples

```text
AOfflineALog[3]     ; opcode in slot 0
AOfflineALog[6]     ; terminal acknowledgement/error in slot 0
```

## See also

- [OfflineBLog](OfflineBLog.md) — mailbox-2 transactions, including CNC interrupt submissions
- [CIStatus](CIStatus.md) — mailbox error counters and last error
