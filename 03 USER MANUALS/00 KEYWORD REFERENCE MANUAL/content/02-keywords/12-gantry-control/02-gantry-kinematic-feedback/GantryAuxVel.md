---
summary: Read-only velocity derived from the gantry auxiliary encoder.
keyword: GantryAuxVel
availability:
  standalone: []
  central-i:
  - v5
can_code: 677
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryAuxVel

Read-only velocity derived from the gantry auxiliary encoder.

## Overview

`GantryAuxVel` is a read-only velocity used in **dual-loop gantry control** ([GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) = 1). It is the time-derivative of [GantryAuxFdbk](GantryAuxFdbk.md) — the common-mode (mean) velocity of the two motor encoders. It is axis-scoped, not saved to flash, and reported in user units.

In dual-loop gantry mode the linear position loop follows a load feedback, but the inner velocity loop is still closed on the motor-side velocity for stability; `GantryAuxVel` is that motor-side velocity. The value the velocity loop actually uses is this reading scaled by the dual-loop factor (see the [dual-loop gantry control overview](../04-dual-loop-gantry-control/00-overview.md)). In single-loop gantry mode the velocity loop uses the common-mode velocity directly and this reading is not used.

## How it works

Each control cycle the controller differentiates [GantryAuxFdbk](GantryAuxFdbk.md) (the mean of the two motor-encoder positions, including the captured offset) to produce `GantryAuxVel`. This keeps the inner velocity loop referenced to the motors even when the outer position loop is referenced to the load, which is what makes the dual-loop arrangement stable. The overview table shows the exact unit and scaling for each control structure.

## Examples

```text
AGantryAuxVel      ; read the motor-encoder (auxiliary) gantry velocity in dual-loop mode
```

### Edge cases

- **Single-loop gantry** ([GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) = 0) — not updated. The velocity loop uses [GantryVel](../03-gantry-tuning/GantryVel.md) directly.
- **Gantry off** ([GantryOn](../01-general-variables/GantryOn.md) = 0) — not updated; last value is held until the next gantry-on cycle.
- **At gantry on transition** — forced to `0` on entry while the feedback history primes; first usable derivative appears one cycle later.
- **Motor off** — gantry pair calculation halts; if A and B disagree on motor state the controller forces the still-on member off (`CON_FLT_GANTRY_MEMBER_UNEXPECTED_MOTOR_OFF`).
- **Non-master axis** — reading on any axis other than a gantry master returns `0`.
- **Platform** — v5 central-i only.

## See also

- [GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) — dual-loop mode in which this velocity is used
- [GantryAuxFdbk](GantryAuxFdbk.md) — auxiliary feedback this velocity is derived from
- [GantryFdbkSrc](GantryFdbkSrc.md) — selects the load feedback source for the linear loop
