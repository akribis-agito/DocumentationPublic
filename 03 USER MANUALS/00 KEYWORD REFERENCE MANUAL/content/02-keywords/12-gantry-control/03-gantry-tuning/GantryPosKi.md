---
summary: Integral gain for the gantry yaw position loop.
keyword: GantryPosKi
availability:
  standalone: []
  central-i:
  - v5
can_code: 715
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
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryPosKi

Integral gain for the gantry yaw position loop.

## Overview

`GantryPosKi` is the integral gain of the gantry yaw position loop. It is the yaw-loop counterpart of the ordinary position-loop integral gain ([PosKi](../../11-control-tuning/03-position-control/00-overview.md)): while the proportional term [GantryPosGain](GantryPosGain.md) responds to the present yaw position error, `GantryPosKi` acts on the accumulated yaw position error so that residual (steady-state) yaw misalignment is driven out over time. It is an axis-related parameter, readable and writable while in motion and with the motor on, and is one of the gantry tuning gains that the controller substitutes for the normal control gains when gantry mode is active (see [GantryOn](../01-general-variables/GantryOn.md)).

## How it works

When gantry mode is active the yaw position error is formed as the difference between the shaped/filtered position reference and the gantry (differential) feedback:

$$
PosErr = PosRef_{shaped} - GantryFdbk
$$

`GantryPosKi` scales the integral (running sum) of this yaw position error. The proportional part ([GantryPosGain](GantryPosGain.md)) and this integral part together form the velocity command sent into the yaw velocity PI loop ([GantryVelGain](GantryVelGain.md) / [GantryVelKi](GantryVelKi.md)), whose output becomes the differential current applied to the two gantry motors. `GantryPosKi` belongs to the same gantry gain set as [GantryPosGain](GantryPosGain.md), [GantryVelGain](GantryVelGain.md), [GantryVelKi](GantryVelKi.md), [GantryAccFFW](GantryAccFFW.md) and [GantryVelFFW](GantryVelFFW.md); on controllers that support gantry gain scheduling all six switch together as a set.

The value is dimensionless. A value of 0 disables the integral action of the yaw position loop. Refer to the keyword attributes for the range and default on a given controller.

## Examples

```text
AGantryPosKi[1]=0   ; set yaw position integral gain (first gain set)
AGantryPosKi[1]     ; read the current value
```

## See also

- [GantryPosGain](GantryPosGain.md) — yaw position-loop proportional gain
- [GantryVelGain](GantryVelGain.md) — yaw velocity-loop proportional gain
- [GantryVelKi](GantryVelKi.md) — yaw velocity-loop integral gain
