---
summary: Enables dual-loop (position + yaw) gantry control mode.
keyword: GantryDLoopOn
availability:
  standalone: []
  central-i:
  - v5
can_code: 675
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryDLoopOn

Enables dual-loop (position + yaw) gantry control mode.

## Overview

`GantryDLoopOn` enables the dual-loop (position + yaw) control mode for the gantry axis. When set to a non-zero value, the controller adds a yaw correction current to the two gantry drive motors to maintain alignment. It is an axis-related parameter. Dual-loop gantry control draws feedback from the two main encoders together with the source selected by [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md); see the [dual-loop gantry control overview](../04-dual-loop-gantry-control/00-overview.md) for how the feedback sources differ between modes.

> **Documentation pending:** This parameter could not be confirmed against the firmware parameter table. Availability and attributes (access, scope, flash, range) need verification before use.

## See also

- [GantryOn](GantryOn.md) — enables gantry MIMO control
- [GantryYawRef](GantryYawRef.md) — yaw correction reference
- [GantryPosGain](../03-gantry-tuning/GantryPosGain.md) — yaw position-loop gain
