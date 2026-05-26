---
keyword: RemoteCANVal
summary: Value to write to the remote controller's parameter on RemoteCANSend.
availability:
  standalone:
  - v4
  - v5
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

`RemoteCANVal` holds the value that will be written to the remote controller's parameter — identified by [RemoteCANCCC](RemoteCANCCC.md) — when [RemoteCANSend](RemoteCANSend.md) is executed. It is a transient register and is **not** saved to flash.

## Examples

```text
RemoteCANVal=5000   ; value to send to the remote parameter
```

## See also

- [RemoteCANAdd](RemoteCANAdd.md) — target node address
- [RemoteCANCCC](RemoteCANCCC.md) — parameter identifier to write
- [RemoteCANSend](RemoteCANSend.md) — execute the remote write
