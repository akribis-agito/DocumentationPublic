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

![Velocity-vs-position sketch: inside the legal travel band the profiled Vel runs at the commanded value, then the pre-emptive distance-to-stop clamp curves it down to zero exactly at the soft limit; the same shape applies in reverse for RevPLim](soft-limit-decel.svg)

The reverse limit is the mirror image of the forward limit; the same four mechanisms apply:

**1. Pre-emptive braking.** For a negative-direction profile the distance-to-stop velocity is computed against `RevPLim`:

```text
DecelerationSpeed = Decel·T - sqrt(Decel²·T² + 2·Decel·(PosRef - RevPLim))
```

The profiled velocity is clamped to this so the axis arrives at `RevPLim` at zero speed.

**2. Stop request when the reference crosses the limit.** If the shaped/filtered reference passes below `RevPLim` while moving backward, a stop request is raised in [MotionStat](../../../10-motion/05-motion-status/MotionStat.md) and [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) = 6 (motion ended at the reverse software limit) is recorded; the stop then uses `EmrgDec`.

**3. Hard clamp.** The reference and absolute target are clamped to be no lower than `RevPLim` in the profiler modes and in the control-interrupt streaming path.

**4. Begin-time rejection.** A motion is rejected if the position reference is already below `RevPLim` and the motion mode cannot drive back inside (the axis cannot start a motion while outside the position limits).

| MotionReason | Meaning |
|--------------|---------|
| 6 | Motion stopped at the reverse software limit |
| 7 | Motion stopped at the forward software limit |

### Data type by version

On central-i v5 the limit is stored as a 64-bit position, extending the usable travel range beyond the 32-bit range used on standalone/v4 (see the frontmatter `range` override). The braking and clamping logic is otherwise identical.

## Examples

```text
ARevPLim[1]=-1000000    ; reverse soft limit (counts)
ARevPLim[1]             ; read back the reverse soft limit
```

The verification flow is the mirror image of the forward one — see [FwdPLim](FwdPLim.md) **Walk-through: confirm a forward soft-limit trip**, but jog with negative `Speed` and expect `MotionReason = 6`.

## See also

- [FwdPLim](FwdPLim.md) — forward software travel limit (upper bound of the same range; includes the walk-through)
- [LimitsStat](LimitsStat.md) — hardware limit-switch status (physical RLS/FLS inputs)
- [MotionStat](../../../10-motion/05-motion-status/MotionStat.md) — carries the stop-request bit set when the limit is hit
- [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) — records reason code 6 when motion ends here
- [EmrgDec](../../../10-motion/03-kinematics-configuration/EmrgDec.md) — emergency rate used by this stop (not the normal `Decel`)
