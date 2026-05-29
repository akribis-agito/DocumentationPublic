---
keyword: GantryOn
summary: Enables gantry MIMO control on the A axis, slaving the A and B axes together.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 650
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryOn

Enables gantry MIMO control on the A axis, slaving the A and B axes together.

## Overview

`GantryOn` controls operation of the gantry mode. With `AGantryOn=0` the gantry mode is disabled and each axis can be moved and controlled independently. With `AGantryOn=1` the gantry mode is enabled and the control scheme is automatically changed to gantry MIMO (multi-input multi-output) control, so that the two parallel drive motors are coordinated as a single mechanism.

When gantry mode is on, motion of the gantry stage is commanded by moving the A axis. The gantry feedbacks reported by [GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md) and the initial offset captured in [GantryOffset](../02-gantry-kinematic-feedback/GantryOffset.md) are referenced to this mode, and the yaw correction set by [GantryYawRef](GantryYawRef.md) is applied while it is active.

`GantryOn` is set on the master (linear) axis, which is the **first axis of each pair**. On v4 (standalone or central-i) only the A–B pair is supported, with A as master and B as yaw. On central-i v5 the pairs A–B, C–D, E–F and G–H can all be gantries, with A, C, E and G as masters and B, D, F and H as their yaw axes. Writing `GantryOn` on a yaw axis (`BGantryOn=1`, etc.) is accepted by the parameter table but has **no effect** — the gantry engine only reads the value stored on the master axis. The two axes of a pair must always be used together. `GantryOn` on the master is automatically cleared to `0` whenever either motor of the pair turns off, so gantry mode is normally enabled only after both motors have been turned on and phased. It is axis-scoped and not saved to flash.

## How it works

### Common-mode and differential-mode control

A gantry has two motors driving the two ends of one beam. Rather than control each motor independently, the controller transforms the two motor measurements into two virtual axes:

- **Common (linear) mode** — the *mean* of the two ends. This is what the stage actually translates, and it is what your A-axis motion commands move. Its feedback is the master value of [GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md).
- **Differential (yaw) mode** — the *difference* between the two ends. This is the skew/squareness of the beam, which you normally want to hold at zero (or at the offset commanded by [GantryYawRef](GantryYawRef.md)). Its feedback is the yaw-axis value of [GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md).

Each virtual axis has its own position and velocity loops (tuned with the `Gantry…` gain keywords). The two loop outputs are then recombined into per-motor current commands — the linear command pushes both motors the same way, while the yaw command pushes them in opposite directions:

![Gantry common-mode and differential-mode control](gantry-common-differential.svg)

This decoupling means a translation command does not induce yaw and a yaw correction does not induce translation. By default the split is symmetric (50/50); on central-i v5 it can be made position-dependent with the gantry decoupling map ([GantryMapType](GantryMapType.md)).

### Engagement and the offset

On the `0`→`1` transition the controller captures the current difference between the two ends as [GantryOffset](../02-gantry-kinematic-feedback/GantryOffset.md) and folds it into the feedbacks so the yaw feedback starts from a clean zero without forcing the beam square. The yaw axis's own reference and reference-filter history are reset to a clean zero in the same cycle, and the master and yaw velocity (and position) integrators are re-shared into common/differential form, so the pair enters MIMO control without a step. Jerk smoothing is then briefly paused while its history refills (see the Smoothing pause edge case below).

### Both motors must stay on

While gantry mode is active, if one motor of the pair turns off the controller deliberately turns off the other as well and records [ConFlt](../../07-status-and-faults/ConFlt.md) fault code **1061** (other gantry member axis got motor off) on the side that was forced down, because a single-sided gantry is not safe to drive. Both motors must also be phased (commutated) for the gantry to remain engaged.

## Examples

```text
AGantryOn=1         ; enable gantry MIMO control (A and B coordinated)
AGantryOn=0         ; disable gantry mode; axes controlled independently
AGantryOn          ; read whether gantry mode is active
```

### Edge cases

- **In motion at write** — rejected (`NOMOTN`). Stop both members first.
- **Out of range** — values outside `0`–`1` are rejected.
- **Either motor off** — the master-axis `GantryOn` is forced to `0` automatically when either member's motor turns off. To re-engage, turn both motors back on, finish their commutation, then write `GantryOn = 1` again.
- **Mid-engage member trip** — if one motor of an engaged pair turns off mid-cycle, the firmware forces the other off and records [ConFlt](../../07-status-and-faults/ConFlt.md) fault code 1061 (other gantry member axis got motor off) on the side that was forced down, then clears the pair's gantry state.
- **Written on yaw axis** — the parameter table accepts the write but the gantry engine only reads the master-axis storage; the write has no functional effect.
- **Pair not commutated** — gantry will not produce useful behaviour if either motor's commutation is not done; check [StatReg](../../07-status-and-faults/StatReg.md) bit 0 on both members.
- **Decoupling map** ([GantryMapType](GantryMapType.md) = 1, v5 only) — at engagement the firmware applies the map ratio to the feedback combination; transient ratio inaccuracy on engagement is smoothed by the gantry-ready-for-smoothing counter.
- **Dual-loop gantry** ([GantryDLoopOn](GantryDLoopOn.md) = 1, v5 only) — at engagement the firmware also computes the dual-loop offset against the load feedback so the linear position does not jump.
- **Smoothing pause** — after every `0 → 1` or `1 → 0` transition the controller temporarily disables jerk smoothing on the pair while the smoothing buffer refills with the new reference; expect a brief tracking blip. The bypass lasts a fixed number of control cycles equal to the jerk-smoothing history length: on central-i this is 8192 cycles (0.5 s at the default 16384 samples/s sampling rate), and on standalone it is 512 cycles (≈31 ms at the same rate). Smoothing resumes automatically once that many cycles have elapsed.
- **Save** — not flash-saveable; comes up `0` at every reset (user must enable after motors are on).
- **Platform** — v4 supports only A–B; v5 central-i supports A–B, C–D, E–F, G–H.

## See also

- [GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md) — MIMO gantry control feedbacks
- [GantryOffset](../02-gantry-kinematic-feedback/GantryOffset.md) — initial A/B offset captured when gantry is switched on
- [GantryYawRef](GantryYawRef.md) — yaw correction reference applied in gantry mode
- [GantryMapType](GantryMapType.md) — position-dependent decoupling map (central-i v5)
- [GantryDLoopOn](GantryDLoopOn.md) — dual-loop gantry (linear loop on load feedback)
- [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) — both motors of the pair must be on to keep gantry mode active
- [ConFlt](../../07-status-and-faults/ConFlt.md) — reports the fault if one gantry motor turns off
