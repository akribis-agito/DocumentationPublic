---
keyword: Identity
summary: Read-only array of controller information used by PCSuite to detect features.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 1
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 63
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Identity

Read-only array of controller information used by PCSuite to detect features.

## Overview

`Identity` is a read-only array that describes the controller. Agito PCSuite reads it to identify which features the controller implements and to adapt its GUI accordingly. It is non-axis and reflects the live device, not a stored value.

## See also

- [FWInfo](FWInfo.md) — firmware version and build information
- [About](About.md) — full parameter dump (Agito PCSuite internal use)
- [ProductSN](ProductSN.md) — the unit's product serial number
