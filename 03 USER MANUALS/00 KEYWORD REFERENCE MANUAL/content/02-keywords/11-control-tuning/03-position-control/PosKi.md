---
keyword: PosKi
availability:
  standalone: []
  central-i:
  - v5
can_code: 714
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
# PosKi

Integral gain of the position loop (central-i v5) — accumulates the scaled position-controller output to add an integral term to the velocity command.

## Overview

`PosKi` is the integral gain of the outer (position) loop. It turns the position controller into a PI controller: where [PosGain](PosGain.md) alone provides a proportional command, `PosKi` accumulates that proportional output over time and adds the accumulated value to the velocity-loop reference [VelRef](../../10-motion/01-kinematics-status/VelRef.md). This allows the position loop to drive steady-state position error toward zero.

`PosKi` is available on **central-i v5 only**. It is an array, so it can take part in gain scheduling; without scheduling the first element `PosKi[1]` is used. See [ScheduleMode](../01-general-keywords/ScheduleMode.md).

## How it works

Each control cycle the (filtered) position error is multiplied by [PosGain](PosGain.md) to form the proportional term. `PosKi` then multiplies that proportional term and the result is added into a running position integral. The proportional term plus the position integral, together with the velocity feed-forward, form the velocity-loop reference:

$$
VelRef = \left( PosErr \times PosGain \right) + \text{integral}\!\left( PosErr \times PosGain \times PosKi \right) + \frac{dPosRef \times VelTrackFact}{1024}
$$

- **What it multiplies:** the position-controller proportional output (`PosErr × PosGain`), before that product enters the integral accumulator.
- **Where it sums:** the accumulated integral is added to the proportional term and the velocity feed-forward to build [VelRef](../../10-motion/01-kinematics-status/VelRef.md).
- **Anti-windup:** the integral saturation value is controlled internally. When the command saturates (for example at the current limit) the integral stops accumulating for that cycle, so it does not wind up.
- **Default:** `0` (position integral disabled, so the position loop is purely proportional).

## Examples

```text
APosKi[1]=2.5       ; enable a position-loop integral term (first scheduling element)
APosKi[1]           ; read the position-loop integral gain
```

## See also

- [PosGain](PosGain.md) — proportional gain whose output `PosKi` integrates
- [PosErr](../../10-motion/01-kinematics-status/PosErr.md) — position error at the input of the position loop
- [VelRef](../../10-motion/01-kinematics-status/VelRef.md) — velocity-loop reference that the position PI output forms
- [VelKi](../04-velocity-control/VelKi.md) — integral gain of the inner (velocity) loop
- [ClearIntegral](../01-general-keywords/ClearIntegral.md) — clears the loop integrators
- [ScheduleMode](../01-general-keywords/ScheduleMode.md) — selects which array element is active
