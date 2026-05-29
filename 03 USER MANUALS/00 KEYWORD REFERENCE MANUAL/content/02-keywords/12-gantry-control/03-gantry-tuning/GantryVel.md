---
summary: Read-only differential velocity of the gantry yaw axis.
keyword: GantryVel
availability:
  standalone: []
  central-i:
  - v5
can_code: 676
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
# GantryVel

Read-only differential velocity of the gantry yaw axis.

## Overview

`GantryVel` is a read-only variable that reports the differential (yaw) velocity of the gantry. It is the velocity feedback used by the gantry yaw velocity loop: when gantry mode is active (see [GantryOn](../01-general-variables/GantryOn.md)) the yaw velocity error is formed against `GantryVel` rather than the single-axis velocity. It is an axis-related status variable, valid while in motion and with the motor on, and is not saved to flash.

## How it works

Each control cycle the controller derives `GantryVel` from the gantry feedback and uses it as the velocity term in the yaw velocity PI loop:

$$
\text{VelErr} = \text{VelRef} - \text{GantryVel}
$$

where `VelRef` is the velocity command produced by the yaw position loop ([GantryPosGain](GantryPosGain.md) / [GantryPosKi](GantryPosKi.md)) and the resulting yaw velocity error is acted on by [GantryVelGain](GantryVelGain.md) and [GantryVelKi](GantryVelKi.md). `GantryVel` is reported in user units. The [dual-loop gantry control overview](../04-dual-loop-gantry-control/00-overview.md) describes how `GantryVel` is computed under each control structure (including the `DualLoopFact` scaling) relative to [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md).

## Examples

```text
AGantryVel          ; read the gantry differential (yaw) velocity
```

## See also

- [GantryVelGain](GantryVelGain.md) — yaw velocity-loop proportional gain
- [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md) — auxiliary-encoder velocity
- [Dual-loop gantry control](../04-dual-loop-gantry-control/00-overview.md) — how GantryVel is derived per mode
