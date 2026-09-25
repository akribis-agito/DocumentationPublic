---
keyword: PushEvSelSys
summary: Bitmask of the controller-wide push-event types to send.
availability:
  standalone: []
  central-i:
  - v5
can_code: 912
attributes:
  access: rw
  scope: non-axis
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
last_updated: '2026-09-25'
doc_revision: '2026.09'
---
# PushEvSelSys

Bitmask of the controller-wide push-event types to send.

## Overview

`PushEvSelSys` chooses which controller-wide [push-event](00-overview.md) types the controller sends. A controller-wide event belongs to no axis and carries axis `0xFF` in its record. Event types that belong to an axis are selected per axis in [PushEvSelect](PushEvSelect.md).

It uses the same layout and bit rule as `PushEvSelect`, but it is a single, non-axis setting. It is saved to flash with [Save](../02-operation/Save.md). The default is 0.

| Index | Event types |
|---|---|
| `[1]` | types 1-32: type *k* is bit *k*−1 |
| `[2]` | types 33-64: type *k* is bit *k*−33 |

Arrays are 1-indexed; `PushEvSelSys[0]` does not exist.

> **No controller-wide event type exists in this release.** The only defined type, Profile ended (type 1), belongs to an axis. `PushEvSelSys` is stored and saved, but no event reads it yet. It is in place so that controller-wide types added later can be selected without a new keyword.

## Examples

```text
APushEvSelSys[1]     ; read the mask for types 1-32
APushEvSelSys[1]=0   ; select no controller-wide types (default)
```

## See also

- [PushEvSelect](PushEvSelect.md) — per-axis event-type mask
- [PushEvEnable](PushEvEnable.md) — master switch
- [Push Events overview](00-overview.md)
