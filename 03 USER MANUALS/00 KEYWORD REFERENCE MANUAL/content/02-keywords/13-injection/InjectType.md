---
keyword: InjectType
summary: Selects the injection waveform shape and whether it is direct or additive.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 112
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
  - 7
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectType

Selects the injection waveform shape and whether it is direct or additive.

## Overview

`InjectType` defines both the shape of the injected test waveform and its injection mode (direct or additive). It works together with [InjectPoint](InjectPoint.md), which selects where in the loop the waveform is applied. Depending on the waveform chosen, an additional waveform-specific keyword must be configured: [InjectFreq](InjectFreq.md) for sine/square, [InjectChirpF](InjectChirpF.md) for chirp, [InjectTimeOn](InjectTimeOn.md) for pulse, and [FastIdDownSam](FastIdDownSam.md) / [FastIdInit](FastIdInit.md) for PRBS. The injection amplitude always comes from the amplitude keyword tied to the selected `InjectPoint`.

## How it works

| Value | Waveforms | Injection mode |
|---|---|---|
| 0 | No injection | - |
| 1 | Sinusoid | Direct |
| 2 | Sinusoid | Additive |
| 3 | Square wave | Direct |
| 4 | Square wave | Additive |
| 5 | Pulse (reserved, only for current command injection) | Direct |
| 6 | Pseudorandom binary sequence (PRBS) | Direct |
| 7 | Pseudorandom binary sequence (PRBS) | Additive |
| 8 | Chirp | Direct |
| 9 | Chirp | Additive |

### Waveform descriptions

- **Sinusoid** — Amplitude is set by the amplitude keyword specific to the injection location ([InjectPoint](InjectPoint.md)); frequency is set by [InjectFreq](InjectFreq.md). The phase starts from 0 at the start of injection.
- **Square wave** — Amplitude is set by the amplitude keyword specific to the injection location; frequency is set by [InjectFreq](InjectFreq.md). The initial value is the positive amplitude value.
- **PRBS** — Generation of binary values from a pre-defined random binary sequence (8192 binary values). The sequence repeats once the index reaches the end. The generation rate depends on the controller cycle rate (typically 16.384 kHz) and the down-sampling keyword [FastIdDownSam](FastIdDownSam.md). For example, if `FastIdDownSam = 1`, a new binary value is produced every 2 controller cycles. Injection amplitude is determined by the keyword tied to the injection location.
- **Chirp** — A sinusoidal waveform with increasing frequency. Once the frequency reaches the maximum value, the chirp repeats. The initial and final frequencies are defined by the [InjectChirpF](InjectChirpF.md) array, while the injection amplitude is determined by the keyword tied to the injection location. The period of the chirp is defined as shown.

$$Period\ of\ chirp\ \lbrack s\rbrack = \ 0.5*int\left( \max\left( \frac{1}{16 \bullet T_{s} \bullet f_{final}},1 \right) \right)\ \ $$

For example, a chirp that starts from 1 Hz and ends with 200 Hz has a chirp period of 2.5 s.

### Injection mode

At appropriate injection locations, direct injection is akin to open-loop injection.

| Direct injection (preceding signal is cut-off/ignored) | Additive injection (preceding signal is summed with the injection signal) |
|:--:|:--:|
| <img alt="A white circle with red x and black text AI-generated content may be incorrect." src="image70.png" style="width:2.94528in;height:0.86944in"/> | <img alt="A white circle with a black background AI-generated content may be incorrect." src="image71.png" style="width:2.96944in;height:0.86728in"/> |

## Examples

```text
InjectType=2        ; additive sinusoid injection
InjectType=6        ; direct PRBS injection
InjectType=0        ; disable injection
InjectType?         ; query the current waveform/mode
```

## See also

- [InjectPoint](InjectPoint.md) — selects the injection location in the loop
- [InjectFreq](InjectFreq.md) — frequency for sine/square waveforms
- [InjectChirpF](InjectChirpF.md) — start/end frequencies for chirp
- [InjectTimeOn](InjectTimeOn.md) — pulse duration
- [FastIdDownSam](FastIdDownSam.md) — PRBS generation downsampling factor
- [FastIdInit](FastIdInit.md) — resets the PRBS sequence index
