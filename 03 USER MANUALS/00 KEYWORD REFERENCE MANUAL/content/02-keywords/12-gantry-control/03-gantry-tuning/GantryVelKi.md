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

`GantryVelKi` is the integral gain of the gantry velocity loop. When gantry mode is active (see [GantryOn](../01-general-variables/GantryOn.md)) it takes the role that the ordinary [VelKi](../../11-control-tuning/04-velocity-control/00-overview.md) plays in the per-axis velocity loop. While the proportional gain [GantryVelGain](GantryVelGain.md) responds to the present gantry velocity error, `GantryVelKi` acts on the accumulated velocity error so that any steady-state offset left by the proportional term is driven out. It is an axis-related, read/write parameter saved to flash and can be changed at any time, including while in motion and with the motor on. It is held per axis of the pair: the first axis runs the linear (common) gantry loop and the second axis runs the yaw (phase) loop, each using its own `GantryVelKi` value.

## How it works

The gantry velocity error is the difference between the velocity command from the gantry position loop and the gantry velocity feedback ([GantryVel](GantryVel.md)) — the common (linear) velocity on the first axis of the pair and the differential (yaw/phase) velocity on the second axis:

$$
\text{VelErr} = \text{VelRef} - \text{GantryVel}
$$

The controller multiplies the proportional term ($\text{VelErr} \cdot$ [GantryVelGain](GantryVelGain.md)) by `GantryVelKi` and a fixed internal integral-scaling factor, then accumulates it into the velocity integrator each control cycle (the accumulation is held when an anti-windup clamp is active, so the integral does not keep building while the current command is saturated):

$$
\text{Integral} \mathrel{+}= (\text{VelErr} \cdot \text{GantryVelGain}) \cdot \text{GantryVelKi} \cdot k_i
$$

The proportional term and this integral are summed and scaled to form the velocity PI output, which (after the velocity filters and feedforward) becomes the gantry current command ([CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)); the linear (common) and yaw (phase) commands are then combined and split across the two gantry motors.

The value is dimensionless. The allowed range is 0 to 100000 with a default of 100 (on controllers where the gantry gains are a 6-element gain-scheduled array the type follows the keyword attributes; the range stays 0 to 100000). A value of 0 disables the integral action of the gantry velocity loop.

## Examples

```text
AGantryVelKi[1]=50     ; set gantry velocity integral gain (first gain set)
AGantryVelKi[1]        ; read the current gain
```

On v4 the keyword is a single value (`AGantryVelKi=50`); on v5 it is a 6-element gain-scheduled array addressed `AGantryVelKi[1]`–`AGantryVelKi[5]`.

### Edge cases

- **Gantry off** — writes accepted; the gain has no effect until [GantryOn](../01-general-variables/GantryOn.md) = 1.
- **Zero gain** — disables integral action; the gantry velocity loop becomes proportional + feedforward only.
- **Per axis** — each axis of the gantry pair uses its own `GantryVelKi` (first axis = linear/common loop, second axis = yaw/phase loop). On a non-gantry axis the value is accepted but not used.
- **Out of range** — values outside `0`–`100000` are rejected on both v4 and v5 (the v5 per-element range is also `0`–`100000`).
- **Wind-up at engagement** — at gantry engagement the two axes' velocity-loop integrators are recombined into their common (half-sum) and differential (half-difference) parts so the transition is bumpless.
- **Save** — flash-saveable.
- **Platform** — v5 stores as a 6-element gain-scheduled `float32` array; v4 stores as a single `int32`.

## See also

- [GantryVelGain](GantryVelGain.md) — yaw velocity-loop proportional gain
- [GantryPosKi](GantryPosKi.md) — yaw position-loop integral gain
