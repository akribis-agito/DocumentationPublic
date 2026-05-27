---
keyword: JerkInAcc
summary: Jerk applied during the acceleration phase of a third-order (infinite-snap) profile.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 720
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
  - 100
  - 1000000000
  default: 1000000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    units: user
    range: null
    default: null
    can_code: 565
---
# JerkInAcc

Jerk applied during the acceleration phase of a third-order (infinite-snap) profile.

## Overview

`JerkInAcc` is the jerk constraint applied during the **acceleration** phase of the third-order trajectory profiler, used when [JerkMode](../02-motion-configuration/JerkMode.md) = 1. Unlike the second-order [Jerk](Jerk.md) (a moving-average exponent), `JerkInAcc` is a genuine jerk limit: it bounds how fast the acceleration itself may rise to and fall from the peak [Accel](Accel.md) during a move, rounding the corners of the acceleration ramp. Its deceleration-phase counterpart is [JerkInDec](JerkInDec.md). It is read/write, axis-scoped, saved to flash, and can be changed at any time, including during motion.

This third-order ("infinite-snap") profiler is a structured, segment-based generator built around the double-S velocity profile. `JerkInAcc` is only consulted when `JerkMode = 1`; in the default second-order mode it has no effect.

## How it works

When `JerkMode = 1`, the profiler calls the structured jerk profiler each cycle, passing `JerkInAcc` (and `JerkInDec`) as the jerk constraints alongside the [Speed](Speed.md), [Accel](Accel.md) and [Decel](Decel.md) limits (`AG300_CTL01Profiler.c:1168`–`1170`). The profiler advances through a fixed sequence of segments, and `JerkInAcc` is the magnitude of the jerk applied in the positive- and negative-jerk acceleration segments (`PROFILER_ACC_MAX_J` / `PROFILER_ACC_MIN_J`, `AG300_CTL01Profiler.c:10789`, `:10803`). It shapes the leading half of the move:

| Segment | Jerk used |
|---------|-----------|
| Acceleration, jerk-up (`ACC_MAX_J`) | `+JerkInAcc` — acceleration rises toward `Accel` |
| Acceleration, constant (`ACC_ZERO_J`) | 0 — acceleration held at `Accel` |
| Acceleration, jerk-down (`ACC_MIN_J`) | `−JerkInAcc` — acceleration falls back to 0 at cruise |

A larger `JerkInAcc` makes acceleration reach the `Accel` limit faster (sharper, shorter S transition); a smaller value spreads the transition over more time for gentler motion.

### Units and internal scaling (v4)

On v4 `JerkInAcc` is an integer with a `NO_USER_UNITS` flag and range 100–1,000,000,000 (default 1,000,000). The firmware multiplies the value by `TRUE_JERK_FACTOR` = 1000 before handing it to the profiler (`AG300_CTL01Profiler.c:1168`), so the effective jerk constraint in counts/s³ is:

$$
jerk_{acc} = JerkInAcc \times 1000
$$

### Emergency stops

The third-order profiler is bypassed for emergency/limit stops: those force the internal jerk mode OFF and decelerate with [EmrgDec](EmrgDec.md) without jerk shaping (`AG300_CTL01Profiler.c:1069`), so `JerkInAcc` does not apply to an emergency stop.

## Examples

```text
AJerkInAcc=2000000   ; acceleration-phase jerk (× 1000 internally on v4)
AJerkInAcc           ; read current value
```

`JerkInAcc` only affects motion when [JerkMode](../02-motion-configuration/JerkMode.md) = 1.

## Changes between versions

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Command code | 720 | 565 |
| Data type | 32-bit integer (`glJerkInAcc`) | float (`gfJerkInAcc`) |
| Units | none (`NO_USER_UNITS`), value × 1000 internally | user units (jerk in user units/s³, used directly) |

In **v5** `JerkInAcc` is a floating-point value expressed directly in user jerk units and passed to the same structured profiler without the ×1000 factor (`develop:CommonC/AG300_CTL01Profiler.c:1114`). **v5 is central-i only.**

## See also

- [JerkInDec](JerkInDec.md) — jerk during the deceleration phase
- [Jerk](Jerk.md) — second-order S-curve setting (different mechanism)
- [JerkMode](../02-motion-configuration/JerkMode.md) — must be 1 for `JerkInAcc` to apply
- [Accel](Accel.md) — peak acceleration the jerk ramps to
- [EmrgDec](EmrgDec.md) — emergency stops bypass the jerk profiler
