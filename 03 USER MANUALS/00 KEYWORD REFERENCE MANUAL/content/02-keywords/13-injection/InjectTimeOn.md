---
keyword: InjectTimeOn
summary: Pulse duration for pulse injection, in milliseconds.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 125
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 65536
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectTimeOn

Pulse duration for pulse injection, in milliseconds.

## Overview

`InjectTimeOn` defines the on-time (duration) of a pulse injection, in milliseconds. It applies only when [InjectType](InjectType.md) selects the pulse waveform (`InjectType = 5`), which is reserved for current-command injection. The pulse amplitude comes from [InjectCurrAmp](InjectCurrAmp.md), and the injection location is set by [InjectPoint](InjectPoint.md).

## Examples

```text
AInjectTimeOn=10     ; 10 ms pulse
AInjectTimeOn       ; query the current pulse duration
```

## See also

- [InjectType](InjectType.md) — selects the pulse waveform (InjectType = 5)
- [InjectCurrAmp](InjectCurrAmp.md) — amplitude of the current pulse
- [InjectPoint](InjectPoint.md) — selects the injection location
