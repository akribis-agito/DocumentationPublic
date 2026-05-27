---
summary: Selects the encoder/feedback source for the gantry yaw measurement.
keyword: GantryFdbkSrc
availability:
  standalone: []
  central-i:
  - v5
can_code: 673
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryFdbkSrc

Selects the feedback source used for the common (linear) gantry position in dual-loop gantry mode.

## Overview

`GantryFdbkSrc` is a pointer that selects which feedback variable supplies the common (linear) gantry position when **dual-loop gantry control** is active ([GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) = 1). The value written is the numeric code of the source variable (the same numbering used by other source-pointer keywords); the default `0` leaves no external source selected. It is axis-scoped, saved to flash, and can be set only with the motor off and not in motion.

In ordinary (single-loop) gantry control the position loop is driven from the two main encoders combined into a common-mode feedback (see [GantryFdbk](GantryFdbk.md)). In **dual-loop** gantry control the controller instead closes the linear position loop on the feedback that `GantryFdbkSrc` points to — typically a direct load-side measurement at the moving stage — while still using the two motor encoders for the inner velocity loop and for the yaw (differential) loop. The source selected here is conventionally referred to as the load feedback for the gantry; the two main motor encoders then become the auxiliary feedback reported by [GantryAuxFdbk](GantryAuxFdbk.md), whose derivative is [GantryAuxVel](GantryAuxVel.md). See the [dual-loop gantry control overview](../04-dual-loop-gantry-control/00-overview.md) for how each feedback and velocity term is sourced in the three modes.

## How it works

When dual-loop gantry mode is engaged, the controller resolves `GantryFdbkSrc` to the live value of the chosen variable each control cycle and uses it (offset so the linear position does not jump at the moment of engagement) as the common-mode position feedback for the master axis. The two motor encoders continue to provide the differential (yaw) feedback and the velocity-loop feedback. Because the pointer is resolved when written, change it only while the motor is off.

## Examples

```text
AGantryFdbkSrc=748   ; point the linear loop at a chosen load-side feedback source (code shown is illustrative)
AGantryFdbkSrc       ; read the configured source code
```

## See also

- [GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) — enables the dual-loop mode that uses this source
- [GantryAuxFdbk](GantryAuxFdbk.md) — the motor-encoder feedback in dual-loop mode (derived alongside this source)
- [GantryAuxVel](GantryAuxVel.md) — velocity derived from the auxiliary feedback
- [GantryFdbk](GantryFdbk.md) — common/differential gantry feedbacks
- [GantryOn](../01-general-variables/GantryOn.md) — enables gantry MIMO control
