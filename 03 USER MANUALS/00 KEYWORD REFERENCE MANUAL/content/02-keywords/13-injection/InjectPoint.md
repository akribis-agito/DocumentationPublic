---
keyword: InjectPoint
summary: Selects which command signal the injected waveform is applied to.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 113
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 3
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectPoint

Selects which command signal the injected waveform is applied to.

## Overview

`InjectPoint` defines the location in the control loop where the test waveform is injected. Injection is used for system identification, step-response tuning, and debugging. The selected point determines which amplitude keyword applies: current command uses [InjectCurrAmp](InjectCurrAmp.md) / [InjectCurrDC](InjectCurrDC.md), velocity command uses [InjectVelAmp](InjectVelAmp.md), position command uses [InjectPosAmp](InjectPosAmp.md), and force command uses [InjectForceA](InjectForceA.md). The waveform itself is selected by [InjectType](InjectType.md).

## How it works

| Value | Injection location | Location in block diagram |
|----|----|----|
| 0 | Current command | see [Control tuning – Current control](../../02-keywords/11-control-tuning/06-current-control/00-overview.md) |
| 1 | Velocity command | see [Control tuning – Velocity control](../../02-keywords/11-control-tuning/04-velocity-control/00-overview.md) |
| 2 | Position command | see [Control tuning – Position control](../../02-keywords/11-control-tuning/03-position-control/00-overview.md) |
| 3 | Force command | see [Control tuning – Force control](../../02-keywords/06-protections/04-force-control/00-overview.md) |

## Examples

```text
AInjectPoint=0       ; inject at the current command
AInjectPoint=2       ; inject at the position command
AInjectPoint        ; query the current injection point
```

## See also

- [InjectType](InjectType.md) — selects the waveform and injection mode
- [InjectCurrAmp](InjectCurrAmp.md) — amplitude for current-command injection (InjectPoint = 0)
- [InjectVelAmp](InjectVelAmp.md) — amplitude for velocity-command injection (InjectPoint = 1)
- [InjectPosAmp](InjectPosAmp.md) — amplitude for position-command injection (InjectPoint = 2)
- [InjectForceA](InjectForceA.md) — amplitude for force-command injection (InjectPoint = 3)
- [InjectedValue](InjectedValue.md) — current injected value
