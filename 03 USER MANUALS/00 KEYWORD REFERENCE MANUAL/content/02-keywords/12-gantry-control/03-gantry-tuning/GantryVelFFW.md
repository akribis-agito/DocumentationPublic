---
summary: Velocity feedforward gain for the gantry yaw correction controller.
keyword: GantryVelFFW
availability:
  standalone: []
  central-i:
  - v5
can_code: 678
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 50000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryVelFFW

Velocity feedforward gain for the gantry yaw correction controller.

## Overview

`GantryVelFFW` sets the velocity feedforward gain for the gantry yaw correction controller. It scales the velocity reference to produce a feedforward current that reduces yaw error during motion. It is an axis-related parameter. It complements the acceleration feedforward [GantryAccFFW](GantryAccFFW.md) and the feedback gain [GantryVelGain](GantryVelGain.md).

> **Documentation pending:** This parameter could not be confirmed against the firmware parameter table. Availability and attributes need verification before use.

## See also

- [GantryVelGain](GantryVelGain.md) — yaw velocity-loop proportional gain
- [GantryAccFFW](GantryAccFFW.md) — acceleration feedforward gain
