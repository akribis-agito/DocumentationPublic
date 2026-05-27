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

`RemoteCANSend` transmits a CAN write message to a remote node. It uses the three RemoteCAN registers set beforehand:

1. [RemoteCANAdd](RemoteCANAdd.md) — the target node's CAN address
2. [RemoteCANCCC](RemoteCANCCC.md) — the parameter (CAN command code) to write
3. [RemoteCANVal](RemoteCANVal.md) — the value to write

Set those three, then execute `RemoteCANSend` to perform the remote write. It can be executed during motion.

## Examples

```text
ARemoteCANAdd=128    ; target node
ARemoteCANCCC=100    ; parameter to write on the remote node
ARemoteCANVal=5000   ; value
ARemoteCANSend=1     ; send the write
```

## See also

- [RemoteCANAdd](RemoteCANAdd.md) — target node address
- [RemoteCANCCC](RemoteCANCCC.md) — parameter identifier
- [RemoteCANVal](RemoteCANVal.md) — value to write
