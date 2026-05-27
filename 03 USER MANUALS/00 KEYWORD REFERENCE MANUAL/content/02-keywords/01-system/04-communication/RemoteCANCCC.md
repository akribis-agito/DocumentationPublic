---
keyword: RemoteCANCCC
summary: CAN command code (parameter identifier) for a remote write issued by RemoteCANSend.
availability:
  standalone:
  - v4
  - v5
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

`RemoteCANCCC` holds the CAN Command Code (CCC) — the parameter identifier — that will be written on the remote controller when [RemoteCANSend](RemoteCANSend.md) is executed. Together with [RemoteCANAdd](RemoteCANAdd.md) (the target node) and [RemoteCANVal](RemoteCANVal.md) (the value) it defines the complete remote write. It is saved to flash.

## Examples

```text
ARemoteCANCCC=100    ; write the remote node's parameter with CAN code 100
```

## See also

- [RemoteCANAdd](RemoteCANAdd.md) — target node address
- [RemoteCANVal](RemoteCANVal.md) — value to write
- [RemoteCANSend](RemoteCANSend.md) — execute the remote write
