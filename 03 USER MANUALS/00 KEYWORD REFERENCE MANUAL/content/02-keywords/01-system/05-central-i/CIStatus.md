---
keyword: CIStatus
summary: Per-axis array reporting the live state of the Central-i port.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 508
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 8
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CIStatus

Per-axis array reporting the live state of the Central-i port.

## Overview

`CIStatus` is a read-only, axis-related array reporting the current state of the Central-i port on the selected axis — connection status, error flags, and link-quality indicators. It is updated in real time and can be read in any motion or motor state. For a one-value, system-wide summary across all ports, use [CIGlobalStat](CIGlobalStat.md).

## Examples

```text
CIStatus[1]?        ; read the first status word for this axis's port
```

## See also

- [CIGlobalStat](CIGlobalStat.md) — system-wide connection summary
- [CIConnect](CIConnect.md) — initiate the link
- [CIIdentity](CIIdentity.md) — connected device identity
