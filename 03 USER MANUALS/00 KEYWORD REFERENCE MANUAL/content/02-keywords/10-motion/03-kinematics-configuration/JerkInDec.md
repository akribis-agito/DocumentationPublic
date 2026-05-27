---
keyword: JerkInDec
summary: Jerk applied during the deceleration phase of a third-order (infinite-snap) profile.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 721
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
    can_code: 566
---
# JerkInDec

Jerk applied during the deceleration phase of a third-order (infinite-snap) profile.

## Overview

`JerkInDec` is the jerk constraint applied during the **deceleration** phase of the third-order trajectory profiler, used when [JerkMode](../02-motion-configuration/JerkMode.md) = 1. It is the deceleration-side counterpart of [JerkInAcc](JerkInAcc.md): it bounds how fast the deceleration may rise to and fall from the peak [Decel](Decel.md), rounding the corners of the braking ramp so the axis comes to rest smoothly. It is read/write, axis-scoped, saved to flash, and can be changed at any time, including during motion.

Like `JerkInAcc`, this is a genuine jerk limit (not the moving-average exponent that the second-order [Jerk](Jerk.md) controls), and it is only consulted when `JerkMode = 1`.

## How it works

When `JerkMode = 1`, the profiler passes `JerkInDec` to the structured jerk profiler each cycle (`AG300_CTL01Profiler.c:1169`–`1170`). It is the jerk magnitude used in the deceleration segments that bracket a constant-deceleration phase (`AG300_CTL01Profiler.c:10832`, `:10841`), and it also governs the controlled decel-to-cruise transition when the axis must slow to a lower target speed (`AG300_CTL01Profiler.c:10761`):

| Segment | Jerk used |
|---------|-----------|
| Deceleration, jerk-up (`DEC_MIN_J`) | `−JerkInDec` — deceleration rises toward `Decel` |
| Deceleration, constant (`DEC_ZERO_J`) | 0 — deceleration held at `Decel` |
| Deceleration, jerk-down (`DEC_MAX_J`) | `+JerkInDec` — deceleration falls back to 0 at the target |

A larger `JerkInDec` reaches the `Decel` limit faster (sharper, shorter braking transition); a smaller value spreads it over more time for a gentler stop.

### Units and internal scaling (v4)

On v4 `JerkInDec` is an integer with a `NO_USER_UNITS` flag and range 100–1,000,000,000 (default 1,000,000). The firmware multiplies it by `TRUE_JERK_FACTOR` = 1000 before use (`AG300_CTL01Profiler.c:1169`), so the effective jerk constraint in counts/s³ is:

$$
jerk_{dec} = JerkInDec \times 1000
$$

### Emergency stops

`JerkInDec` does not shape an emergency stop: limit/abort/controlled-stop halts force the internal jerk mode OFF and brake with [EmrgDec](EmrgDec.md) directly, without jerk limiting (`AG300_CTL01Profiler.c:1069`).

## Examples

```text
AJerkInDec=2000000   ; deceleration-phase jerk (× 1000 internally on v4)
AJerkInDec           ; read current value
```

`JerkInDec` only affects motion when [JerkMode](../02-motion-configuration/JerkMode.md) = 1.

## Changes between versions

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Command code | 721 | 566 |
| Data type | 32-bit integer (`glJerkInDec`) | float (`gfJerkInDec`) |
| Units | none (`NO_USER_UNITS`), value × 1000 internally | user units (jerk in user units/s³, used directly) |

In **v5** `JerkInDec` is a floating-point value in user jerk units, passed to the same structured profiler without the ×1000 factor (`develop:CommonC/AG300_CTL01Profiler.c:1114`). **v5 is central-i only.**

## See also

- [JerkInAcc](JerkInAcc.md) — jerk during the acceleration phase
- [Jerk](Jerk.md) — second-order S-curve setting (different mechanism)
- [JerkMode](../02-motion-configuration/JerkMode.md) — must be 1 for `JerkInDec` to apply
- [Decel](Decel.md) — peak deceleration the jerk ramps to
- [EmrgDec](EmrgDec.md) — emergency stops bypass the jerk profiler
