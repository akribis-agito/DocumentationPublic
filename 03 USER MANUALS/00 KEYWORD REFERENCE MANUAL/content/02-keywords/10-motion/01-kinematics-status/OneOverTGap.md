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
---
# OneOverTGap

Encoder-counter change (as a power of two) that triggers a 1/T polling save.

## Overview

`OneOverTGap` defines the required change in the hardware encoder counter that triggers saving of the polling counter for the 1/T velocity measurement (`Vel[4]`). It is supported only on non-Central-i products and only when a digital incremental encoder (`EncType = 1`) is used. Use it together with [OneOverTOn](OneOverTOn.md) (enable) and [OneOverTFreq](OneOverTFreq.md) (polling frequency).

## How it works

$$
User\ defined\ gap = 2^{OneOverTGap}\ 
$$

The polling and delta counters reset after the polling counter is saved, ready for the next detection.

> **Note:** A gap of at least 4 (`OneOverTGap` ≥ 2) gives a more accurate velocity reading because it is not affected by the shift between the A and B encoder signals (which is not always exactly 90 degrees).

## Examples

```text
AOneOverTGap=2       ; default: gap = 2^2 = 4 counts
AOneOverTGap        ; read current value
```

## See also

- [Vel](Vel.md) — feedback velocity array (`Vel[4]` is the 1/T method)
- [OneOverTOn](OneOverTOn.md) — enable/disable 1/T velocity measurement
- [OneOverTFreq](OneOverTFreq.md) — polling-frequency down-sampling factor
