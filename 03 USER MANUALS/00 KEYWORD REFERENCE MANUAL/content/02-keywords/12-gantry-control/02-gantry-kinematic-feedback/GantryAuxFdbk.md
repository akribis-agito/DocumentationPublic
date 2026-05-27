---
summary: Read-only auxiliary-encoder feedback used to measure gantry yaw.
keyword: GantryAuxFdbk
availability:
  standalone: []
  central-i:
  - v5
can_code: 674
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryAuxFdbk

Read-only auxiliary-encoder feedback used to measure gantry yaw.

## Overview

`GantryAuxFdbk` is a read-only parameter that reports the feedback position from the auxiliary encoder of the gantry axis. It is used by the gantry dual-loop controller to measure the yaw (misalignment) angle between the two beam ends. It is an axis-related status variable. The feedback source it derives from is selected by [GantryFdbkSrc](GantryFdbkSrc.md), and in dual-loop mode it underpins the velocity readings described in the [dual-loop gantry control overview](../04-dual-loop-gantry-control/00-overview.md).

> **Documentation pending:** This parameter could not be confirmed against the firmware parameter table. Availability and attributes need verification before use.

## See also

- [GantryFdbkSrc](GantryFdbkSrc.md) — selects the feedback source
- [GantryAuxVel](GantryAuxVel.md) — velocity derived from this feedback
- [GantryYawRef](../01-general-variables/GantryYawRef.md) — yaw correction reference
