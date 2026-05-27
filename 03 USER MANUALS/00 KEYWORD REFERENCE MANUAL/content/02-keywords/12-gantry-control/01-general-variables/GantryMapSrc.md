---
summary: Selects the position source used to index the gantry map correction table.
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
