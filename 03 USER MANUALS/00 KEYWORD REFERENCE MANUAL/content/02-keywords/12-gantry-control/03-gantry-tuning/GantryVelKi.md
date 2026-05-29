---
keyword: GantryVelKi
summary: Integral gain for the gantry yaw velocity loop.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 657
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
---
# GantryVelKi

Integral gain for the gantry yaw velocity loop.

## Overview

`GantryVelKi` is the integral gain of the gantry yaw velocity loop. When gantry mode is active (see [GantryOn](../01-general-variables/GantryOn.md)) it takes the role that the ordinary [VelKi](../../11-control-tuning/04-velocity-control/00-overview.md) plays in the per-axis velocity loop. While the proportional gain [GantryVelGain](GantryVelGain.md) responds to the present yaw velocity error, `GantryVelKi` acts on the accumulated yaw velocity error so that any steady-state offset left by the proportional term is driven out. It is an axis-related, read/write parameter saved to flash and can be changed at any time, including while in motion and with the motor on.

## How it works

The yaw velocity error is the difference between the velocity command from the yaw position loop and the gantry differential velocity ([GantryVel](GantryVel.md)):

$$
\text{VelErr} = \text{VelRef} - \text{GantryVel}
$$

The controller multiplies the proportional term ($\text{VelErr} \cdot$ [GantryVelGain](GantryVelGain.md)) by `GantryVelKi` and a fixed internal integral-scaling factor, then accumulates it into the velocity integrator each control cycle (the accumulation is held when an anti-windup clamp is active, so the integral does not keep building while the current command is saturated):

$$
\text{Integral} \mathrel{+}= (\text{VelErr} \cdot \text{GantryVelGain}) \cdot \text{GantryVelKi} \cdot k_i
$$

The proportional term and this integral are summed and scaled to form the velocity PI output, which (after the velocity filters and feedforward) becomes the differential motor current command ([CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)) on the two gantry motors.

The value is dimensionless. The allowed range is 0 to 100000 with a default of 100 (on controllers where the gantry gains are a 6-element gain-scheduled array the type and range follow the keyword attributes). A value of 0 disables the integral action of the yaw velocity loop.

## Examples

```text
AGantryVelKi=50     ; set yaw velocity integral gain
AGantryVelKi       ; read the current gain
```

### Edge cases

- **Gantry off** — writes accepted; the gain has no effect until [GantryOn](../01-general-variables/GantryOn.md) = 1.
- **Zero gain** — disables integral action; the yaw velocity loop becomes proportional + feedforward only.
- **Wrong axis** — consulted on the yaw axis of the pair; writes on the master or a non-gantry axis are accepted but not used.
- **Out of range** — values outside `0`–`100000` (v4) are rejected; v5 per-element range follows the keyword attributes.
- **Wind-up at engagement** — the firmware halves the velocity-loop integral across the master/yaw split at gantry engagement to keep the transition bumpless.
- **Save** — flash-saveable.
- **Platform** — v5 stores as a 6-element gain-scheduled `float32` array; v4 stores as a single `int32`.

## See also

- [GantryVelGain](GantryVelGain.md) — yaw velocity-loop proportional gain
- [GantryPosKi](GantryPosKi.md) — yaw position-loop integral gain
