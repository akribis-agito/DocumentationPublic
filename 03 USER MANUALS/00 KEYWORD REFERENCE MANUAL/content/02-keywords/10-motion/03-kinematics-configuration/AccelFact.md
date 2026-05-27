---
keyword: AccelFact
summary: Scaling factor applied to Accel to adjust effective acceleration without changing Accel.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 168
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
  - 1
  - 40
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# AccelFact

Scaling factor applied to `Accel` to adjust effective acceleration without changing `Accel`.

## Overview

`AccelFact` is an integer multiplier (range 1–40, default 1) applied to **both** [Accel](Accel.md) and [Decel](Decel.md), so the effective acceleration and deceleration used by the profiler are `Accel × AccelFact` and `Decel × AccelFact`. It lets you scale a stored ramp profile up or down by a whole-number ratio without disturbing the stored `Accel`/`Decel` values — handy when one base recipe must be run faster or slower. It is read/write, axis-scoped and saved to flash, and can be changed at any time, including during motion.

## How it works

Every control cycle the profiler multiplies both the acceleration and deceleration rates by `AccelFact` before using them:

$$
Accel_{eff} = Accel \times AccelFact ,\qquad
Decel_{eff} = Decel \times AccelFact
$$

Key behavioral points:

- **Applies to the emergency rate too.** When [EmrgDec](EmrgDec.md) replaces `Decel` on a limit/abort/controlled stop, that value is also multiplied by `AccelFact`, so emergency stops scale with the factor as well.
- **Whole-number only.** `AccelFact` is an integer 1–40. Fractional scaling is not possible — adjust `Accel`/`Decel` directly for finer control.
- **Live.** Because the multiply happens each cycle, changing `AccelFact` mid-move re-scales the ramp slopes on the next cycle.
- **Carries into both profiler orders.** The scaled `Accel_eff`/`Decel_eff` are what the second-order ramp uses directly, and what is passed to the third-order jerk profiler as the peak-acceleration/peak-deceleration constraints.

It is dimensionless (no user-unit scaling) and does **not** scale [Speed](Speed.md) or the jerk settings — only the accel/decel rates.

## Examples

```text
AAccelFact=2         ; double the effective acceleration and deceleration
AAccelFact=1         ; restore base rates (default)
AAccelFact           ; read current factor
```

## See also

- [Accel](Accel.md) — base acceleration this factor multiplies
- [Decel](Decel.md) — base deceleration this factor multiplies
- [EmrgDec](EmrgDec.md) — emergency rate, also scaled by this factor
- [Speed](Speed.md) — cruise velocity (not affected by `AccelFact`)
