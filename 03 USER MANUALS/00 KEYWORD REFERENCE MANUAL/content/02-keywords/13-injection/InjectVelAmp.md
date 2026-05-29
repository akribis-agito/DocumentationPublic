---
keyword: InjectVelAmp
summary: Amplitude of velocity-command injection; units depend on dual-loop setting.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 115
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 10000
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectVelAmp

Amplitude of velocity-command injection; units depend on dual-loop setting.

## Overview

`InjectVelAmp` is the amplitude of the injected waveform when injecting at the velocity command. It applies only when [InjectPoint](InjectPoint.md) selects the velocity command (`InjectPoint = 1`). The waveform shape is chosen by [InjectType](InjectType.md). The amplitude unit depends on the dual-loop setting; see [Control tuning – Dual-loop control](../11-control-tuning/02-dual-loop-control/00-overview.md) for more information.

## How it works

This value sets the peak magnitude the waveform reaches at the velocity-loop reference [VelRef](../10-motion/01-kinematics-status/VelRef.md): a sine swings between +`InjectVelAmp` and −`InjectVelAmp`, a square and PRBS toggle between those two levels. The available velocity-command waveforms are sine, square and PRBS in v4; **chirp** is added in v5 (central-i only). In **direct** mode ([InjectType](InjectType.md) = 1, 3 or 6, and 8 in v5) this waveform becomes `VelRef`, replacing the position-loop output; in **additive** mode it is summed onto `VelRef`. The resulting reference is still clamped to the velocity limit ([MaxVel](../06-protections/03-motion/general-maximum-limits/MaxVel.md)) as usual in both versions. The present level can be read back with [InjectedValue](InjectedValue.md).

In **v4 only**, the PRBS waveform at the velocity command additionally adds the [InjectCurrDC](InjectCurrDC.md) offset to the velocity reference (in both direct and additive PRBS modes); v5 applies the PRBS value alone with no DC term.

## Examples

```text
AInjectVelAmp=10000      ; velocity injection amplitude (default)
AInjectVelAmp           ; query the current velocity injection amplitude
```

## See also

- [InjectPoint](InjectPoint.md) — must be 1 for velocity-command injection
- [InjectType](InjectType.md) — selects the waveform shape and direct/additive mode
- [VelRef](../10-motion/01-kinematics-status/VelRef.md) — velocity-loop reference this injection modifies
- [InjectedValue](InjectedValue.md) — reads back the present injection value
- [Control tuning – Dual-loop control](../11-control-tuning/02-dual-loop-control/00-overview.md) — determines the amplitude unit
