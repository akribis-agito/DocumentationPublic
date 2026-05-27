---
keyword: OneOverTOn
summary: Enables or disables the 1/T velocity measurement reported as Vel[4].
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 187
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# OneOverTOn

Enables or disables the 1/T velocity measurement reported as Vel[4].

## Overview

`OneOverTOn` enables (`= 1`) or disables (`= 0`) the 1/T velocity measurement. When disabled, `Vel[4]` reports `0`. It applies when a digital incremental encoder (`EncType = 1`) is used. The measurement is further tuned by [OneOverTFreq](OneOverTFreq.md) (polling frequency) and [OneOverTGap](OneOverTGap.md) (counter gap).

## Examples

```text
AOneOverTOn=1        ; enable 1/T velocity measurement
AOneOverTOn=0        ; disable (Vel[4] reports 0)
```

## See also

- [Vel](Vel.md) — feedback velocity array (`Vel[4]` is the 1/T method)
- [OneOverTFreq](OneOverTFreq.md) — polling-frequency down-sampling factor
- [OneOverTGap](OneOverTGap.md) — encoder-counter gap that triggers polling save
