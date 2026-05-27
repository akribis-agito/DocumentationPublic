---
summary: Initialises the gantry map correction feature before gantry motion.
---
# GantryMapInit

Initialises the gantry map correction feature before gantry motion.

## Overview

`GantryMapInit` initialises the gantry map correction feature. It is typically written once to set up the map table before gantry motion begins. It is an axis-related parameter. Once initialised, the map is described by [GantryMapType](GantryMapType.md), indexed by [GantryMapSrc](GantryMapSrc.md), and its active output is reported by [GantryMap](GantryMap.md) and [GantryMapVal](GantryMapVal.md).

> **Documentation pending:** This parameter could not be confirmed against the firmware parameter table. Availability and attributes (access, scope, flash, range) need verification before use.

## See also

- [GantryMap](GantryMap.md) — active map correction value
- [GantryMapType](GantryMapType.md) — selects the map correction type
- [GantryMapVal](GantryMapVal.md) — value read from the map at the current position
