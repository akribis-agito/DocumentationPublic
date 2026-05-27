---
summary: Active error-map correction value applied to the gantry yaw axis.
---
# GantryMap

Active error-map correction value applied to the gantry yaw axis.

## Overview

`GantryMap` is the active error-map correction value currently applied to the gantry yaw axis. It represents the position-dependent correction offset from the gantry map table, used to compensate for mechanical beam straightness errors. It is an axis-related parameter. The map is configured by [GantryMapType](GantryMapType.md) and indexed by the position source set in [GantryMapSrc](GantryMapSrc.md), with the looked-up value reported by [GantryMapVal](GantryMapVal.md).

> **Documentation pending:** This parameter could not be confirmed against the firmware parameter table. Availability and attributes (access, scope, flash, range) need verification before use.

## See also

- [GantryMapType](GantryMapType.md) — selects the map correction type
- [GantryMapSrc](GantryMapSrc.md) — position source used to index the map
- [GantryMapVal](GantryMapVal.md) — value read from the map at the current position
