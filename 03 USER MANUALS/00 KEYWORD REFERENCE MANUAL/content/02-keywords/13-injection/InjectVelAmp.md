---
keyword: InjectVelAmp
summary: Amplitude of velocity-command injection; units depend on dual-loop setting.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`InjectVelAmp` is the amplitude of the injected waveform when injecting at the velocity command. It applies only when [InjectPoint](InjectPoint.md) selects the velocity command (`InjectPoint = 1`). The waveform shape is chosen by [InjectType](InjectType.md). The amplitude unit depends on the dual-loop setting; see [Control tuning – Dual-loop control](../../02-keywords/11-control-tuning/02-dual-loop-control/00-overview.md) for more information.

## Examples

```text
AInjectVelAmp=10000      ; velocity injection amplitude (default)
AInjectVelAmp           ; query the current velocity injection amplitude
```

## See also

- [InjectPoint](InjectPoint.md) — must be 1 for velocity-command injection
- [InjectType](InjectType.md) — selects the waveform shape
- [Control tuning – Dual-loop control](../../02-keywords/11-control-tuning/02-dual-loop-control/00-overview.md) — determines the amplitude unit
