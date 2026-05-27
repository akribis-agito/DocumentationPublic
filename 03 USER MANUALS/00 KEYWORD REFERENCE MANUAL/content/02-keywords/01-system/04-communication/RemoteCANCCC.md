---
keyword: RemoteCANCCC
summary: CAN command code (parameter identifier) for a remote write issued by RemoteCANSend.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 441
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
  - -2147483648
  - 2147483647
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
---
# RemoteCANCCC

CAN command code (parameter identifier) for a remote write issued by RemoteCANSend.

## Overview

`RemoteCANCCC` holds the **Complex CAN Code** (CCC) that identifies *which* parameter on the remote controller a [RemoteCANSend](RemoteCANSend.md) transaction acts on. It is more than a bare CAN code: it encodes the target keyword's CAN code together with the axis it applies to and, for array keywords, the array index. Together with [RemoteCANAdd](RemoteCANAdd.md) (the node) and [RemoteCANVal](RemoteCANVal.md) (the value) it forms a complete remote access. It is saved to flash.

## How it works

When `RemoteCANSend` runs, the firmware decomposes `RemoteCANCCC` into its parts — the parameter's CAN code, the addressed axis, and the array index — and packs them into the outgoing CAN frame's identifier and data bytes. This is why a single integer can address any parameter on the remote node, including a specific element of an array keyword and a specific axis.

The practical way to obtain the right value is to take the CAN code of the remote parameter and combine it with the axis/index encoding used by the controller's CAN protocol (see the communication manual for the exact bit layout). The default is 2.

## Examples

```text
ARemoteCANCCC=100    ; encoded identifier of the remote parameter to access
```

## See also

- [RemoteCANAdd](RemoteCANAdd.md) — target node address
- [RemoteCANVal](RemoteCANVal.md) — value written, or value returned on a read
- [RemoteCANSend](RemoteCANSend.md) — execute the remote access
