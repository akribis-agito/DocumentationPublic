---
summary: Initial and final frequencies of the chirp injection, in Hz/100.
keyword: InjectChirpF
availability:
  standalone: []
  central-i:
  - v5
can_code: 716
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 10
  - 100000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectChirpF

Initial and final frequencies of the chirp injection, in Hz/100.

## Overview

`InjectChirpF` is an array defining the start and end frequencies of the chirp signal, expressed in units of Hz/100. It applies only when [InjectType](InjectType.md) selects a chirp waveform (`InjectType = 8 or 9`). The chirp sweeps from the initial to the final frequency and then repeats; the resulting chirp period is derived from the final frequency (see [InjectType](InjectType.md)).

## How it works

| Index | Definition        |
|-------|-------------------|
| 1     | Initial frequency |
| 2     | Final frequency   |

The frequency in Hz is the stored value divided by 100. For example, an initial chirp frequency of 5 Hz requires `InjectChirpF[1] = 500`.

Whenever this array (or [InjectType](InjectType.md)) is written, the controller precomputes the sweep so that the instantaneous frequency rises **linearly** from the initial to the final frequency over one chirp period, then snaps back to the initial frequency and repeats. The chirp period is derived from the final frequency so that each individual sine within the sweep is represented by at least 16 samples (see [InjectType](InjectType.md) for the period formula). Because the sweep is recomputed on write, both array entries should be set before the chirp is started; the final frequency also determines how long the sweep takes.

Both frequencies must lie within the keyword range (0.1 Hz to 1000 Hz, i.e. stored 10 to 100000). The waveform amplitude comes from the amplitude keyword tied to the selected [InjectPoint](InjectPoint.md).

## Examples

```text
AInjectChirpF[1]=100     ; start at 1 Hz
AInjectChirpF[2]=20000   ; end at 200 Hz
AInjectChirpF[1]        ; query the initial frequency
```

## See also

- [InjectType](InjectType.md) — selects the chirp waveform and defines the chirp period
- [InjectFreq](InjectFreq.md) — fixed frequency for sine/square injection
- [InjectPoint](InjectPoint.md) — selects the injection location
