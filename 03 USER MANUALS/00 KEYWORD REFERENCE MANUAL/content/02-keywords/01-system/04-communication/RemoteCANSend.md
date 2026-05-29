---
keyword: RemoteCANSend
summary: Command that transmits a CAN write to a remote node using the RemoteCAN* registers.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 443
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 1
  - 3
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RemoteCANSend

Command that transmits a CAN write to a remote node using the RemoteCAN* registers.

## Overview

`RemoteCANSend` performs a single CAN access to a remote node, letting one controller act as a CAN master toward another. It uses the three RemoteCAN registers set beforehand:

1. [RemoteCANAdd](RemoteCANAdd.md) — the target node's CAN address
2. [RemoteCANCCC](RemoteCANCCC.md) — the encoded parameter (Complex CAN Code) to access
3. [RemoteCANVal](RemoteCANVal.md) — the value to write, or where a read result is returned

The value you assign to `RemoteCANSend` selects the kind of access:

| RemoteCANSend | Access | Effect |
|---|---|---|
| 1 | Assignment (write) | Writes [RemoteCANVal](RemoteCANVal.md) to the remote parameter |
| 2 | Inquiry (read) | Reads the remote parameter; the returned value is stored back in [RemoteCANVal](RemoteCANVal.md) |
| 3 | Function | Executes the remote parameter as a function/command |

## How it works

`RemoteCANSend` must be executed from inside a **user program** — it is rejected if issued directly over a normal communication channel, because it blocks the issuing thread while it waits for the remote node. On execution the controller:

1. Programs its remote-access mailboxes to transmit to [RemoteCANAdd](RemoteCANAdd.md) and receive replies at `RemoteCANAdd + 1`.
2. Builds the request frame from [RemoteCANCCC](RemoteCANCCC.md) (and, for a write, the 32-bit [RemoteCANVal](RemoteCANVal.md)) and transmits it.
3. Waits in two stages — first for the frame to be transmitted, then for the remote node's reply — with a timeout of about 100 ms at each stage.
4. Interprets the reply: a write/function expects an "OK" acknowledgement; an inquiry expects a value, which is decoded from the 32-bit reply and written into [RemoteCANVal](RemoteCANVal.md).

The transaction can report these errors:

| Error | Meaning |
|---|---|
| 111 | `RemoteCANSend` was not issued from a user program (it must run inside one). |
| 238 | Remote-access timeout — the transmit or reply did not complete within its ~100 ms stage. |
| 239 | The remote node answered with an error; its 16-bit error code is written into [RemoteCANVal](RemoteCANVal.md). |
| 240 | The reply could not be interpreted. |

It can be executed during motion.

> Platform note: this transaction is implemented on the standalone/controller platform. On the central-i platform the remote-CAN master transaction is not yet implemented.

## Examples

```text
ARemoteCANAdd=128    ; target node
ARemoteCANCCC=100    ; encoded parameter on the remote node
ARemoteCANVal=5000   ; value (used for a write)
ARemoteCANSend=1     ; perform a write

ARemoteCANSend=2     ; perform a read; afterwards ARemoteCANVal holds the returned value
```

## See also

- [RemoteCANAdd](RemoteCANAdd.md) — target node address
- [RemoteCANCCC](RemoteCANCCC.md) — encoded parameter to access
- [RemoteCANVal](RemoteCANVal.md) — value written, or value returned on a read
- [SendToCntrlr](SendToCntrlr.md) — relay a value to another controller over serial
