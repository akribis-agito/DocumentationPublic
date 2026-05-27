---
keyword: PosGain
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 100
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
    range:
    - 0
    - 1000000
---
# PosGain

Proportional gain of the position loop — the factor that multiplies the position error to produce the velocity command.

## Overview

`PosGain` is the proportional gain of the outer (position) loop in the PIV cascade. Each control cycle it multiplies the position error to produce the position-controller output, which is the main contribution to the velocity-loop reference [VelRef](../../10-motion/01-kinematics-status/VelRef.md). It is the single scaling factor that converts a position error (in main user units) into a commanded velocity (in main user units per second).

`PosGain` is an array, so it can take part in gain scheduling. Without gain scheduling the first element `PosGain[1]` is used for control. See [ScheduleMode](../01-general-keywords/ScheduleMode.md) for which array element is used under each scheduling method.

In gantry mode the gantry-specific position gain is used in place of `PosGain` for the gantried axes.

## How it works

The position controller acts on [PosErr](../../10-motion/01-kinematics-status/PosErr.md) (the position reference minus the position feedback). The proportional output is then summed with the velocity feed-forward (the scaled reference velocity [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md)) to form the velocity-loop reference:

$$
VelRef = PosErr \times PosGain + \frac{dPosRef \times VelTrackFact}{1024}
$$

The product is computed in extended precision and then clamped to the storable range before becoming `VelRef`. `VelRef` is afterwards hard-limited to ±[MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md).

- **What it multiplies:** the position error [PosErr](../../10-motion/01-kinematics-status/PosErr.md) (after the optional position-error filter; see [PosFiltOn](PosFiltOn.md)).
- **Where it sums:** its output is added to the [VelTrackFact](../04-velocity-control/VelTrackFact.md)-scaled velocity feed-forward to build [VelRef](../../10-motion/01-kinematics-status/VelRef.md), the input to the velocity loop.
- **Scaling / units:** applied as a direct multiplier (scaling factor 1.0). With a value of `0` the position loop produces no proportional command and only the velocity feed-forward remains.
- **Range / default:** `0` to `20000`, default `0`.

## Examples

```text
APosGain[1]=350     ; set the position-loop proportional gain (first scheduling element)
APosGain[1]         ; read the position-loop proportional gain
```

## Changes between versions

In **v4** the position loop is purely proportional: its output is `PosErr × PosGain`. In **v5 (central-i)** `PosGain` is a floating-point value with a wider range (`0` to `1000000`), the position error can first pass through a second-order position-error filter, and an optional position integral term ([PosKi](PosKi.md)) is added to the `PosGain` output before it forms `VelRef`. **v5 is central-i only.**

## See also

- [PosErr](../../10-motion/01-kinematics-status/PosErr.md) — position error that `PosGain` multiplies
- [VelRef](../../10-motion/01-kinematics-status/VelRef.md) — velocity-loop reference produced from the `PosGain` output
- [PosKi](PosKi.md) — position integral gain (v5) acting on the `PosGain` output
- [PosFiltOn](PosFiltOn.md) / [PosFiltDef](PosFiltDef.md) — optional position-loop filters
- [VelTrackFact](../04-velocity-control/VelTrackFact.md) — scales the velocity feed-forward summed with the `PosGain` output
- [VelGain](../04-velocity-control/VelGain.md) — proportional gain of the inner (velocity) loop
- [ScheduleMode](../01-general-keywords/ScheduleMode.md) — selects which array element is active
