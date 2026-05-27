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

`RemoteCANAdd` specifies the CAN node address of the remote controller that will receive a message when [RemoteCANSend](RemoteCANSend.md) is executed. It is saved to flash and works together with [RemoteCANCCC](RemoteCANCCC.md) (the parameter to write) and [RemoteCANVal](RemoteCANVal.md) (the value) to form the outgoing transaction.

## Examples

```text
ARemoteCANAdd=128    ; address of the remote node to write to
```

## See also

- [RemoteCANCCC](RemoteCANCCC.md) — parameter identifier to write
- [RemoteCANVal](RemoteCANVal.md) — value to write
- [RemoteCANSend](RemoteCANSend.md) — execute the remote write
