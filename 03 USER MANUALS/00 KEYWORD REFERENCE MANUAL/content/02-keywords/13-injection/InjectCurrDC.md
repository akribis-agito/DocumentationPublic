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

`InjectCurrDC` is the DC offset of the injected current value, in mA. It applies only when [InjectPoint](InjectPoint.md) selects the current command (`InjectPoint = 0`). It shifts the waveform set by [InjectCurrAmp](InjectCurrAmp.md) about a non-zero current level, so the injected current oscillates around the DC offset rather than around zero.

The offset is added to the current command only in **direct** [InjectType](InjectType.md) modes; in additive modes the waveform is summed onto the existing command without the DC offset. The controller applies it only after commutation/phasing of the motor is complete; while the motor is unphased the DC term is suppressed (the waveform is still injected, but without the offset) to avoid an uncontrolled steady current.

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
