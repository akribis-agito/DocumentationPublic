---
keyword: FwdPLim
summary: Forward software travel limit; reference position is capped here.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 83
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 2000000000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# FwdPLim

Forward software travel limit; reference position is capped here.

## Overview

`FwdPLim` is the forward (positive) software travel limit, in counts. It is the upper bound of the legal travel range; `RevPLim` is the lower bound. The reference position is never allowed to pass `FwdPLim` in the forward direction, and a motion that would carry the axis past it is either rejected at `Begin` or decelerated to a stop at the limit.

Unlike the hardware limit switches reported by `LimitsStat` (which are physical inputs), `FwdPLim`/`RevPLim` are firmware-computed boundaries acting on the position reference. The value is held in flash and cannot be changed while the axis is in motion.

## How it works

The profiler enforces the forward limit in several layered ways (firmware `CommonC/AG300_CTL01Profiler.c` and `CommonC/AG300_CTL01Funcs.c`):

**1. Pre-emptive braking (planned stop at the limit).** When a point-to-point / jog profile is running, the profiler continuously computes the maximum velocity from which it could still stop exactly at `FwdPLim` using the active deceleration, via a square-root distance-to-stop formula (`AG300_CTL01Profiler.c:792`):

```text
DecelerationSpeed = -Decel·T + sqrt(Decel²·T² + 2·Decel·(FwdPLim·2^16 - PosRef)·T)
```

If the profiled velocity exceeds `DecelerationSpeed`, it is clamped to it, so the axis ramps down and arrives at `FwdPLim` at zero speed rather than overshooting.

**2. Stop request when the reference crosses the limit.** If the shaped/filtered reference does pass `FwdPLim` while moving forward (`AG300_CTL01Profiler.c:555`), the profiler sets the `IN_STOP_REQUEST` bit in [MotionStat](../../../10-motion/05-motion-status/MotionStat.md) and records `MotionReason = MOTION_REASON_END_FWD_PLIM` (code `7`). When that reason is active, the stop uses the emergency deceleration `EmrgDec` rather than the normal `Decel` (`AG300_CTL01Profiler.c:783`).

**3. Hard clamp of the reference.** In multiple profiler modes the position reference and the absolute target are hard-clamped so they can never exceed `FwdPLim` (e.g. `AG300_CTL01Profiler.c:1007`, `:1196`, `:1317`, `:1604`, `:2015`). The same clamp is also applied inside the control interrupt's PVT/streaming path (`CommonIncludes/AG300_CTL01ControlInterrupt.h:286`).

**4. Begin-time rejection.** A motion cannot be started in the "outside the limits, pointing further out" case: if `PosRef` is already beyond `FwdPLim`/`RevPLim` and the motion mode is not one of the direct/jog modes that can drive back inside, `Begin` returns `CANT_START_MOTION_IF_OUT_OF_POS_LIMITS` (`AG300_CTL01Funcs.c:952`).

| MotionReason | Value | Meaning |
|--------------|-------|---------|
| `MOTION_REASON_END_FWD_PLIM` | 7 | Motion stopped at the forward software limit |
| `MOTION_REASON_END_REV_PLIM` | 6 | Motion stopped at the reverse software limit |

### Data type by version

On central-i v5 the limit is stored as a 64-bit position, extending the usable travel range well beyond the 32-bit range used on standalone/v4 (see the frontmatter `range` override). The braking and clamping logic is otherwise identical.

## Examples

```text
AFwdPLim[1]=1000000    ; forward soft limit (counts)
AFwdPLim[1]            ; read back the forward soft limit
```

## See also

- [RevPLim](RevPLim.md) — reverse software travel limit (lower bound of the same range)
- [LimitsStat](LimitsStat.md) — hardware limit-switch status (physical RLS/FLS inputs)
- [MotionStat](../../../10-motion/05-motion-status/MotionStat.md) — carries the `IN_STOP_REQUEST` bit set when the limit is hit
- [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) — records reason code 7 (`MOTION_REASON_END_FWD_PLIM`) when motion ends here
