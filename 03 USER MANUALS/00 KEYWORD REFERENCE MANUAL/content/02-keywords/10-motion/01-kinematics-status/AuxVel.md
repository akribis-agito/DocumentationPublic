---
keyword: AuxVel
summary: Auxiliary-encoder velocity feedback (backward-Euler derivative of AuxPos).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 6
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: aux_user_units
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# AuxVel

Auxiliary-encoder velocity feedback (backward-Euler derivative of AuxPos).

## Overview

`AuxVel` reports the velocity of the auxiliary encoder, computed as the backward-Euler derivative of the auxiliary position feedback [AuxPos](AuxPos.md). It is expressed in auxiliary user units per second (configurable via [AuxUsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md)). It is the auxiliary-loop counterpart of the main velocity feedback [Vel](Vel.md).

## How it works

$$
\text{AuxVel} = \frac{\text{AuxPos}\left(1 - z^{-1}\right)}{T_{s}}
$$

where $T_{s}$ is the controller sampling time. This is implemented as the per-cycle change of [AuxPos](AuxPos.md) scaled by the sample frequency, i.e. `ΔAuxPos × samples-per-second`, which equals `ΔAuxPos / Tₛ`. This is the same single-difference method used for the main `Vel[2]`; there is no moving-average or 1/T variant for the auxiliary encoder.

In **dual-loop** ([DualLoopOn](../../11-control-tuning/02-dual-loop-control/DualLoopOn.md) = 1) `AuxVel` (scaled by [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md)) becomes the velocity-loop feedback [Vel](Vel.md)`[1]`.

### Edge cases

- **Motor off:** `AuxVel` keeps reflecting the auxiliary encoder's per-cycle change; if the auxiliary shaft is back-driven externally, `AuxVel` will be non-zero with the motor off.
- **Simulation mode (`MotorType` = 5):** `AuxPos` is not updated by hardware, so `AuxVel` is zero.
- **ModRev wrap:** [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) acts on [Pos](Pos.md) only — [AuxPos](AuxPos.md) is not wrapped, so `AuxVel` is not subject to a spurious modulo-edge spike. With a rotary aux encoder that itself wraps in hardware, the single-difference derivative will see a one-sample jump at each wrap.
- **Gantry:** `AuxVel` is per-axis (no gantry common/differential combination); each leg's `AuxVel` is independent.
- **Active fault:** `AuxVel` continues to be calculated each cycle; reading it during fault shows whether the load is still moving.

## Examples

```text
AAuxVel             ; read the auxiliary velocity
```

## Changes between versions

In **v5 (central-i)** `AuxVel` is 64-bit; the single-difference derivative is unchanged. The data-type/range difference is shown in the frontmatter. **v5 is central-i only.**

## See also

- [AuxPos](AuxPos.md) — auxiliary position, the source of this derivative
- [Vel](Vel.md) — main velocity feedback array (`Vel[1]` uses `AuxVel` under dual-loop)
- [AuxUsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — auxiliary user-unit scaling
- [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md) — scaling applied when `AuxVel` feeds the velocity loop
