---
keyword: InjectCurrAmp
summary: Amplitude of current-command injection, in mA.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 114
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
  - 64000
  default: 2133
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    default: null
---
# InjectCurrAmp

Amplitude of current-command injection, in mA.

## Overview

`InjectCurrAmp` is the amplitude of the injected waveform when injecting at the current command, in mA. It applies only when [InjectPoint](InjectPoint.md) selects the current command (`InjectPoint = 0`). The waveform shape is chosen by [InjectType](InjectType.md); for direct injection a DC offset can be added with [InjectCurrDC](InjectCurrDC.md).

## Examples

```text
AInjectCurrAmp=2133      ; 2133 mA injection amplitude (default)
AInjectCurrAmp          ; query the current injection amplitude
```

## See also

- [InjectPoint](InjectPoint.md) — must be 0 for current-command injection
- [InjectType](InjectType.md) — selects the waveform shape
- [InjectCurrDC](InjectCurrDC.md) — DC offset for direct current injection
