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
\text{VelRef} = \text{PosErr} \cdot \text{PosGain} + \frac{\text{dPosRef} \cdot \text{VelTrackFact}}{1024}
$$

The product is computed in extended precision and then clamped to the storable range before becoming `VelRef`. `VelRef` is afterwards hard-limited to ±[MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md).

- **What it multiplies:** the position error [PosErr](../../10-motion/01-kinematics-status/PosErr.md) (after the optional position-error filter; see [PosFiltOn](PosFiltOn.md)).
- **Where it sums:** its output is added to the [VelTrackFact](../04-velocity-control/VelTrackFact.md)-scaled velocity feed-forward to build [VelRef](../../10-motion/01-kinematics-status/VelRef.md), the input to the velocity loop.
- **Scaling / units:** applied as a direct multiplier (scaling factor 1.0). With a value of `0` the position loop produces no proportional command and only the velocity feed-forward remains.

### Range and default

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Data type | 32-bit integer | 32-bit float |
| Range | 0 to 20000 | 0 to 1000000 |
| Default | 0 | 0 |

## Examples

```text
APosGain[1]=350     ; set the position-loop proportional gain (first scheduling element)
APosGain[1]         ; read the position-loop proportional gain
```

### Worked example: reading off the steady-state following error

With `PosGain = 350`, `VelTrackFact = 1024` (unity feed-forward), and the axis tracking a constant velocity reference of `dPosRef = 20000` user units/s, if at steady state the velocity loop perfectly follows `VelRef`, the position error needed for the position loop to balance any residual contribution can be read off:

`VelRef = PosErr x PosGain + dPosRef x VelTrackFact / 1024`

At steady state along a constant slew, `VelRef ≈ dPosRef` and the proportional term `PosErr x PosGain` only has to cover the small difference. With zero velocity feed-forward (`VelTrackFact = 0`), the position loop alone must supply all of `VelRef`, so `PosErr = VelRef / PosGain = 20000 / 350 ≈ 57.1` user units. The same axis with unity feed-forward typically shows a fraction of that error.

## Changes between versions

In **v4** the position loop is purely proportional: its output is `PosErr × PosGain`. In **v5 (central-i)** `PosGain` is a floating-point value with a wider range (`0` to `1000000`), the position error can first pass through a second-order position-error filter, and an optional position integral term ([PosKi](PosKi.md)) is added to the `PosGain` output before it forms `VelRef`. **v5 is central-i only.**

## See also

- [PosErr](../../10-motion/01-kinematics-status/PosErr.md) — position error that `PosGain` multiplies
- [VelRef](../../10-motion/01-kinematics-status/VelRef.md) — velocity-loop reference produced from the `PosGain` output
- [PosKi](PosKi.md) — position integral gain (v5) acting on the `PosGain` output
- [PosFiltOn](PosFiltOn.md) / [PosFiltDef](PosFiltDef.md) — optional position-loop filters
- [VelTrackFact](../04-velocity-control/VelTrackFact.md) — scales the velocity feed-forward summed with the `PosGain` output
- [AccFFW](../05-feedforwards/AccFFW.md) / [VelFFW](../05-feedforwards/VelFFW.md) — paired feedforwards added downstream of the position loop
- [VelGain](../04-velocity-control/VelGain.md) — proportional gain of the inner (velocity) loop
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 23 (velocity saturation) when the position-loop output exceeds MaxVel
- [ScheduleMode](../01-general-keywords/ScheduleMode.md) — selects which array element is active
