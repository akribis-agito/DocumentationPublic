---
summary: Selects the type of gantry map correction applied to the yaw axis.
keyword: GantryMapType
availability:
  standalone: []
  central-i:
  - v5
can_code: 749
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
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryMapType

Selects the type of gantry map correction applied to the yaw axis.

## Overview

`GantryMapType` selects the type of gantry map correction applied to the yaw axis. Different values activate different correction modes (for example, using a lookup table versus a polynomial). It is an axis-related parameter. The position used to index the map is chosen by [GantryMapSrc](GantryMapSrc.md), and the resulting correction is reported by [GantryMapVal](GantryMapVal.md) and applied as [GantryMap](GantryMap.md).

> **Documentation pending:** This parameter could not be confirmed against the firmware parameter table. Availability, attributes, and the meaning of each value need verification before use.

## See also

- [GantryMap](GantryMap.md) — active map correction value
- [GantryMapSrc](GantryMapSrc.md) — position source used to index the map
- [GantryMapVal](GantryMapVal.md) — value read from the map at the current position
