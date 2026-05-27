---
keyword: CIOfflineData
summary: Per-axis array holding the payload sent during a Central-i offline (simulation) transaction.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

Per-axis array holding the payload sent during a Central-i offline (simulation) transaction.

## Overview

`CIOfflineData` is the per-axis request/response buffer for a single Central-i **offline** transaction — a non-cyclic "mailbox" read or write to one register inside the connected remote unit. Unlike the synchronous channel (which exchanges control data every cycle), the offline channel carries occasional, addressed messages: query the value of a remote register, or assign a value to it. You set up the buffer, call [CIOfflineSend](CIOfflineSend.md), and then read the reply back from the same array. It is saved to flash. Index `[0]` is unused; the fields are `[1]`–`[5]`.

## How it works

| Index | Field | Meaning |
|-------|-------|---------|
| [1] | Message type | `0` = query (read a remote register), `1` = assignment (write a remote register) |
| [2] | Opcode | The address of the remote register to read or write |
| [3] | Value to assign | The value to write (used only when message type is `1`) |
| [4] | Inquired value | The value returned by the remote (filled on a successful query) |
| [5] | Acknowledge / error | `0` = acknowledged; any other value is the error code returned by the remote |

[CIOfflineSend](CIOfflineSend.md) builds the outgoing offline message from elements [1]–[3], transmits it on the port's offline mailbox, waits for the reply, and writes the result into [4] (for a query) and [5] (the ack/error). The exchange is also recorded in the offline log buffers ([OfflineALog](OfflineALog.md) / [OfflineBLog](OfflineBLog.md)).

This is an expert mechanism for reading or setting individual remote-unit registers directly; in normal operation the firmware itself uses the offline channel during [CIConnect](CIConnect.md) to read the remote's identity.

## Examples

```text
ACIOfflineData[1]=0   ; message type: query (read)
ACIOfflineData[2]=...  ; opcode: the remote register address to read
ACIOfflineSend         ; perform the transaction
ACIOfflineData[4]      ; read back the value returned by the remote
ACIOfflineData[5]      ; 0 = ok, non-zero = error code
```

## See also

- [CIOfflineDef](CIOfflineDef.md) — offline-channel definition (frequency / filter)
- [CIOfflineSend](CIOfflineSend.md) — transmit this transaction and capture the reply
- [OfflineALog](OfflineALog.md) / [OfflineBLog](OfflineBLog.md) — offline message logs
- [CISyncDef](CISyncDef.md) — the synchronous (per-cycle) channel, by contrast
