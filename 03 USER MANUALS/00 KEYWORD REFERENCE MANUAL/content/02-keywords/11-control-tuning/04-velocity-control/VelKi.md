---
keyword: VelKi
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 103
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
  - 20000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# VelKi

Integral gain of the velocity loop — accumulates the scaled velocity-controller output, with internal anti-windup.

## Overview

`VelKi` is the integral gain of the inner (velocity) loop in the PIV cascade. Together with [VelGain](VelGain.md) it makes the velocity controller a PI controller: `VelGain` provides the proportional term and `VelKi` accumulates that proportional term over time. The proportional term plus the integral form the velocity-PI output, which (after the velocity filters and feed-forwards) becomes the motor current command [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md).

`VelKi` is an array, so it can take part in gain scheduling. Without gain scheduling the first element `VelKi[1]` is used for control. See [ScheduleMode](../01-general-keywords/ScheduleMode.md).

## How it works

Each control cycle the velocity error [VelErr](../../10-motion/01-kinematics-status/VelErr.md) is multiplied by [VelGain](VelGain.md) to form the proportional term. `VelKi` then multiplies that proportional term and the result is added into a running velocity integral:

$$
\text{integral} \mathrel{+}= \big( VelErr \times VelGain \big) \times VelKi \times k_{i}
$$

$$
\text{VelPIOutput} = \big( VelErr \times VelGain + \text{integral} \big) \times k_{scale}
$$

where $k_i$ and $k_{scale}$ are fixed internal scalings.

- **What it multiplies:** the velocity-controller proportional output (`VelErr × VelGain`), before that product enters the integral accumulator.
- **Where it sums:** the accumulated integral is added to the proportional term to form the velocity-PI output that becomes [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md).
- **Anti-windup:** the integral saturation value is controlled internally. When the current command saturates (at a torque/current limit) and the error has the same sign as the output, integration is halted for that cycle so the integral does not wind up. The integral is also preloaded when switching operation modes so the current command does not jump.
- **Range / default:** `0` to `20000`, default `0` (no integral action; velocity loop is purely proportional).

## Examples

```text
AVelKi[1]=80        ; set the velocity-loop integral gain (first scheduling element)
AVelKi[1]           ; read the velocity-loop integral gain
```

## Changes between versions

In **v5 (central-i)** `VelKi` is a floating-point value; the proportional×error accumulation, internal anti-windup and mode-switch preloading are otherwise the same. **v5 is central-i only.**

## See also

- [VelGain](VelGain.md) — proportional gain whose output `VelKi` integrates
- [VelErr](../../10-motion/01-kinematics-status/VelErr.md) — velocity error at the input of the velocity loop
- [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md) — current command produced from the velocity-PI output
- [PosKi](../03-position-control/PosKi.md) — integral gain of the outer (position) loop (v5)
- [ClearIntegral](../01-general-keywords/ClearIntegral.md) — clears the loop integrators
- [ScheduleMode](../01-general-keywords/ScheduleMode.md) — selects which array element is active
