---
summary: Read-only auxiliary-encoder feedback used to measure gantry yaw.
keyword: GantryAuxFdbk
availability:
  standalone: []
  central-i:
  - v5
can_code: 674
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
# GantryAuxFdbk

Read-only auxiliary-encoder feedback used to measure gantry yaw.

## Overview

`GantryAuxFdbk` is a read-only feedback used in **dual-loop gantry control** ([GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) = 1). In that mode the common (linear) position loop is closed on the load feedback selected by [GantryFdbkSrc](GantryFdbkSrc.md), and the two motor encoders are demoted to an *auxiliary* role: their common-mode (mean) position is reported here as `GantryAuxFdbk`. It is the motor-side counterpart to the load-side [GantryFdbk](GantryFdbk.md), and the inner velocity loop is closed on its derivative, [GantryAuxVel](GantryAuxVel.md), scaled by the dual-loop factor. It is axis-scoped, not saved to flash, and reported in user units.

In single-loop gantry mode this value is not used (the motor encoders form the linear feedback directly through [GantryFdbk](GantryFdbk.md)).

## How it works

When dual-loop gantry mode is engaged, the controller computes the same common-mode quantity as the single-loop gantry feedback — the mean of the two motor-encoder positions including the captured [GantryOffset](GantryOffset.md) — but routes it to `GantryAuxFdbk` rather than to the position loop. The position loop then follows the load feedback from [GantryFdbkSrc](GantryFdbkSrc.md). The velocity used by the loop is the time-derivative of this auxiliary feedback, scaled by the dual-loop factor; see the [dual-loop gantry control overview](../04-dual-loop-gantry-control/00-overview.md) for the full sourcing table.

## Examples

```text
AGantryAuxFdbk     ; read the motor-encoder (auxiliary) gantry feedback in dual-loop mode
```

### Edge cases

- **Single-loop gantry** ([GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) = 0) — not updated. The motor-encoder mean is reported directly as [GantryFdbk](GantryFdbk.md) on the master axis.
- **Gantry off** ([GantryOn](../01-general-variables/GantryOn.md) = 0) — not updated. Last value is held until the next gantry-on cycle.
- **Motor off** — the gantry calculation halts for the pair; if A and B disagree on motor state the controller forces the still-on member off and records `CON_FLT_GANTRY_MEMBER_UNEXPECTED_MOTOR_OFF`.
- **Non-master axis** — reading on any axis other than a gantry master returns `0`.
- **Platform** — v5 central-i only; not available on v4 or standalone.

## See also

- [GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) — dual-loop mode in which this feedback is used
- [GantryFdbkSrc](GantryFdbkSrc.md) — load feedback source for the linear loop
- [GantryAuxVel](GantryAuxVel.md) — velocity derived from this feedback
- [GantryFdbk](GantryFdbk.md) — load-side common/differential gantry feedbacks
- [GantryOffset](GantryOffset.md) — A/B offset folded into the common-mode calculation
