---
keyword: VelGain
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 102
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range:
    - 0
    - 1000000000
---
# VelGain

Proportional gain of the velocity loop — the factor that multiplies the velocity error.

## Overview

`VelGain` is the proportional gain of the inner (velocity) loop in the PIV cascade. Each control cycle it multiplies the velocity error [VelErr](../../10-motion/01-kinematics-status/VelErr.md) to form the proportional part of the velocity-PI output. That output (proportional plus the [VelKi](VelKi.md) integral, after the velocity filters) becomes the motor current command [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md) that drives the current loop.

`VelGain` is an array, so it can take part in gain scheduling. Without gain scheduling the first element `VelGain[1]` is used for control. See [ScheduleMode](../01-general-keywords/ScheduleMode.md).

In gantry mode the gantry-specific velocity gain is used in place of `VelGain` for the gantried axes.

## How it works

The velocity controller acts on [VelErr](../../10-motion/01-kinematics-status/VelErr.md) (the velocity reference [VelRef](../../10-motion/01-kinematics-status/VelRef.md) minus the velocity feedback). The proportional term and the integral are summed and scaled internally to produce the velocity-PI output:

$$
\text{proportional} = VelErr \times VelGain
$$

$$
\text{VelPIOutput} = \big( \text{proportional} + \text{integral} \big) \times k_{scale}
$$

The integral is the running accumulation of `proportional × VelKi` (see [VelKi](VelKi.md)). `VelPIOutput` then passes through the velocity filters ([VelFiltOn](VelFiltOn.md) / [VelFiltDef](VelFiltDef.md)) and, in position mode, has the acceleration and velocity feed-forwards added to form the current command [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md).

- **What it multiplies:** the velocity error [VelErr](../../10-motion/01-kinematics-status/VelErr.md).
- **Where it sums:** its product is added to the velocity integral; the sum (after internal scaling and the velocity filters) becomes [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md).
- **Scaling / units:** applied as a multiplier (scaling factor 1.0); the combined PI result is brought to current-command units by a fixed internal scaling.
- **Range / default:** `0` to `1000000`, default `0`.

## Examples

```text
AVelGain[1]=1200    ; set the velocity-loop proportional gain (first scheduling element)
AVelGain[1]         ; read the velocity-loop proportional gain
```

### Worked example: proportional contribution at a velocity error

With `VelGain = 1200` and a velocity error `VelErr = 50` (in velocity-loop units), the proportional term entering the PI sum is:

`proportional = VelErr x VelGain = 50 x 1200 = 60000`

This product enters the PI sum (together with the integral) and is then converted to current-command units by the fixed internal scaling before passing through the velocity filters and feedforwards.

## Changes between versions

In **v5 (central-i)** `VelGain` is a floating-point value (same `0` to `1000000000` range concept, wider span); the proportional×error → PI → current-command path is otherwise the same. **v5 is central-i only.**

## See also

- [VelErr](../../10-motion/01-kinematics-status/VelErr.md) — velocity error that `VelGain` multiplies
- [VelRef](../../10-motion/01-kinematics-status/VelRef.md) — velocity-loop reference
- [VelKi](VelKi.md) — velocity integral gain summed with the `VelGain` term
- [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md) — current command produced from the velocity-PI output
- [VelFiltOn](VelFiltOn.md) / [VelFiltDef](VelFiltDef.md) — velocity-loop filters on the PI output
- [PosGain](../03-position-control/PosGain.md) — proportional gain of the outer (position) loop
- [ScheduleMode](../01-general-keywords/ScheduleMode.md) — selects which array element is active
