---
keyword: CIAutoConnect
summary: When enabled, establishes the Central-i connection automatically at power-up.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 500
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CIAutoConnect

When enabled, establishes the Central-i connection automatically at power-up.

## Overview

`CIAutoConnect = 1` causes the controller to attempt a Central-i connection automatically on power-up or reset, without an explicit [CIConnect](CIConnect.md) from the host. `CIAutoConnect = 0` (default) requires the host to connect manually. The setting is axis-related and saved to flash.

## Examples

```text
CIAutoConnect=1     ; auto-connect this axis's Central-i port at startup
```

## See also

- [CIConnect](CIConnect.md) — connect manually
- [CIDisconnect](CIDisconnect.md) — disconnect
- [CIStatus](CIStatus.md) — link state
