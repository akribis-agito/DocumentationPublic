---
summary: Selects the position source used to index the gantry map correction table.
keyword: GantryMapSrc
availability:
  standalone: []
  central-i:
  - v5
can_code: 753
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryMapSrc

Selects the position source used to index the gantry map correction table.

## Overview

`GantryMapSrc` selects the position source used as the index into the gantry map correction table. The chosen source determines which axis position is used to look up the yaw correction offset from the map. It is an axis-related parameter. The looked-up correction is reported by [GantryMapVal](GantryMapVal.md) and applied as [GantryMap](GantryMap.md); the table itself is configured by [GantryMapType](GantryMapType.md).

> **Documentation pending:** This parameter could not be confirmed against the firmware parameter table. Availability and attributes (access, scope, flash, range) need verification before use.

## See also

- [GantryMap](GantryMap.md) — active map correction value
- [GantryMapType](GantryMapType.md) — selects the map correction type
- [GantryMapVal](GantryMapVal.md) — value read from the map at the indexed position
