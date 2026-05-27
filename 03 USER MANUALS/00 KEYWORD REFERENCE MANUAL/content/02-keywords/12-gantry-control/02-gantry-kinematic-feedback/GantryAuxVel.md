---
summary: Read-only velocity derived from the gantry auxiliary encoder.
---
# GantryAuxVel

Read-only velocity derived from the gantry auxiliary encoder.

## Overview

`GantryAuxVel` is a read-only parameter that reports the velocity derived from the gantry auxiliary encoder. It provides the differential velocity information used by the gantry yaw controller. It is an axis-related status variable. As described in the [dual-loop gantry control overview](../04-dual-loop-gantry-control/00-overview.md), it is the derivative of [GantryAuxFdbk](GantryAuxFdbk.md), whose source is set by [GantryFdbkSrc](GantryFdbkSrc.md).

> **Documentation pending:** This parameter could not be confirmed against the firmware parameter table. Availability and attributes need verification before use.

## See also

- [GantryAuxFdbk](GantryAuxFdbk.md) — auxiliary feedback this velocity is derived from
- [GantryFdbkSrc](GantryFdbkSrc.md) — selects the feedback source
