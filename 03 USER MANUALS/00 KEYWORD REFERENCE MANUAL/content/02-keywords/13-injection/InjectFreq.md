---
keyword: InjectFreq
summary: Frequency of the injected sine or square wave, in Hz/100.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 117
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
  - 800000
  default: 2000
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectFreq

Frequency of the injected sine or square wave, in Hz/100.

## Overview

`InjectFreq` sets the frequency of the injected sine or square wave, expressed in units of Hz/100 (so the stored value is the frequency in Hz multiplied by 100). It applies only when [InjectType](InjectType.md) selects a sine or square waveform (`InjectType = 1, 2, 3 or 4`). The waveform amplitude comes from the amplitude keyword tied to the selected [InjectPoint](InjectPoint.md).

## How it works

The frequency in Hz is `InjectFreq / 100`. For example, an 11.2 Hz wave requires `InjectFreq = 1120`.

## Examples

```text
InjectFreq=1120     ; 11.2 Hz sine/square wave
InjectFreq=200      ; 2 Hz
InjectFreq?         ; query the current injection frequency
```

## See also

- [InjectType](InjectType.md) — selects the sine/square waveform that uses this frequency
- [InjectChirpF](InjectChirpF.md) — start/end frequencies for chirp injection
- [InjectPoint](InjectPoint.md) — selects the injection location
