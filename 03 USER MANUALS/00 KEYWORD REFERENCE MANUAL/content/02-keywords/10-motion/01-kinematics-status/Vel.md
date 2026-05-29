---
keyword: Vel
summary: Feedback-velocity array; each element is a different velocity-estimation method.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 5
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
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
# Vel

Feedback-velocity array; each element is a different velocity-estimation method.

## Overview

`Vel` is an array that reports the feedback velocities, each element using a different velocity-calculation or approximation method (simple derivative, moving average, and the 1/T method — fixed position change over a measurable time).

`Vel[1]` is the velocity-loop feedback in non-gantry mode, so its definition changes with the gantry mode and the dual-loop condition. `Vel[4]` is the 1/T measurement, governed by [OneOverTOn](OneOverTOn.md), [OneOverTFreq](OneOverTFreq.md) and [OneOverTGap](OneOverTGap.md); it reports `0` when 1/T measurement is disabled. The velocity error [VelErr](VelErr.md) is derived from `Vel[1]`.

## How it works

### Array elements

All elements are in main user units per second. The base estimate is the per-cycle position change scaled by the sample frequency, i.e. `ΔPos × samples-per-second`. Because the sample rate is a power of two, this scaling is implemented as a left-shift (by 14 bits at the standalone sample rate, by 16 bits at the fast-sampling rate) rather than a multiply.

| Index | Method |
|-------|--------|
| `Vel[1]` | **Velocity-loop feedback** — the value actually used to close the velocity loop. Selected per loop configuration (see below). |
| `Vel[2]` | Simple backward derivative of the main encoder (`ΔPos × samples-per-second`). |
| `Vel[3]` | Moving average of `Vel[2]` over 32 samples. |
| `Vel[4]` | **1/T measurement** — position change measured over a precisely-timed interval; see [OneOverTOn](OneOverTOn.md). |

`Vel[0]` is not produced by the control cycle. The keyword is read in axis-prefix syntax as `AVel[n]`.

`Vel[3]` is an exact 32-sample sliding-window average of `Vel[2]`, not an exponential filter: each cycle the oldest of 32 stored samples is replaced with the newest and a running sum is divided by 32. At the standalone sample rate the 32-sample window spans about 2 ms; at the fast-sampling rate it spans about 0.5 ms. The window history and running sum are cleared only once, at controller start-up — they are *not* reset on motor-off or on a fault, so `Vel[3]` carries the last samples across those transitions until the window fills again.

### How Vel[1] is selected

`Vel[1]` is the velocity used by the velocity loop, so its meaning follows the dual-loop / gantry configuration. Dual-loop takes precedence; if dual-loop is off, gantry overrides on axes A/B; otherwise `Vel[1]` follows the main-encoder derivative.

| Priority | Configuration | `Vel[1]` source |
|---|---------------|-----------------|
| 1 | Dual-loop ([DualLoopOn](../../11-control-tuning/02-dual-loop-control/DualLoopOn.md) = 1) | [AuxVel](AuxVel.md) $\times \frac{\text{DualLoopFact}}{65536}$ when [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md) $\ge 1$ (`Vel[1]` is in main-encoder units). When `DualLoopFact` $< 1$ the feedback gain is 1.0, so `Vel[1]` stays in auxiliary-encoder units and the velocity-loop *command* ([VelRef](VelRef.md)) is scaled by $\frac{1}{\text{DualLoopFact}/65536}$ instead. |
| 2 | Analog-tacho dual-loop (`DualLoopOn` = 2) | Filtered analog tacho input |
| 3 | Gantry on (axes A/B, no dual-loop) | Gantry velocity ([GantryVel](../../12-gantry-control/03-gantry-tuning/GantryVel.md)) |
| 4 | Normal (no dual-loop, no gantry) | `Vel[2]` — main-encoder derivative |

`Vel[1]` is assigned directly from the selected feedback (it is the raw selected velocity, not separately filtered). The cast is the only post-processing applied; any velocity filtering is done downstream in the velocity controller.

Whether `Vel[1]` (and the velocity reference) is expressed in main-encoder or auxiliary-encoder units depends on [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md): with `DualLoopFact` ≥ 1 the feedback is scaled to main-encoder units; with `DualLoopFact` < 1 the feedback is left in auxiliary-encoder units and the command is scaled instead. Both sides are always brought to the same units.

