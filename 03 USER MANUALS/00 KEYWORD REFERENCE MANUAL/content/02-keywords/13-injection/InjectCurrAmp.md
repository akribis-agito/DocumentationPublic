---
keyword: InjectCurrAmp
summary: Amplitude of current-command injection, in mA.
availability:
- controller
- ci-master
can_code: 114
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
  - 0
  - 16000
  default: 533.3333333333334
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - 0
    - 64000
    default: 2133.3333333333335
  agc300-et:
    range:
    - 0
    - 4000
    default: 133.33333333333334
  agc301-et:
    range:
    - 0
    - 4000
    default: 133.33333333333334
  agc301-et-bioxtreme:
    range:
    - 0
    - 4000
    default: 133.33333333333334
  agd200-et-2d01:
    range:
    - 0
    - 4000
    default: 133.33333333333334
  agd200-et-2d02:
    range:
    - 0
    - 8000
    default: 266.6666666666667
  agd301-et-2d01:
    range:
    - 0
    - 4000
    default: 133.33333333333334
  agd301-et-2d02:
    range:
    - 0
    - 8000
    default: 266.6666666666667
  agd301-et-2d09:
    range:
    - 0
    - 25500
    default: 850.0
  agd155-af-2a06:
    range:
    - 0
    - 25500
    default: 850.0
  agd155-af-2a10:
    range:
    - 0
    - 28500
    default: 950.0
  agd155-ec:
    range:
    - 0
    - 25500
    default: 850.0
  agd155-ec-var34:
    range:
    - 0
    - 28500
    default: 950.0
  agd155-ec-var34-3:
    range:
    - 0
    - 42500
    default: 1416.6666666666667
  agd156-ec:
    range:
    - 0
    - 12726
    default: 424.2
  agd101-ec-34a:
    range:
    - 0
    - 28280
    default: 942.6666666666666
  agd101-ec-17a:
    range:
    - 0
    - 14140
    default: 471.3333333333333
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# InjectCurrAmp

Amplitude of current-command injection, in mA.

## Overview

`InjectCurrAmp` is the amplitude of the injected waveform when injecting at the current command, in mA. It applies only when [InjectPoint](InjectPoint.md) selects the current command (`InjectPoint = 0`). The waveform shape is chosen by [InjectType](InjectType.md); a DC offset can be added with [InjectCurrDC](InjectCurrDC.md).

## How it works

This value sets the peak magnitude the waveform reaches at the current command: a sine swings between +`InjectCurrAmp` and −`InjectCurrAmp`, a square and PRBS toggle between those two levels, and a pulse holds +`InjectCurrAmp` for the pulse on-time. In **direct** mode ([InjectType](InjectType.md) = 1, 3, 5, 6 or 8) this waveform (plus the [InjectCurrDC](InjectCurrDC.md) offset) becomes the current command, replacing the velocity-loop output; in **additive** mode it is summed onto the existing current command. The present level can be read back with [InjectedValue](InjectedValue.md). The amplitude takes effect on the next injected sample, so it can be changed while injecting.

## Examples

```text
AInjectCurrAmp=2133      ; 2133 mA injection amplitude (default)
AInjectCurrAmp          ; query the current injection amplitude
```

## See also

- [InjectPoint](InjectPoint.md) — must be 0 for current-command injection
- [InjectType](InjectType.md) — selects the waveform shape and direct/additive mode
- [InjectCurrDC](InjectCurrDC.md) — DC offset for current injection
- [InjectedValue](InjectedValue.md) — reads back the present injection value
