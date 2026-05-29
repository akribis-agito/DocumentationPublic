---
keyword: CIOfflineSend
summary: Command that transmits the Central-i offline data package on the selected axis port.
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
removed_in:
- v5
---
# CIOfflineSend

Command that transmits the Central-i offline data package on the selected axis port.

## Overview

`CIOfflineSend` performs a single Central-i **offline** transaction on the selected axis port: it sends the addressed mailbox message built from [CIOfflineData](CIOfflineData.md) to the connected remote unit, waits for the reply, and writes the result back into [CIOfflineData](CIOfflineData.md). It is the way the host reads or writes one register inside a remote unit directly, outside the cyclic synchronous data exchange. It is a function keyword (no value).

## How it works

`CIOfflineSend` uses the port's **second** offline mailbox (the host channel), leaving the first mailbox for the firmware's own background traffic. When called it:

1. Checks the mailbox is free (not still transmitting or holding an unread reply).
2. Builds the outgoing message from [CIOfflineData](CIOfflineData.md): the message type ([1], query or assignment), the opcode/register address ([2]), and — for an assignment — the value to write ([3]).
3. Writes the message into the mailbox, which triggers transmission to the remote.
4. Waits (up to a timeout) for the reply. On success it stores the returned value in [CIOfflineData](CIOfflineData.md)`[4]` (for a query) and the acknowledge/error code in `[5]`; a timeout or a non-acknowledge reply reports a communication error.
5. Logs the whole exchange — sender, type, opcode, value out, value in, ack/error, time, sample counter and port — into the port-B offline log, [OfflineBLog](OfflineBLog.md).

A reply is expected, so the port should be connected ([CIStatus](CIStatus.md) showing connected) before sending.

## Examples

```text
ACIOfflineData[1]=0   ; query
ACIOfflineData[2]=...  ; remote register address
ACIOfflineSend         ; run the transaction
ACIOfflineData[4]      ; value returned by the remote
```

## Edge cases

- **Port disconnected.** `CIOfflineSend` does not gate on connection state, so it can be issued on a disconnected port. With no remote responding the transaction simply ends with a communication timeout and the error is captured in [CIOfflineData](CIOfflineData.md)`[5]`.
- **Motor on / in motion.** The command is permitted while the motor is on or moving — the offline mailbox is independent of the control loop. The reply still arrives in [CIOfflineData](CIOfflineData.md) on the same cycle window.
- **Power-up.** The offline channel is only usable after [CIConnect](CIConnect.md) (or [CIAutoConnect](CIAutoConnect.md)) has brought the port up; before that, no remote is addressable and the call times out.
- **Simulated device.** With [CIDeviceType](CIDeviceType.md) set to a simulation class the port is marked connected but there is no real remote — `CIOfflineSend` will time out, and the simulated-port path is intended for host tooling, not for real register access.
- **Standalone (v4).** Available on standalone v4 as well as on central-i v4/v5; the transaction targets one register on the remote across the link.

## Changes between versions

The transaction is present and behaves the same in both v4 and v5: it does not gate on connection state, and the reply has to come back within the timeout to succeed. The request/response field layout in [CIOfflineData](CIOfflineData.md) and the logging into [OfflineBLog](OfflineBLog.md) are unchanged between versions.

> **Frontmatter flag.** The generator-populated frontmatter currently lists this keyword as `removed_in: v5`, but v5 still defines and uses `CIOfflineSend` (CAN code 502). The generator's removed-in classification should be re-run; the body has been corrected to match the firmware.

## See also

- [CIOfflineData](CIOfflineData.md) — request/response buffer this command transmits
- [CIOfflineDef](CIOfflineDef.md) — offline-channel definition
- [OfflineBLog](OfflineBLog.md) — log of transactions sent by this command
- [CIConnect](CIConnect.md) — bring up the link before sending