![Vel[1] feedback selection](vel-feedback-selection.svg)

### 1/T measurement (Vel[4])

`Vel[1]`, `Vel[2]` and `Vel[3]` are computed in the first half of the control sample, *before* the position, velocity, acceleration and current control filters run, because they feed the control loop. `Vel[4]` is computed in the second half of the sample, *after* the control filters, because its 1/T calculation involves a division that is comparatively slow and the result is used only for display and recording, never for control. [OneOverTOn](OneOverTOn.md) gates only whether that division is performed each cycle (to save processing time): when 1/T measurement is off the division is skipped and `Vel[4]` reports `0`.

> **Note:**
>
> 1. Vertical lines denote the controller sampling-time instances.
> 2. The gap is 1 (`OneOverTGap = 0`) and polling frequency is 300 MHz (`OneOverTFreq = 0`).
> 3. `Vel[4] = 0` in the zeroth control cycle/interrupt.
> 4. In between the zeroth and first control interrupts, the hardware records a change of 1 count in 12000 polling cycles and saves this value. On the first control interrupt, the controller reads this value from hardware and calculates `Vel[4]`.
> 5. In between the second and third control interrupts, the hardware updates twice as a 1 position-count change happens twice. The first updated value is 7200 polling counts; the second updated value is 4800 polling counts.

Refer to [Control tuning – Dual-loop control](../../11-control-tuning/02-dual-loop-control/00-overview.md) for more information about the types of dual-loop control.

### Edge cases

- **Motor off:** `Vel[2]` and `Vel[3]` continue updating from the encoder (so back-driving the load while disabled produces a non-zero reading). `Vel[1]` follows the same source as when enabled. `Vel[4]` follows [OneOverTOn](OneOverTOn.md) regardless of motor state.
- **Simulation mode (`MotorType` = 5):** [Pos](Pos.md) tracks [PosRef](PosRef.md), so `Vel[2]/[3]` reflect the *reference* velocity. `Vel[4]` is `0` because there is no hardware to time encoder transitions.
- **ModRev wrap:** the controller subtracts/adds [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) from `Pos` and from `PosPrev` together at the wrap, so `ΔPos` does not see the wrap jump and `Vel[2]/[3]` stay continuous through the wrap.
- **Out-of-range:** `Vel` is read-only; nothing to write. Internally, if `|Vel[1]|` exceeds about 25 percent above [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) the controller raises the "velocity too high" fault (`ConFlt` 1019) and disables the axis; it does not saturate `Vel[1]` or clear a buffer at this threshold.
- **Active fault:** all four array elements continue to update — they are derived from the encoder, not from the control loop, so they remain valid diagnostics after a fault.
- **Gantry:** as noted above, with gantry on `Vel[1]` becomes [GantryVel](../../12-gantry-control/03-gantry-tuning/GantryVel.md) (linear-mode velocity on A, phase velocity on B); `Vel[2]/[3]/[4]` are still per-axis.

## Examples

```text
AVel[1]             ; read the velocity-loop feedback
AVel[4]             ; read the 1/T velocity measurement
```

## Changes between versions

In **v5 (central-i)** the velocity array is 64-bit and `Vel[1]` is selected the same way (main / dual-loop aux / analog tacho / gantry). The data type and range differences are shown in the frontmatter. **v5 is central-i only**, so on standalone `Vel` remains the v4 32-bit array.

## See also

- [VelErr](VelErr.md) — velocity error (`VelRef − Vel[1]`)
- [VelRef](VelRef.md) — velocity-loop reference/input
- [OneOverTOn](OneOverTOn.md) / [OneOverTFreq](OneOverTFreq.md) / [OneOverTGap](OneOverTGap.md) — configure the `Vel[4]` 1/T method
- [DualLoopOn](../../11-control-tuning/02-dual-loop-control/DualLoopOn.md) / [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md) — change what `Vel[1]` measures
- [GantryVel](../../12-gantry-control/03-gantry-tuning/GantryVel.md) — `Vel[1]` source in gantry mode
- [AuxVel](AuxVel.md) — auxiliary velocity (the dual-loop feedback before scaling)
