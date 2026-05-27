---
keyword: OneOverTGap
summary: Encoder-counter change (as a power of two) that triggers a 1/T polling save.
availability:
  standalone:
  - v4
  central-i: []
can_code: 190
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
  - 11
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
removed_in:
- v5
---
# OneOverTGap

Encoder-count change (as a power of two) timed for each 1/T velocity sample.

## Overview

`OneOverTGap` defines the number of encoder counts the 1/T unit accumulates before it latches a measured time, expressed as a power of two: `gap = 2^OneOverTGap` counts. The 1/T velocity ([Vel](Vel.md)`[4]`) is this fixed displacement divided by the time the encoder took to travel it. A larger gap averages over more counts (steadier reading, lower update rate); a smaller gap updates faster but is more sensitive to encoder-edge jitter.

It is supported only on standalone products and only when a digital incremental encoder ([EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) `= 1`) is used. Use it together with [OneOverTOn](OneOverTOn.md) (enable) and [OneOverTFreq](OneOverTFreq.md) (timer frequency).

The valid range is `0`–`11` (the value is masked to 4 bits and written to the eQEP unit-position-event prescaler `QCAPCTL.UPPS`; `SpecialFuncs.c:4111`). The maximum, `11`, is the largest gap the DSP supports (`MAX_ONE_OVER_T_GAP_DIVIDER`, `AG300_CTL01ParamsCommon.h:1962`). The default is `2`.

## How it works

$$
Gap\lbrack counts\rbrack = 2^{OneOverTGap}
$$

The eQEP hardware times the interval over which the encoder advances by `gap` counts, latching the timer period (`QCPRDLAT`) when the gap is reached; the internal counters then reset, ready for the next gap. On each control interrupt the firmware combines the gap and timer frequency into the velocity (`AG300_CTL01ControlInterrupt.c:7663`–`7685`):

$$
Vel\lbrack 4\rbrack = \frac{2^{OneOverTGap}}{2^{OneOverTFreq}} \times \frac{SYSTEMCLOCK}{QCPRDLAT}
$$

The first factor is precomputed once as `gfOneOverTFact = 2^OneOverTGap / 2^OneOverTFreq` whenever `OneOverTGap` or [OneOverTFreq](OneOverTFreq.md) is written (`SpecialFuncs.c:4122`), so the interrupt only does the `SYSTEMCLOCK / QCPRDLAT` division and one multiply.

| `OneOverTGap` | Gap `2^n` (counts) |
|---------------|--------------------|
| 0 | 1 |
| 1 | 2 |
| 2 (default) | 4 |
| 3 | 8 |
| 4 | 16 |
| … | … |
| 11 (max) | 2048 |

> **Note:** A gap of at least 4 (`OneOverTGap` ≥ 2) gives a more accurate velocity reading because it is not affected by the shift between the A and B encoder signals (which is not always exactly 90 degrees). This is why the default is `2` (`AG300_CTL01Params.h:1231`).

## Examples

```text
AOneOverTGap[1]=2    ; default: gap = 2^2 = 4 counts on axis 1
AOneOverTGap[1]=4    ; gap = 16 counts (steadier reading, slower update)
AOneOverTGap[1]      ; read current value
```

## See also

- [Vel](Vel.md) — feedback velocity array (`Vel[4]` is the 1/T method)
- [OneOverTOn](OneOverTOn.md) — enable/disable the 1/T velocity calculation
- [OneOverTFreq](OneOverTFreq.md) — 1/T timer-frequency divider (resolution vs. overflow)
- [OneOverTAuto](OneOverTAuto.md) — reserved auto-tuning of frequency/gap (not implemented)
- [EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) — must be a digital incremental encoder
