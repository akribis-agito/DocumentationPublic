---
keyword: InjectType
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

**Definition:**

InjectType defines the injection waveform and mode.

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

Each waveform shape is described as shown.

**Note:**

Waveform Descriptions Sinusoid The sinusoid amplitude is defined by amplitude keywords specific to the injection location (InjectPoint). Its frequency is defined by InjectFreq. The phase starts from 0 at the start of injection. To illustrate with current command injection, Square wave The square wave amplitude is defined by amplitude keywords specific to the injection location. Its frequency is defined by InjectFreq. The initial value is the positive amplitude value. To illustrate with position command injection, PRBS PRBS is the generation of binary values from a pre-defined random binary sequence (8192 binary values). The sequence repeats once the index reaches the end. The generation rate depends on the controller cycle rate (typically 16.384kHz) and the down-sampling keyword (FastIdDownSam). Injection amplitude is determined by specific keyword tied to the injection location. For example, if FastIdDownSam = 1, new binary value is produced every 2 controller cycles. Chirp Chirp is the sinusoidal waveform with increasing frequency. Once the frequency reaches the maximum value, the chirp repeats. The initial and final frequencies are defined by InjectChirpF array, while the injection amplitude is determined by specific keyword tied to the injection location. The period of the chirp is defined as shown. $$Period\ of\ chirp\ \lbrack s\rbrack = \ 0.5*int\left( \max\left( \frac{1}{16 \bullet T_{s} \bullet f_{final}},1 \right) \right)\ \ $$ For example, the chirp below starts from 1Hz and ends with 200Hz, where chirp period is 2.5s.

The mode of injection is described as shown. At appropriate injection locations, direct injection will be akin to open-loop injection.

| Direct injection (preceding signal is cut-off/ignored) | Additive injection (preceding signal is summed with the injection signal) |
|:--:|:--:|
| <img alt="A white circle with red x and black text AI-generated content may be incorrect." src="image70.png" style="width:2.94528in;height:0.86944in"/> | <img alt="A white circle with a black background AI-generated content may be incorrect." src="image71.png" style="width:2.96944in;height:0.86728in"/> |
