---
keyword: MapErrOnStep
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 476
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
  - 16384
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
summary: Step size used to apply the map correction when mapping engages.
---
# MapErrOnStep

Step size used to apply the map correction when mapping engages.

## Overview

`MapErrOnStep` controls the **engage/disengage ramp** of the error-mapping correction — how the whole correction (table value plus the [MapErrOffset](MapErrOffset.md) component) fades in when [MapType](MapType.md) becomes non-zero and fades out when it returns to zero. Ramping prevents a position step in the feedback at the moment mapping is switched on or off. It is separate from [MapErrOffRamp](MapErrOffRamp.md), which slews only the offset. The valid range is `0` to `16384`.

It is an axis-scoped parameter saved to flash and can be changed at any time, including during motion.

## How it works

The controller maintains a ramp **counter** that runs from `0` (correction off) up to a full-scale of `16384`. The applied correction is scaled by `counter / 16384`, so the counter is effectively a 0…1 blend factor between the uncorrected feedback and the fully-corrected feedback. `MapErrOnStep` is the amount the counter changes **per control cycle**:

- **Engaging** ([MapType](MapType.md) set 1/2/3): the counter increments by `MapErrOnStep` each cycle until it saturates at full scale.
- **Disengaging** ([MapType](MapType.md) set 0): the counter decrements by `MapErrOnStep` each cycle; when it reaches 0 the internal mapping type reverts to off.
- **`MapErrOnStep = 0` (default):** the counter jumps straight to full scale on engage / to 0 on disengage — an immediate, single-cycle switch (no ramp).

Larger steps engage faster. A step of `N` engages over about `16384 / N` cycles, so `MapErrOnStep = 1` ramps in over `16384` cycles (≈ 1 s at the base sampling rate), while `MapErrOnStep = 16384` ramps in over a single cycle (effectively immediate). Intermediate values give a controlled fade — for example `MapErrOnStep = 16` takes `1024` cycles to fully engage.

## Examples

```text
AMapErrOnStep=0      ; default: switch correction in/out immediately
AMapErrOnStep=16     ; gentle fade-in over ~1024 cycles (~62 ms at 16 kHz)
AMapErrOnStep        ; read the current step size
```

### Edge cases

- **Out of range** — values outside `0`–`16384` are rejected.
- **Zero step** — engage / disengage is immediate (one cycle); the correction can produce a position step in the feedback.
- **In motion** — accepted; the ramp continues to advance during motion, so it is safe to change `MapType` while moving as long as the step is small enough to absorb the correction discontinuity.
- **`MapType = 0` already** — writes are accepted but the ramp counter sits at `0` until `MapType` is set non-zero.
- **Internal state** — the ramp counter and internal map type are shared with [MapErrOffset](MapErrOffset.md) / [MapErrOffRamp](MapErrOffRamp.md); a fast `MapErrOnStep` engage during an active `MapErrOffset` ramp produces a faster-than-expected total change.
- **Fast off/on toggle (mid-ramp re-engage)** — the internal map type only re-arms the engage ramp from zero when it was already fully off. If you set [MapType](MapType.md) = 0 and then back to 1/2/3 *before* the disengage ramp has finished (counter still above 0), the re-write does not reset the counter to 0; engaging simply resumes from the counter's current partial value. The correction therefore re-engages faster than a full ramp and without a position step, because the feedback never had to fully drop the correction in the first place.
- **Save** — flash-saveable.

## See also

- [MapErrOffset](MapErrOffset.md) — constant offset added to the correction
- [MapErrOffRamp](MapErrOffRamp.md) — slew rate of that offset
- [MapType](MapType.md) — enables the error mapping (its change drives this ramp)
- [Pos](../10-motion/01-kinematics-status/Pos.md) — corrected feedback that ramps in/out
