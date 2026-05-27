---
summary: Initial and final frequencies of the chirp injection, in Hz/100.
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

## Examples

```text
InjectChirpF[1]=100     ; start at 1 Hz
InjectChirpF[2]=20000   ; end at 200 Hz
InjectChirpF[1]?        ; query the initial frequency
```

## See also

- [InjectType](InjectType.md) — selects the chirp waveform and defines the chirp period
- [InjectFreq](InjectFreq.md) — fixed frequency for sine/square injection
- [InjectPoint](InjectPoint.md) — selects the injection location
