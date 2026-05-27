---
summary: Selects the encoder/feedback source for the gantry yaw measurement.
---
# GantryFdbkSrc

Selects the encoder/feedback source for the gantry yaw measurement.

## Overview

`GantryFdbkSrc` selects which encoder or feedback source is used for the gantry yaw measurement. The chosen source is used to compute the differential position between the two beam ends. It is an axis-related parameter. In dual-loop gantry control this pointer designates the feedback (denoted "encoder C") that, together with the two main encoders, drives the loop — see the [dual-loop gantry control overview](../04-dual-loop-gantry-control/00-overview.md). It also feeds the readings reported by [GantryAuxFdbk](GantryAuxFdbk.md) and [GantryAuxVel](GantryAuxVel.md).

> **Documentation pending:** This parameter could not be confirmed against the firmware parameter table. Availability and attributes need verification before use.

## See also

- [GantryAuxFdbk](GantryAuxFdbk.md) — auxiliary feedback derived from this source
- [GantryAuxVel](GantryAuxVel.md) — auxiliary velocity derived from this source
- [GantryOn](../01-general-variables/GantryOn.md) — enables gantry MIMO control
