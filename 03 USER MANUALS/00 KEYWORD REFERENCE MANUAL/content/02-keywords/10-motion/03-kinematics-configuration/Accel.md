---
keyword: Accel
summary: Acceleration rate for point-to-point motion, in user units per second squared.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 136
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
# Accel

Acceleration rate for point-to-point motion, in user units per second squared.

## Overview

`Accel` is the acceleration limit the trajectory profiler stays within when ramping the axis up toward the commanded [Speed](Speed.md). It is one of the four core kinematic limits — `Speed`, `Accel`, [Decel](Decel.md) and the jerk setting — that the profiler shapes a move from. The deceleration side is set separately by `Decel`; the value is scaled by [AccelFact](AccelFact.md); and the abruptness of the start/end of the ramp is governed by [Jerk](Jerk.md) (second-order) or [JerkInAcc](JerkInAcc.md)/[JerkInDec](JerkInDec.md) (third-order), selected by [JerkMode](../02-motion-configuration/JerkMode.md).

`Accel` is read/write, axis-scoped and saved to flash. It can be changed at any time, including during motion — the profiler re-reads it every control cycle, so a new value takes effect on the next cycle.

## How it works

### Effective acceleration each cycle

The profiler runs once per control cycle (16,384 Hz on v4 central-i; sample time ≈ 61 µs). On every cycle it forms the **effective acceleration** as the product of `Accel` and the integer scaling factor [AccelFact](AccelFact.md) (`AG300_CTL01Profiler.c:781`, `:1062`):

$$
Accel_{eff} = Accel \times AccelFact
$$

In a normal acceleration phase the profiler velocity is then incremented by `Accel_eff × SAMPLE_TIME` each cycle until it reaches `Speed` (`AG300_CTL01Profiler.c:1095`):

$$
v_{k} = v_{k-1} + Accel_{eff}\times T_s ,\qquad v_k \le Speed
$$

Because both `Accel` and `AccelFact` are read fresh each cycle, changing either mid-move changes the slope of the velocity ramp immediately.

### Deceleration-distance limiting (the trapezoid)

The profiler does not blindly accelerate to `Speed`. Each cycle it computes, from the remaining distance to [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md), the velocity from which it could still stop in time using `Decel` (`AG300_CTL01Profiler.c:1090`):

$$
v_{dec} = -Decel_{eff}\,T_s + \sqrt{Decel_{eff}^{2}\,T_s^{2} + 2\,Decel_{eff}\,(target - posRef)\,T_s}
$$

`Accel` raises the velocity toward `Speed`; this `v_dec` clamp lowers it as the target nears. The two together produce the classic trapezoidal (or triangular, on a short move) velocity profile. `Accel` therefore sets the **leading slope** of the trapezoid; `Decel` sets the trailing slope.

### Jog and joystick moves

The same `Accel_eff = Accel × AccelFact` construction is used in jog mode and joystick-indirect velocity mode (`AG300_CTL01Profiler.c:781`). Joystick **direct** velocity mode bypasses ramping by forcing the internal accel/decel to a very large value, so `Accel` is not used there except during a stop.

### When Accel is not used

- A controlled stop on a limit switch, software position limit or controlled-stop input substitutes [EmrgDec](EmrgDec.md) for the deceleration rate; `Accel` still governs any re-acceleration.
- In third-order mode ([JerkMode](../02-motion-configuration/JerkMode.md) = 1) `Accel` is the **peak acceleration** constraint passed to the structured jerk profiler (`AG300_CTL01Profiler.c:1170`), which ramps acceleration up to it at the rate set by `JerkInAcc` rather than stepping to it instantly.

### Acceleration shaping

If acceleration shaping is enabled ([AccShapeOn](AccShapeOn.md) ≠ 0) the effective acceleration is additionally multiplied by a position-dependent factor interpolated from the [AccShapeDist](AccShapeDist.md)/[AccShapeFact](AccShapeFact.md) tables (`AG300_CTL01Profiler.c:1056`), so `Accel` becomes the baseline that shaping scales.

## Examples

```text
AAccel=200000        ; set acceleration to 200000 user units/s^2
AAccel               ; read current acceleration
```

## Changes between versions

In **v4** `Accel` is a 32-bit integer (`glAccel`, counts/s²). In **v5 (central-i)** it is a single-precision float (`gfAccel`); the profiler construction `Accel × AccelFact`, the trapezoid limiting and the jerk interactions are otherwise unchanged (`develop:CommonC/AG300_CTL01Profiler.c:810`). **v5 is central-i only** — on standalone `Accel` remains the v4 32-bit value.

## See also

- [Decel](Decel.md) — deceleration rate (trailing slope of the trapezoid)
- [Speed](Speed.md) — cruise velocity the ramp accelerates toward
- [AccelFact](AccelFact.md) — integer multiplier applied to `Accel` each cycle
- [Jerk](Jerk.md) — second-order S-curve smoothing of the ramp
- [JerkInAcc](JerkInAcc.md) — acceleration-phase jerk in third-order mode
- [JerkMode](../02-motion-configuration/JerkMode.md) — selects second- vs third-order profiling
- [EmrgDec](EmrgDec.md) — replaces `Decel` on a controlled/limit stop
- [AccShapeOn](AccShapeOn.md) — position-dependent acceleration shaping
