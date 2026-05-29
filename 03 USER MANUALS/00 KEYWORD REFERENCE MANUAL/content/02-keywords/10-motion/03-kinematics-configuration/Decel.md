---
keyword: Decel
summary: Deceleration rate for point-to-point motion, in user units per second squared.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 137
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# Decel

Deceleration rate for point-to-point motion, in user units per second squared.

## Overview

`Decel` is the deceleration limit the trajectory profiler uses to ramp the axis down from the commanded [Speed](Speed.md) to rest at the end of a move. It is the counterpart to [Accel](Accel.md) and is also the rate used by a controlled [Stop](../04-motion-command/Stop.md). For an [Abort](../04-motion-command/Abort.md) or a fault-driven halt the separate, usually larger [EmrgDec](EmrgDec.md) rate is used instead. Like `Accel`, `Decel` is scaled by [AccelFact](AccelFact.md) and smoothed by [Jerk](Jerk.md) / [JerkInDec](JerkInDec.md) according to [JerkMode](../02-motion-configuration/JerkMode.md).

`Decel` is read/write, axis-scoped and saved to flash. It can be changed at any time, including during motion — the profiler re-reads it every control cycle.

![Velocity profile: trapezoid versus S-curve](velocity-profile.svg)

## How it works

### Effective deceleration each cycle

Each control cycle the profiler forms the effective deceleration as the product of `Decel` and [AccelFact](AccelFact.md):

$$
Decel_{eff} = Decel \times AccelFact
$$

### Deceleration-distance lookahead

`Decel` is the rate the profiler plans its stop with. Every cycle it computes the velocity from which the axis could still come to rest exactly at [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) using `Decel_eff`:

$$
v_{dec} = -Decel_{eff}\,T_s + \sqrt{Decel_{eff}^{2}\,T_s^{2} + 2\,Decel_{eff}\,(target - posRef)\,T_s}
$$

When the rising profiler velocity exceeds this `v_dec`, the profiler clamps to `v_dec` and the motion enters its deceleration phase (the deceleration motion-status bit is set). `Decel` therefore sets the **trailing slope** of the trapezoidal velocity profile. A larger `Decel` lets the axis run at `Speed` longer before braking; a smaller `Decel` starts braking earlier and from a lower velocity.

`Decel` is also used as the brake rate when the profiler velocity has the wrong sign for the requested direction, i.e. when reversing.

### Software-limit braking

In jog/joystick moves the same `Decel`-based lookahead is computed against the software position limits ([FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md)/[RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)) so the axis decelerates to rest at the limit.

### When EmrgDec replaces Decel

When the motion ends because of a limit switch, a software position limit, or a controlled-stop input, the profiler substitutes [EmrgDec](EmrgDec.md) for `Decel` and disables jerk smoothing for that stop. A normal [Stop](../04-motion-command/Stop.md) command keeps using `Decel`; only [Abort](../04-motion-command/Abort.md)/fault paths use `EmrgDec`.

### Third-order mode

In third-order mode ([JerkMode](../02-motion-configuration/JerkMode.md) = 1) `Decel` is the **peak deceleration** constraint passed to the structured jerk profiler; the deceleration is itself ramped at the rate set by [JerkInDec](JerkInDec.md).

## Examples

```text
ADecel=200000        ; set deceleration to 200000 user units/s^2
ADecel               ; read current deceleration
```

## Changes between versions

In **v4** `Decel` is a 32-bit integer; in **v5 (central-i)** it is a single-precision float. The lookahead, `AccelFact` scaling, `EmrgDec` substitution and jerk interactions are unchanged. **v5 is central-i only.**

## See also

- [Accel](Accel.md) — acceleration rate (leading slope of the trapezoid)
- [Speed](Speed.md) — cruise velocity the ramp decelerates from
- [AccelFact](AccelFact.md) — integer multiplier applied to `Decel`
- [EmrgDec](EmrgDec.md) — emergency deceleration used on abort/fault/limit stops
- [Jerk](Jerk.md) — second-order S-curve smoothing of the ramp
- [JerkInDec](JerkInDec.md) — deceleration-phase jerk in third-order mode
- [JerkMode](../02-motion-configuration/JerkMode.md) — selects second- vs third-order profiling
- [Stop](../04-motion-command/Stop.md) — controlled stop (uses `Decel`)
- [FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) / [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md) — software limits use the `Decel` lookahead for pre-emptive braking
