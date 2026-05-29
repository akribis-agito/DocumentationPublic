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
    range:
    - 100.0
    - 686700000000.0
---
# Decel

Deceleration rate for point-to-point motion, in user units per second squared.

## Overview

`Decel` is the deceleration limit the trajectory profiler uses to ramp the axis down from the commanded [Speed](Speed.md) to rest at the end of a move. It is the counterpart to [Accel](Accel.md) and is also the rate used by a controlled [Stop](../04-motion-command/Stop.md). On a limit switch (RLS/FLS), a software position limit (FwdPLim/RevPLim), or a controlled-stop input, the profiler substitutes the separate, usually larger [EmrgDec](EmrgDec.md) rate. An [Abort](../04-motion-command/Abort.md), by contrast, does **not** use either rate — it instantaneously clears the in-motion bits, leaving the position loop to hold the last reference. Like `Accel`, `Decel` is scaled by [AccelFact](AccelFact.md) and smoothed by [Jerk](Jerk.md) / [JerkInDec](JerkInDec.md) according to [JerkMode](../02-motion-configuration/JerkMode.md).

`Decel` is read/write, axis-scoped and saved to flash. It can be changed at any time, including during motion — the profiler re-reads it every control cycle.

![Velocity profile: trapezoid versus S-curve](velocity-profile.svg)

## How it works

### Effective deceleration each cycle

Each control cycle the profiler forms the effective deceleration as the product of `Decel` and [AccelFact](AccelFact.md):

$$
\text{Decel}_{\text{eff}} = \text{Decel} \cdot \text{AccelFact}
$$

### Deceleration-distance lookahead

`Decel` is the rate the profiler plans its stop with. Every cycle it computes the velocity from which the axis could still come to rest exactly at [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) using `Decel_eff`:

$$
v_{\text{dec}} = -\text{Decel}_{\text{eff}}\,T_s + \sqrt{\text{Decel}_{\text{eff}}^{2}\,T_s^{2} + 2\,\text{Decel}_{\text{eff}}\,(\text{target} - \text{PosRef})\,T_s}
$$

When the rising profiler velocity exceeds this `v_dec`, the profiler clamps to `v_dec` and the motion enters its deceleration phase (the deceleration motion-status bit is set). `Decel` therefore sets the **trailing slope** of the trapezoidal velocity profile. A larger `Decel` lets the axis run at `Speed` longer before braking; a smaller `Decel` starts braking earlier and from a lower velocity.

`Decel` is also used as the brake rate when the profiler velocity has the wrong sign for the requested direction, i.e. when reversing.

### Software-limit braking

In jog/joystick moves the same `Decel`-based lookahead is computed against the software position limits ([FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md)/[RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)) so the axis decelerates to rest at the limit.

### When EmrgDec replaces Decel

When the motion ends because of a limit switch (RLS/FLS), a software position limit ([FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md)/[RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)) or the controlled-stop input, the profiler substitutes [EmrgDec](EmrgDec.md) for `Decel` and disables jerk smoothing (`JerkMode` is forced to `0`) for that stop. A normal [Stop](../04-motion-command/Stop.md) command keeps using `Decel`. [Abort](../04-motion-command/Abort.md) is different again — it does not ramp at all (the in-motion bits are cleared immediately and the position loop holds at the last reference); neither `Decel` nor `EmrgDec` is consulted.

### Third-order mode

In third-order mode ([JerkMode](../02-motion-configuration/JerkMode.md) = 1) `Decel` is the **peak deceleration** constraint passed to the structured jerk profiler; the deceleration is itself ramped at the rate set by [JerkInDec](JerkInDec.md).

### Edge cases

- **Motor off:** the value is held; no profiler computation runs.
- **Out-of-range write:** the parameter system clamps writes to `100`–`2,000,000,000`; values outside are rejected.
- **Simulation mode (`MotorType` = 5):** unchanged; the profiler runs in simulation.
- **ModRev wrap:** unrelated — `Decel` is a kinematic rate, not a position.
- **Active fault:** the axis is disabled and the profiler is stopped; the next `Begin` re-reads `Decel`.
- **Other motion modes:** consumed by jog, PTP, repetitive PTP, PD-indirect, gear-indirect, ECAM-indirect and joystick-indirect modes. Direct modes drive position commands directly and ignore `Decel`, except during a controlled stop.
- **Joystick velocity direct (`MotionMode = 14`):** internally the deceleration is set very high (essentially instant); the user `Decel` is only used during a stop ramp.
- **Cannot be zero:** the minimum is `100` user units/s² to keep the profiler arithmetic finite.

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
