---
keyword: InjectPosAmp
summary: Amplitude of position-command injection, in main user units.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 116
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
  - 2147483647
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectPosAmp

Amplitude of position-command injection, in main user units.

## Overview

`InjectPosAmp` is the amplitude of the injected waveform when injecting at the position command, expressed in the main user unit (configurable by `UsrUnits`). It applies only when [InjectPoint](InjectPoint.md) selects the position command (`InjectPoint = 2`). The waveform shape is chosen by [InjectType](InjectType.md).

## Examples

```text
InjectPosAmp=100        ; position injection amplitude (default)
InjectPosAmp?           ; query the current position injection amplitude
```

## See also

- [InjectPoint](InjectPoint.md) — must be 2 for position-command injection
- [InjectType](InjectType.md) — selects the waveform shape
