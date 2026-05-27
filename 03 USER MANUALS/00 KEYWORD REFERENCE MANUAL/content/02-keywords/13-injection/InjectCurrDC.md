---
keyword: InjectCurrDC
summary: DC offset added to current-command injection in direct mode, in mA.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 126
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
  - -32000
  - 32000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# InjectCurrDC

DC offset added to current-command injection in direct mode, in mA.

## Overview

`InjectCurrDC` is the DC offset of the injected current value, in mA. It applies only when [InjectPoint](InjectPoint.md) selects the current command (`InjectPoint = 0`) and [InjectType](InjectType.md) selects a direct injection mode. It shifts the waveform set by [InjectCurrAmp](InjectCurrAmp.md) about a non-zero current level.

## Examples

```text
AInjectCurrDC=500        ; 500 mA DC offset
AInjectCurrDC=0          ; no offset (default)
AInjectCurrDC           ; query the current DC offset
```

## See also

- [InjectPoint](InjectPoint.md) — must be 0 for current-command injection
- [InjectType](InjectType.md) — selects the waveform and direct/additive mode
- [InjectCurrAmp](InjectCurrAmp.md) — amplitude of the current injection
