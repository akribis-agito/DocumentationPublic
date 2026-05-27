---
summary: Correction value read from the gantry map table at the current indexed position.
---
# GantryMapVal

Correction value read from the gantry map table at the current indexed position.

## Overview

`GantryMapVal` holds the current correction value read from the gantry map table at the position indexed by [GantryMapSrc](GantryMapSrc.md). It reflects the yaw offset correction being applied at the current beam position. It is an axis-related parameter. The correction mode is set by [GantryMapType](GantryMapType.md), and the value that is actually applied to the yaw axis is reported by [GantryMap](GantryMap.md).

> **Documentation pending:** This parameter could not be confirmed against the firmware parameter table. Availability and read-only/read-write status need verification before use.

## See also

- [GantryMap](GantryMap.md) — active map correction value
- [GantryMapSrc](GantryMapSrc.md) — position source used to index the map
- [GantryMapType](GantryMapType.md) — selects the map correction type
