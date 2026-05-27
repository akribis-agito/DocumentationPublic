---
summary: Selects the type of gantry map correction applied to the yaw axis.
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
