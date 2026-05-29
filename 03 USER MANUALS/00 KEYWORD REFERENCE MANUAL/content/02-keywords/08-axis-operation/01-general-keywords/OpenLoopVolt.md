---
keyword: OpenLoopVolt
summary: Voltage reference applied to the modulation in voltage open-loop mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 146
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: scaling
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# OpenLoopVolt

Voltage reference applied to the modulation in voltage open-loop mode.

## Overview

`OpenLoopVolt` is the amplitude of the voltage applied to the PWM modulation while the axis is in the voltage open-loop condition. It is only used when [OpenLoopOn](OpenLoopOn.md) = 2, and it bypasses the current control loop entirely.

> **Note:** Please contact Agito for more information if this feature is needed in your application.

## How it works

When [OpenLoopOn](OpenLoopOn.md) = 2 and the motor is on, the controller injects a **sinusoid onto phase A only**, with phases B and C held at zero. The phase advances each cycle at the rate set by [InjectFreq](../../13-injection/InjectFreq.md). Because the current loop is bypassed, this directly excites the motor windings with a known voltage waveform.

The primary use is **motor resistance and inductance (R/L) measurement**: the controller assumes the frequency is high enough that the rotor barely moves and the amplitude is small enough not to draw excessive current. To enforce the latter the value is a PWM scaling (units `scaling`) and is **clamped to a maximum of 20 % PWM**; the minimum is `0`. The frontmatter shows `range: null` because the absolute limit depends on the drive's PWM period.

The value is **forced to 0** whenever `OpenLoopOn ≠ 2` or the motor is disabled, so no residual excitation remains when you leave the mode.

## Examples

```text
AOpenLoopOn=2        ; enter voltage open loop
AOpenLoopVolt=500    ; set the injection amplitude (PWM scaling, capped at 20%)
```

### Edge cases

- **Wrong mode** ([OpenLoopOn](OpenLoopOn.md) ≠ 2) — the value is **forced to `0` every cycle**; the modulator does not use it.
- **Motor off** — the value is forced to `0` every motor-off cycle.
- **In motion at write** — rejected (`NOMOTN`).
- **Above 20 % PWM** — clamped at the 20 % cap; the configured value is stored but the modulator uses the clamp.
- **Negative value** — rejected; the parameter accepts only non-negative amplitudes.
- **Frequency missing** — without [InjectFreq](../../13-injection/InjectFreq.md) set, the injected sinusoid does not advance and the windings see a DC voltage on phase A only.
- **Phase B/C** — held at `0`; the injection is single-phase by design so the motor barely moves.
- **Simulation** — accepted; produces a numerical-only excitation on the simulated phase A.
- **Save** — not flash-saveable; restarts at `0` after reset.
- **Platform** — v5 stores as `float32` and uses the remote PWM scaling factor; v4 stores as `int32`. The 20 % cap is unchanged.

## Changes between versions

In **v5 (central-i)** `OpenLoopVolt` is stored as a 32-bit float rather than the v4 integer, and uses the remote PWM scaling factor; the 20 % PWM cap and the phase-A sinusoid behaviour are unchanged. **v5 is central-i only** — on the standalone product `OpenLoopVolt` remains the v4 integer value.

## See also

- [OpenLoopOn](OpenLoopOn.md) — selects the open-loop point (2 = voltage open loop)
- [OpenLoopCurr](OpenLoopCurr.md) — current reference for current open loop
- [InjectFreq](../../13-injection/InjectFreq.md) — sets the frequency of the injected voltage sinusoid
- [MotorOn](MotorOn.md) — must be on for excitation; disabling forces the amplitude to 0
