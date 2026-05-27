---
keyword: GantryVelGain
summary: Proportional velocity gain for the gantry yaw correction controller.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 656
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 100000
  default: 100
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    type: array
    array_size: 6
    data_type: float32
    range:
    - 0
    - 100000000
---
# GantryVelGain

Proportional velocity gain for the gantry yaw correction controller.

## Overview

`GantryVelGain` is the proportional gain of the gantry yaw velocity loop. When gantry mode is active (see [GantryOn](../01-general-variables/GantryOn.md)) it takes the role that the ordinary [VelGain](../../11-control-tuning/04-velocity-control/00-overview.md) plays in the per-axis velocity loop, scaling the yaw (differential) velocity error to form the corrective current command. It is an axis-related parameter saved to flash and can be changed at any time, including while in motion and with the motor on.

## How it works

In gantry mode the yaw velocity error is the difference between the velocity command from the yaw position loop and the gantry differential velocity ([GantryVel](GantryVel.md)) rather than the single-axis velocity:

$$
VelErr = VelRef - GantryVel
$$

`GantryVelGain` scales this yaw velocity error to produce the proportional term of the velocity PI controller:

$$
P = VelErr \times GantryVelGain
$$

This proportional term is summed with the integral term scaled by [GantryVelKi](GantryVelKi.md); the combined PI output is then passed through the velocity-loop filters and an internal scaling factor, and finally added to the feedforward terms to form the differential motor current command ([CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)) applied to the two gantry motors. Raising `GantryVelGain` increases the current produced per unit of yaw velocity error.

The value is dimensionless. The allowed range is 0 to 100000 with a default of 100 (on controllers where the gantry gains are a 6-element gain-scheduled array the upper range is extended; see the keyword attributes). A value of 0 disables the proportional action of the yaw velocity loop.

## Examples

```text
AGantryVelGain=150  ; set yaw velocity proportional gain
AGantryVelGain     ; read the current gain
```

## See also

- [GantryVelKi](GantryVelKi.md) — yaw velocity-loop integral gain
- [GantryPosGain](GantryPosGain.md) — yaw position-loop proportional gain
- [GantryAccFFW](GantryAccFFW.md) — acceleration feedforward gain
- [GantryVelFFW](GantryVelFFW.md) — velocity feedforward gain
