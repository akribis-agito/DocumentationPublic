---
summary: Read-only differential velocity of the gantry yaw axis.
---
# GantryVel

Read-only differential velocity of the gantry yaw axis.

## Overview

`GantryVel` is a read-only parameter that reports the current differential velocity of the gantry yaw axis, derived from the auxiliary feedback source. It is used by the gantry yaw velocity controller. It is an axis-related status variable. The [dual-loop gantry control overview](../04-dual-loop-gantry-control/00-overview.md) describes how `GantryVel` is computed under each control structure (including the `DualLoopFact` scaling) relative to [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md).

> **Documentation pending:** This parameter could not be confirmed against the firmware parameter table. Availability and attributes need verification before use.

## See also

- [GantryVelGain](GantryVelGain.md) — yaw velocity-loop proportional gain
- [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md) — auxiliary-encoder velocity
- [Dual-loop gantry control](../04-dual-loop-gantry-control/00-overview.md) — how GantryVel is derived per mode
