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

Down-sampling exponent for the hardware polling frequency used in Vel[4].

## Overview

`OneOverTFreq` sets the down-sampling factor applied to the hardware polling frequency used in the 1/T velocity measurement reported as `Vel[4]`. It is supported only on non-Central-i products and only when a digital incremental encoder (`EncType = 1`) is used. Use it together with [OneOverTOn](OneOverTOn.md) (enable) and [OneOverTGap](OneOverTGap.md) (counter gap) to tune the 1/T measurement.

## How it works

$$
Polling\ frequency\lbrack Hz\rbrack = \frac{Hardware\ base\ frequency\lbrack Hz\rbrack}{2^{OneOverTFreq}}
$$

A higher `OneOverTFreq` divides the base frequency by a larger power of two, lowering the effective polling frequency.

## Examples

```text
AOneOverTFreq=4      ; default down-sampling exponent
AOneOverTFreq       ; read current value
```

## See also

- [Vel](Vel.md) — feedback velocity array (`Vel[4]` is the 1/T method)
- [OneOverTOn](OneOverTOn.md) — enable/disable 1/T velocity measurement
- [OneOverTGap](OneOverTGap.md) — encoder-counter gap that triggers polling save
