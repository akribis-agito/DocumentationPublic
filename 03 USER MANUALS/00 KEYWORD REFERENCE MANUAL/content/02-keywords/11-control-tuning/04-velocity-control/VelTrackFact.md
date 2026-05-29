---
keyword: VelTrackFact
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 107
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
  - 1228
  default: 1024
  scaling: 1.0
  implemented: final
overrides: {}
---
# VelTrackFact

Velocity feed-forward (tracking) factor — scales the reference-derived velocity that is added to the position-controller output.

## Overview

`VelTrackFact` is the velocity feed-forward gain of the position loop. It scales the (filtered) derivative of the position reference — the reference velocity [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md) — and adds the result to the position-controller output to build the velocity-loop reference [VelRef](../../10-motion/01-kinematics-status/VelRef.md). This feed-forward lets the velocity loop track the commanded velocity directly, reducing the position error that the proportional position gain would otherwise have to produce during motion.

The factor in use is `VelTrackFact/1024`, so a value of `1024` applies a unity feed-forward (the full reference velocity).

## How it works

`VelTrackFact` scales [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md) and the scaled value is summed with the position-controller output (the [PosGain](../03-position-control/PosGain.md) term) to form [VelRef](../../10-motion/01-kinematics-status/VelRef.md):

$$
VelRef = PosErr \times PosGain + \frac{dPosRef \times VelTrackFact}{1024}
$$

- **What it multiplies:** the filtered reference velocity [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md) (the derivative of the position reference, after the [dPosRefFilt](dPosRefFilt.md) low-pass filter).
- **Where it sums:** the scaled term is added to the position-loop output to form [VelRef](../../10-motion/01-kinematics-status/VelRef.md), before the dual-loop, operation-mode and `MaxVel` stages.
- **Scaling / units:** the effective factor is `VelTrackFact/1024` (so `1024` = ×1.0 = full reference velocity).
- **Range / default:** `0` to `1228`, default `1024` (unity feed-forward). The maximum of `1228` corresponds to about ×1.2.

## Examples

```text
AVelTrackFact=1024  ; unity velocity feed-forward (pass the full reference velocity)
AVelTrackFact=0     ; disable velocity feed-forward
AVelTrackFact       ; read the velocity feed-forward factor
```

### Worked example: contribution at a constant-velocity slew

With `VelTrackFact = 1024` (unity), `PosGain = 400`, and during a constant-velocity slew the filtered reference velocity is `dPosRef = 20000` (user units/s). Suppose the position error has settled to `PosErr = 5`. The velocity-loop reference is:

`VelRef = 5 x 400 + (20000 x 1024) / 1024 = 2000 + 20000 = 22000` (user velocity units)

The feedforward term (`20000`) supplies most of `VelRef`, so the position loop only has to make up `2000` to cover the residual error. Setting `VelTrackFact = 0` would force the position loop to produce the full `22000` from error alone, raising the steady-state following error.

## See also

- [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md) — reference velocity that `VelTrackFact` scales
- [dPosRefFilt](dPosRefFilt.md) — low-pass filter applied to `dPosRef` before this scaling
- [VelRef](../../10-motion/01-kinematics-status/VelRef.md) — velocity-loop reference that the scaled feed-forward joins
- [PosGain](../03-position-control/PosGain.md) — position gain whose output the feed-forward is added to
- [PosKi](../03-position-control/PosKi.md) — position integral whose output joins the same summing point (v5)
- [VelFFW](../05-feedforwards/VelFFW.md) — velocity feed-forward into the current command (the parallel path)
