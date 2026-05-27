---
keyword: OneOverTAuto
summary: Reserved keyword for 1/T velocity measurement (not implemented).
availability:
  standalone:
  - v4
  central-i: []
can_code: 188
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
  implemented: not_implemented
overrides: {}
removed_in:
- v5
---
# OneOverTAuto

Reserved keyword for 1/T velocity measurement (not implemented).

## Overview

`OneOverTAuto` is a reserved keyword in the 1/T velocity-measurement group. It is supported only on non-Central-i products and only when a digital incremental encoder (`EncType = 1`) is used. It relates to the other 1/T configuration keywords [OneOverTOn](OneOverTOn.md), [OneOverTFreq](OneOverTFreq.md) and [OneOverTGap](OneOverTGap.md), which together govern the `Vel[4]` measurement.

> **Documentation pending:** `OneOverTAuto` is currently reserved and not implemented (`implemented: not_implemented`). No functional behaviour is defined.

## See also

- [OneOverTOn](OneOverTOn.md) — enable/disable 1/T velocity measurement
- [OneOverTFreq](OneOverTFreq.md) — polling-frequency down-sampling factor
- [OneOverTGap](OneOverTGap.md) — encoder-counter gap that triggers polling save
- [Vel](Vel.md) — feedback velocity array (`Vel[4]` is the 1/T method)
