---
keyword: InjectCurrDC
summary: DC offset added to current-command injection in direct mode, in mA.
availability:
- controller
- ci-master
can_code: 126
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -8000.0
  - 8000.0
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - -32000.0
    - 32000.0
  agc300-et:
    range:
    - -2000.0
    - 2000.0
  agc301-et:
    range:
    - -2000.0
    - 2000.0
  agc301-et-bioxtreme:
    range:
    - -2000.0
    - 2000.0
  agd200-et-2d01:
    range:
    - -2000.0
    - 2000.0
  agd200-et-2d02:
    range:
    - -4000.0
    - 4000.0
  agd301-et-2d01:
    range:
    - -2000.0
    - 2000.0
  agd301-et-2d02:
    range:
    - -4000.0
    - 4000.0
  agd301-et-2d09:
    range:
    - -12750.0
    - 12750.0
  agd155-af-2a06:
    range:
    - -12750.0
    - 12750.0
  agd155-af-2a10:
    range:
    - -14250.0
    - 14250.0
  agd155-ec:
    range:
    - -12750.0
    - 12750.0
  agd155-ec-var34:
    range:
    - -14250.0
    - 14250.0
  agd155-ec-var34-3:
    range:
    - -21250.0
    - 21250.0
  agd156-ec:
    range:
    - -6363.0
    - 6363.0
  agd101-ec-34a:
    range:
    - -14140.0
    - 14140.0
  agd101-ec-17a:
    range:
    - -7070.0
    - 7070.0
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# InjectCurrDC

DC offset added to current-command injection in direct mode, in mA.

## Overview

`InjectCurrDC` is the DC offset of the injected current value, in mA. It applies only when [InjectPoint](InjectPoint.md) selects the current command (`InjectPoint = 0`). It shifts the waveform set by [InjectCurrAmp](InjectCurrAmp.md) about a non-zero current level, so the injected current oscillates around the DC offset rather than around zero.

The offset is added to the current command only in **direct** [InjectType](InjectType.md) modes; in additive modes the waveform is summed onto the existing command without the DC offset. The controller applies the DC term only after commutation/phasing of the motor is complete, to avoid an uncontrolled steady current. In v5 the waveform is still injected while the motor is unphased, just without the offset; in v4 current-command injection runs only once the motor is phased, so while it is unphased neither the waveform nor the offset is applied.

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
