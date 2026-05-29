---
keyword: RecLength
summary: Number of data points captured per parameter per scope (recording period).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 241
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 30500
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecLength

Number of data points captured per parameter per scope (recording period).

## Overview

`RecLength` is an array that defines the number of data points to capture per parameter, thereby determining the period of the recording. Combined with the down-sampling factor [RecGap](RecGap.md), it sets how long a scope records. Each array index selects a scope.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

## How it works

The recording period is:

$$
\text{Period of recording for scope } x\ [\text{s}] = \frac{\text{RecLength}[x] \cdot \text{RecGap}[x]}{\text{Controller cycle rate}\ [\text{Hz}]}
$$

`RecLength` sets the points captured *per parameter*. The scope buffer is shared across all recorded channels, so the binding limit is the total sample count: the number of channels selected in [RecParamA/RecParamB](RecParamA-RecParamB.md) multiplied by `RecLength` must fit the buffer. If it does not, [RecStart](RecStart.md) is rejected. Recording more channels therefore reduces the maximum usable `RecLength`. The maximum buffer size is product-dependent (see the [Data recording](00-overview.md) overview for per-product point limits).

[RecTrigPos](RecTrigPos.md) splits these points into pre-trigger and post-trigger portions: the pre-trigger fraction is filled first as a rolling buffer while the scope waits for the trigger, and the remainder is captured after the trigger fires.

Worked example: with `RecLength[1] = 16384` and `RecGap[1] = 1` at a 16384 Hz cycle rate, the recording covers `16384 / 16384 = 1.0` s per parameter. Doubling the down-sampling to `RecGap[1] = 2` doubles the period to 2.0 s for the same point count, at half the time resolution. With 4 channels selected via [RecParamA/RecParamB](RecParamA-RecParamB.md) the buffer must hold `4 x 16384 = 65 536` samples — keep this product within the per-product buffer limit.

## Examples

```text
ARecLength[1]=16384  ; capture 16384 points per parameter on the first scope
ARecLength[1]       ; query the first scope record length
```

## See also

- [RecGap](RecGap.md) — down-sampling factor (sets the frequency)
- [RecTrigPos](RecTrigPos.md) — pre-trigger fraction of RecLength
- [RecStart](RecStart.md) — start recording once setup is complete
