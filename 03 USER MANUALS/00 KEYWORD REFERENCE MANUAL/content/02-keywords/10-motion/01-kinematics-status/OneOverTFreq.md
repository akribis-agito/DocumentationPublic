---
keyword: OneOverTFreq
summary: Down-sampling exponent for the hardware polling frequency used in Vel[4].
availability:
  standalone:
  - v4
  central-i: []
can_code: 189
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 7
  default: 4
  scaling: 1.0
  implemented: final
overrides: {}
removed_in:
- v5
---
# OneOverTFreq

Down-sampling exponent for the timer clock used to measure the 1/T period in Vel[4].

## Overview

`OneOverTFreq` sets the exponent of the power-of-two divider applied to the system clock to produce the timer clock that the 1/T unit uses to *time* the gap between encoder events. The 1/T velocity ([Vel](Vel.md)`[4]`) is `counts / time`, so the timer clock frequency sets the **time resolution** of the measurement and the maximum (slowest) period before the timer overflows.

It is supported only on standalone products and only when a digital incremental encoder ([EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) `= 1`) is used. Use it together with [OneOverTOn](OneOverTOn.md) (enable) and [OneOverTGap](OneOverTGap.md) (count gap) to tune the measurement.

The valid range is `0`–`7` (the value is masked to 3 bits and written to the eQEP capture-timer prescaler `QCAPCTL.CCPS`; `SpecialFuncs.c:4110`). The maximum, `7`, is the largest divider the DSP supports (`MAX_ONE_OVER_T_FREQUENCY_DIVIDER`, `AG300_CTL01ParamsCommon.h:1961`). The default is `4`.

## How it works

The system clock is 300 MHz (`SYSTEMCLOCK`, `AG300_CTL01DevInit.h:14`). The 1/T timer clock is:

$$
Timer\ frequency\lbrack Hz\rbrack = \frac{SYSTEMCLOCK}{2^{OneOverTFreq}} = \frac{300\,000\,000}{2^{OneOverTFreq}}
$$

A larger `OneOverTFreq` divides by a larger power of two, lowering the timer frequency. A lower timer frequency coarsens the time resolution but extends the longest period the 16-bit capture register can hold before overflow — so it lets the 1/T unit measure **slower** speeds without overflowing (`AG300_CTL01Params.h:1226`, comment: *"default is 300/16=18.75MHz, so can monitor lower speed with no overflow"*).

`OneOverTFreq` combines with [OneOverTGap](OneOverTGap.md) into a precomputed factor `gfOneOverTFact = 2^OneOverTGap / 2^OneOverTFreq`, calculated once when either keyword is written (`SpecialFuncs.c:4122`). At each control interrupt the velocity is then (`AG300_CTL01ControlInterrupt.c:7685`):

```c
glVel[A_AXIS][4] = ((float)(SYSTEMCLOCK / EQep1Regs.QCPRDLAT)) * gfOneOverTFact[A_AXIS];
```

where `QCPRDLAT` is the latched timer period (in timer ticks) for the most recent gap. The sign is taken from `Vel[2]` because the 1/T unit itself does not sense direction (`:7686`–`7687`). If the capture overflowed or a direction change occurred, `Vel[4]` is forced to `0` (`:7645`–`7656`).

| `OneOverTFreq` | Divider `2^n` | Timer frequency | Tick period |
|----------------|---------------|-----------------|-------------|
| 0 | 1 | 300 MHz | 3.33 ns |
| 1 | 2 | 150 MHz | 6.67 ns |
| 2 | 4 | 75 MHz | 13.3 ns |
| 3 | 8 | 37.5 MHz | 26.7 ns |
| 4 (default) | 16 | 18.75 MHz | 53.3 ns |
| 5 | 32 | 9.375 MHz | 107 ns |
| 6 | 64 | 4.6875 MHz | 213 ns |
| 7 | 128 | 2.34375 MHz | 427 ns |

A higher timer frequency (lower `OneOverTFreq`) gives finer velocity resolution at higher speeds; a lower frequency (higher `OneOverTFreq`) avoids timer overflow at lower speeds. The default of `4` is a balance that favours low-speed monitoring.

## Examples

```text
AOneOverTFreq[1]=4   ; default: 18.75 MHz timer on axis 1
AOneOverTFreq[1]=0   ; full 300 MHz timer (finest resolution, overflows sooner)
AOneOverTFreq[1]     ; read current value
```

## See also

- [Vel](Vel.md) — feedback velocity array (`Vel[4]` is the 1/T method)
- [OneOverTOn](OneOverTOn.md) — enable/disable the 1/T velocity calculation
- [OneOverTGap](OneOverTGap.md) — encoder-count gap measured per 1/T sample
- [OneOverTAuto](OneOverTAuto.md) — reserved auto-tuning of frequency/gap (not implemented)
- [EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) — must be a digital incremental encoder
