---
keyword: CISyncDef
summary: Per-axis array defining the parameters exchanged synchronously each control cycle.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 506
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
# CISyncDef

Per-axis array defining the parameters exchanged synchronously each control cycle.

## Overview

`CISyncDef` is an axis-related array that defines the set of parameters exchanged synchronously over the Central-i link on every control cycle — the real-time data map for the port. The definition is saved to flash and takes effect when [CIConnect](CIConnect.md) is executed. It is the synchronous (live-link) counterpart to the offline dataset defined by [CIOfflineDef](CIOfflineDef.md).

## Examples

```text
ACISyncDef[1]       ; read the first synchronous-data definition element
```

## See also

- [CILinkConfig](CILinkConfig.md) — physical/protocol parameters
- [CIOfflineDef](CIOfflineDef.md) — offline dataset definition
- [CIConnect](CIConnect.md) — initiate the link
