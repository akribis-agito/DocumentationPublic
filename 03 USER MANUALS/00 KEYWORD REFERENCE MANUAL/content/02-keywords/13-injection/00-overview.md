# Injection

Agito controller allows injection of common waveform (sine, square, pulse, chirp and pseudorandom binary sequence (PRBS)) at any of the 4 different locations (selectable by [InjectPoint](../../02-keywords/13-injection/InjectPoint.md)).

| No. | Injection locations | Locations in block diagram | Related keywords |
|:--:|:--:|:--:|:--:|
| 1 | Position command | see [Control tuning – Position control](../../02-keywords/11-control-tuning/03-position-control/00-overview.md) | InjectPosAmp |
| 2 | Velocity command | see [Control tuning – Velocity control](../../02-keywords/11-control-tuning/04-velocity-control/00-overview.md) | InjectVelAmp |
| 3 | Current command | see [Control tuning – Current control](../../02-keywords/11-control-tuning/06-current-control/00-overview.md) | InjectCurrAmp, InjectCurrDC |
| 4 | Force command | see [Control tuning – Force control](../../02-keywords/06-protections/04-force-control/00-overview.md) | InjectForceA |

Depending on selected waveform (defined by [InjectType](../../02-keywords/13-injection/InjectType.md)), user is required to configure waveform specific keyword(s).

| No. |       Waveform       | Waveform specific keywords |
|:---:|:--------------------:|:--------------------------:|
|  1  |         PRBS         | FastIdDownSam, FastIdInit  |
|  2  | Sine and square wave |         InjectFreq         |
|  3  |        Chirp         |        InjectChirpF        |
|  4  |        Pulse         |        InjectTimeOn        |

These injections are generally used for system identification, time-domain tuning (step response) and debugging purposes.
