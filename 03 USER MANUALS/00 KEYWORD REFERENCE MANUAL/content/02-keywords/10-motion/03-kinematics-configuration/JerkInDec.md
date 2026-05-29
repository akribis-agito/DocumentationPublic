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

When `JerkMode = 1`, the profiler uses `JerkInDec` in the structured jerk profiler each cycle. It is the jerk magnitude used in the deceleration segments that bracket a constant-deceleration phase, and it also governs the controlled decel-to-cruise transition when the axis must slow to a lower target speed:

| Segment | Jerk used |
|---------|-----------|
| Deceleration, jerk-up | `−JerkInDec` — deceleration rises toward `Decel` |
| Deceleration, constant | 0 — deceleration held at `Decel` |
| Deceleration, jerk-down | `+JerkInDec` — deceleration falls back to 0 at the target |

A larger `JerkInDec` reaches the `Decel` limit faster (sharper, shorter braking transition); a smaller value spreads it over more time for a gentler stop.

![Third-order velocity and acceleration profile segments](jerkinacc-segments.svg)

### Units and internal scaling (v4)

On v4 `JerkInDec` is a dimensionless integer with range 100–1,000,000,000 (default 1,000,000). The controller multiplies it by a fixed factor of 1000 before use, so the effective jerk constraint in counts/s³ is:

$$
\text{jerk}_{\text{dec}} = \text{JerkInDec} \cdot 1000
$$

### Emergency stops

`JerkInDec` does not shape an emergency stop: limit-switch (RLS/FLS), software-limit and controlled-stop-input halts force the internal jerk mode OFF and brake with [EmrgDec](EmrgDec.md) directly, without jerk limiting. [Abort](../04-motion-command/Abort.md) does not ramp at all and is also unaffected by `JerkInDec`.

### Edge cases

- **Motor off:** value is held; profiler does not run.
- **Out-of-range write:** the parameter system clamps to `100`–`1,000,000,000`; values outside are rejected.
- **Simulation mode (`MotorType` = 5):** unchanged.
- **ModRev wrap:** the third-order profiler tracks the wrap through its internal state; the jerk constraint is unaffected.
- **Active fault:** the axis is disabled; on re-enable and next `Begin`, `JerkInDec` is re-read.
- **Other motion modes:** consumed only by the structured jerk profiler under PTP / repetitive PTP with [JerkMode](../02-motion-configuration/JerkMode.md) = 1. Jog, indirect modes, and direct modes ignore it.
- **Live change in motion:** allowed, but takes effect at the start of the next profiler segment, not mid-segment.

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
| Data type | 32-bit integer | float |
| Units | none, value × 1000 internally | user units (jerk in user units/s³, used directly) |

In **v5** `JerkInDec` is a floating-point value in user jerk units, passed to the same structured profiler without the ×1000 factor. **v5 is central-i only.**

## See also

- [JerkInAcc](JerkInAcc.md) — jerk during the acceleration phase
- [Jerk](Jerk.md) — second-order S-curve setting (different mechanism)
- [JerkMode](../02-motion-configuration/JerkMode.md) — must be 1 for `JerkInDec` to apply
- [Decel](Decel.md) — peak deceleration the jerk ramps to
- [EmrgDec](EmrgDec.md) — emergency stops bypass the jerk profiler
