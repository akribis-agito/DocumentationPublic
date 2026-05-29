# Injection

Agito controller allows injection of common waveform (sine, square, pulse, chirp and pseudorandom binary sequence (PRBS)) at any of the 4 different locations (selectable by [InjectPoint](InjectPoint.md)).

![Where the test signal is injected: a waveform generator produces the selected shape at the amplitude tied to the chosen InjectPoint, and the value is summed onto (additive) or substituted for (direct) one of the position, velocity, current or force loop references](injection-overview.svg)

| InjectPoint | Injection location | Location in block diagram | Amplitude keyword(s) |
|:--:|:--:|:--:|:--:|
| 0 | Current command | see [Control tuning – Current control](../11-control-tuning/06-current-control/00-overview.md) | [InjectCurrAmp](InjectCurrAmp.md), [InjectCurrDC](InjectCurrDC.md) |
| 1 | Velocity command | see [Control tuning – Velocity control](../11-control-tuning/04-velocity-control/00-overview.md) | [InjectVelAmp](InjectVelAmp.md) |
| 2 | Position command | see [Control tuning – Position control](../11-control-tuning/03-position-control/00-overview.md) | [InjectPosAmp](InjectPosAmp.md) |
| 3 | Force command | see [Control tuning – Force control](../06-protections/04-force-control/00-overview.md) | [InjectForceA](InjectForceA.md) |

Depending on selected waveform (defined by [InjectType](InjectType.md)), user is required to configure waveform specific keyword(s).

| Waveform | Waveform-specific keyword(s) |
|:--:|:--:|
| PRBS | [FastIdDownSam](FastIdDownSam.md), [FastIdInit](FastIdInit.md) |
| Sine and square wave | [InjectFreq](InjectFreq.md) |
| Chirp (central-i v5) | [InjectChirpF](InjectChirpF.md) |
| Pulse (current command only) | [InjectTimeOn](InjectTimeOn.md) |

These injections are generally used for system identification, time-domain tuning (step response) and debugging purposes.
