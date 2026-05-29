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
\text{Accel}_{\text{eff}} = \text{Accel} \cdot \text{AccelFact} ,\qquad
\text{Decel}_{\text{eff}} = \text{Decel} \cdot \text{AccelFact}
$$

Key behavioral points:

- **Applies to the emergency rate too.** When [EmrgDec](EmrgDec.md) replaces `Decel` on a limit-switch, software-limit or controlled-stop-input halt, that value is also multiplied by `AccelFact`, so emergency stops scale with the factor as well. [Abort](../04-motion-command/Abort.md) does not ramp at all and so is not affected by `AccelFact`.
- **Whole-number only.** `AccelFact` is an integer 1–40. Fractional scaling is not possible — adjust `Accel`/`Decel` directly for finer control.
- **Live.** Because the multiply happens each cycle, changing `AccelFact` mid-move re-scales the ramp slopes on the next cycle.
- **Carries into both profiler orders.** The scaled `Accel_eff`/`Decel_eff` are what the second-order ramp uses directly, and what is passed to the third-order jerk profiler as the peak-acceleration/peak-deceleration constraints.

It is dimensionless (no user-unit scaling) and does **not** scale [Speed](Speed.md) or the jerk settings — only the accel/decel rates.

### Edge cases

- **Motor off:** value is held; no profiler runs.
- **Out-of-range write:** the parameter system clamps to `1`–`40`; values outside are rejected.
- **Simulation mode (`MotorType` = 5):** unchanged.
- **ModRev wrap:** unrelated.
- **Active fault:** the axis is disabled; the next `Begin` re-reads `AccelFact`.
- **Other motion modes:** consumed by all profiler-driven modes (jog/PTP/PD-indirect/gear-indirect/joystick-indirect) and applied to both normal `Decel` and `EmrgDec`. Direct modes ignore `AccelFact` because they do not use `Accel`/`Decel`.
- **`AccelFact = 1`:** the default; rates are used as configured.

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
