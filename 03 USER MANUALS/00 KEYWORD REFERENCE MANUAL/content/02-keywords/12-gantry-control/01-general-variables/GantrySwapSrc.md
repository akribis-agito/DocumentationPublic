---
keyword: GantrySwapSrc
summary: Selects the position source that decides on-the-fly switching between dual-loop and single-loop gantry control.
availability:
  standalone: []
  central-i:
  - v5
can_code: 754
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantrySwapSrc

Selects the position source that decides on-the-fly switching between dual-loop and single-loop gantry control.

## Overview

`GantrySwapSrc` is a pointer that selects which position the controller watches when it switches a **dual-loop gantry** between dual-loop (load-feedback) and single-loop (motor-encoder) control on the fly. The value written is the numeric code of the source variable, using the same numbering scheme as the other gantry source-pointer keywords ([GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md), [GantryMapSrc](GantryMapSrc.md)); the default `0` selects no source.

When the gantry is configured for dual-loop control ([GantryDLoopOn](GantryDLoopOn.md) = 1) and on-the-fly swapping is enabled, the controller reads the live value of this source each cycle and uses it to decide which feedback the linear position loop should close on: inside a configured position window it uses the load (dual-loop) feedback; outside that window it falls back to the motor-encoder (single-loop) feedback. This lets a gantry use a high-accuracy load measurement only over the part of the travel where that measurement is valid, and revert to the motor encoders elsewhere — without a position jump.

It is axis-scoped (configured on the gantry master), saved to flash, and settable with the motor on but not while in motion. Available on central-i (v5).

## How it works

`GantrySwapSrc` is resolved to its target variable's pointer when written, so the controller can read the live source value cheaply each control cycle. While the gantry runs with dual-loop control and on-the-fly swapping active, each cycle the controller compares the source value against a position window:

- **Source value inside the window** — the linear position loop uses the load (dual-loop) feedback selected by [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md); the motor encoders remain the auxiliary/velocity feedback ([GantryAuxFdbk](../02-gantry-kinematic-feedback/GantryAuxFdbk.md) / [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md)).
- **Source value outside the window** — the linear loop falls back to the motor-encoder feedback (single-loop behaviour).

On the transition from single-loop to dual-loop the controller captures an offset between the two feedbacks so the reported linear position does not step at the moment of the swap. The position window itself and the master enable for swapping are configured by the separate dual-encoder swap keywords; `GantrySwapSrc` only chooses *which position* is tested against that window.

## Examples

```text
AGantrySwapSrc=<code>  ; watch a chosen position source for dual/single-loop swapping (use the CAN code of that source)
AGantrySwapSrc        ; read the configured source code
```

### Edge cases

- **In motion at write** — rejected (`NOMOTN`); may be changed with the motor on.
- **Source = 0 (default)** — no source is bound; on-the-fly swapping has nothing to test and the gantry stays in its configured loop mode.
- **Invalid CAN code** — the pointer resolution falls back to a safe zero pointer; the swap window is then evaluated against zero.
- **Swapping not enabled** — `GantrySwapSrc` is stored but has no effect unless dual-loop gantry control and on-the-fly swapping are both enabled.
- **Set on wrong axis** — consulted on the gantry master axis only; writes elsewhere are stored but ignored.
- **Save** — flash-saveable; the pointer is re-resolved at boot.
- **Platform** — v5 central-i only.

## See also

- [GantryDLoopOn](GantryDLoopOn.md) — enables the dual-loop gantry mode this swap operates within
- [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md) — load feedback used inside the swap window
- [GantryAuxFdbk](../02-gantry-kinematic-feedback/GantryAuxFdbk.md) / [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md) — motor-encoder feedback used outside the window
- [GantryOn](GantryOn.md) — enables gantry MIMO control
