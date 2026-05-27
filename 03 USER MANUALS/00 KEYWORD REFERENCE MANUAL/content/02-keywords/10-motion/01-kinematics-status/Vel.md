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

> **Note:**
>
> 1. Vertical lines denote the controller sampling-time instances.
> 2. The gap is 1 (`OneOverTGap = 0`) and polling frequency is 300 MHz (`OneOverTFreq = 0`).
> 3. `Vel[4] = 0` in the zeroth control cycle/interrupt.
> 4. In between the zeroth and first control interrupts, the hardware records a change of 1 count in 12000 polling cycles and saves this value. On the first control interrupt, the controller reads this value from hardware and calculates `Vel[4]`.
> 5. In between the second and third control interrupts, the hardware updates twice as a 1 position-count change happens twice. The first updated value is 7200 polling counts; the second updated value is 4800 polling counts.

Refer to [Control tuning – Dual-loop control](../../11-control-tuning/02-dual-loop-control/00-overview.md) for more information about the types of dual-loop control.

## Examples

```text
AVel[1]             ; read the velocity-loop feedback
AVel[4]             ; read the 1/T velocity measurement
```

## See also

- [VelErr](VelErr.md) — velocity error (`VelRef - Vel[1]`)
- [OneOverTOn](OneOverTOn.md) / [OneOverTFreq](OneOverTFreq.md) / [OneOverTGap](OneOverTGap.md) — configure the `Vel[4]` 1/T method
- [VelRef](VelRef.md) — velocity-loop reference/input
