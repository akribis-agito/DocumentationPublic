---
keyword: RemoteCANVal
summary: Value to write to the remote controller's parameter on RemoteCANSend.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 442
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# RemoteCANVal

Value to write to the remote controller's parameter on RemoteCANSend.

## Overview

`RemoteCANVal` is the data register of a remote-CAN access. Its role depends on the kind of access requested by [RemoteCANSend](RemoteCANSend.md):

- On a **write** (assignment), it supplies the value written to the remote parameter identified by [RemoteCANCCC](RemoteCANCCC.md).
- On a **read** (inquiry), the firmware overwrites it with the value returned by the remote node, so after the access completes you read the result back from `RemoteCANVal`.

It is a transient register and is **not** saved to flash. The default is -1.

## How it works

For a write, set `RemoteCANVal` before calling `RemoteCANSend`; the firmware packs it into the outgoing CAN frame. For a read, its prior contents are irrelevant — when the reply arrives the firmware decodes the returned value and stores it here. If the remote node reports an error instead of a normal reply, `RemoteCANVal` receives the returned error code rather than a parameter value.

## Examples

```text
ARemoteCANVal=5000   ; value to send on a write access
ARemoteCANVal        ; after a read access, holds the value returned by the remote node
```

## See also

- [RemoteCANAdd](RemoteCANAdd.md) — target node address
- [RemoteCANCCC](RemoteCANCCC.md) — encoded parameter to access
- [RemoteCANSend](RemoteCANSend.md) — execute the remote access (write / read / function)
