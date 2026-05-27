---
keyword: RevPLim
summary: Reverse software travel limit; reference position is capped here.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 82
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
  default: -2000000000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# RevPLim

Reverse software travel limit; reference position is capped here.

## Overview

`RevPLim` is the reverse (negative) software travel limit, in counts. It is the lower bound of the legal travel range; `FwdPLim` is the upper bound. The reference position is never allowed to pass `RevPLim` in the reverse direction, and a motion that would carry the axis past it is either rejected at `Begin` or decelerated to a stop at the limit.

Unlike the hardware limit switches reported by `LimitsStat` (physical inputs), `RevPLim`/`FwdPLim` are firmware-computed boundaries acting on the position reference. The value is held in flash and cannot be changed while the axis is in motion.

## How it works

The reverse limit is the mirror image of the forward limit; the same four mechanisms apply (firmware `CommonC/AG300_CTL01Profiler.c` and `CommonC/AG300_CTL01Funcs.c`):

**1. Pre-emptive braking.** For a negative-direction profile the distance-to-stop velocity is computed against `RevPLim` (`AG300_CTL01Profiler.c:835`):

```text
DecelerationSpeed = Decel·T - sqrt(Decel²·T² + 2·Decel·(PosRef - RevPLim))
```

The profiled velocity is clamped to this so the axis arrives at `RevPLim` at zero speed.

**2. Stop request when the reference crosses the limit.** If the shaped/filtered reference passes below `RevPLim` while moving backward (`AG300_CTL01Profiler.c:563`), the `IN_STOP_REQUEST` bit is set in [MotionStat](../../../10-motion/05-motion-status/MotionStat.md) and `MotionReason = MOTION_REASON_END_REV_PLIM` (code `6`) is recorded; the stop then uses `EmrgDec` (`AG300_CTL01Profiler.c:783`).

**3. Hard clamp.** The reference and absolute target are clamped to be no lower than `RevPLim` in the profiler modes (e.g. `AG300_CTL01Profiler.c:1010`, `:1201`, `:1328`, `:1609`, `:2020`) and in the control-interrupt streaming path (`CommonIncludes/AG300_CTL01ControlInterrupt.h:291`).

**4. Begin-time rejection.** A motion is rejected with `CANT_START_MOTION_IF_OUT_OF_POS_LIMITS` if `PosRef` is already below `RevPLim` and the motion mode cannot drive back inside (`AG300_CTL01Funcs.c:952`).

| MotionReason | Value | Meaning |
|--------------|-------|---------|
| `MOTION_REASON_END_REV_PLIM` | 6 | Motion stopped at the reverse software limit |
| `MOTION_REASON_END_FWD_PLIM` | 7 | Motion stopped at the forward software limit |

### Data type by version

On central-i v5 the limit is stored as a 64-bit position, extending the usable travel range beyond the 32-bit range used on standalone/v4 (see the frontmatter `range` override). The braking and clamping logic is otherwise identical.

## Examples

```text
ARevPLim[1]=-1000000    ; reverse soft limit (counts)
ARevPLim[1]             ; read back the reverse soft limit
```

## See also

- [FwdPLim](FwdPLim.md) — forward software travel limit (upper bound of the same range)
- [LimitsStat](LimitsStat.md) — hardware limit-switch status (physical RLS/FLS inputs)
- [MotionStat](../../../10-motion/05-motion-status/MotionStat.md) — carries the `IN_STOP_REQUEST` bit set when the limit is hit
- [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) — records reason code 6 (`MOTION_REASON_END_REV_PLIM`) when motion ends here
