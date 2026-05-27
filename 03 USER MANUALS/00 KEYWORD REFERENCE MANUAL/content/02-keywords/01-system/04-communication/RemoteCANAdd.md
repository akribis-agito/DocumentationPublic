---
keyword: RemoteCANAdd
summary: Target CAN node address for a remote write issued by RemoteCANSend.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 440
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2047
  default: 128
  scaling: 1.0
  implemented: final
overrides: {}
---
# RemoteCANAdd

Target CAN node address for a remote write issued by RemoteCANSend.

## Overview

`RemoteCANAdd` specifies the CAN node address of the remote controller that a [RemoteCANSend](RemoteCANSend.md) transaction targets. It is one of three registers that describe a remote access: `RemoteCANAdd` (which node), [RemoteCANCCC](RemoteCANCCC.md) (which parameter), and [RemoteCANVal](RemoteCANVal.md) (the value). It is saved to flash. The valid range is the full 11-bit CAN identifier space (0–2047); the default is 128.

## How it works

When `RemoteCANSend` runs, the controller programs its remote-access CAN mailboxes from `RemoteCANAdd`:

- it **transmits** the request to the address in `RemoteCANAdd`, and
- it **receives** the remote node's reply at `RemoteCANAdd + 1`.

This +0 / +1 request/reply pairing mirrors the receive/reply layout the controller itself uses for its own [CANAddr](CANAddr.md), so `RemoteCANAdd` should be set to the *base* receive address of the remote node.

## Examples

```text
ARemoteCANAdd=128    ; address of the remote node to access
```

## See also

- [RemoteCANCCC](RemoteCANCCC.md) — encoded parameter (CAN command code) to access
- [RemoteCANVal](RemoteCANVal.md) — value written, or value returned on a read
- [RemoteCANSend](RemoteCANSend.md) — execute the remote access
- [CANAddr](CANAddr.md) — this controller's own CAN address
