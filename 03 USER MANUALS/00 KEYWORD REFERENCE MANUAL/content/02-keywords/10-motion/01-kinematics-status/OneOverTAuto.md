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

`OneOverTAuto` is a reserved keyword in the 1/T velocity-measurement group. It is supported only on standalone products and only when a digital incremental encoder ([EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) `= 1`) is used. It relates to the other 1/T configuration keywords [OneOverTOn](OneOverTOn.md), [OneOverTFreq](OneOverTFreq.md) and [OneOverTGap](OneOverTGap.md), which together govern the [Vel](Vel.md)`[4]` measurement.

> **Documentation pending:** `OneOverTAuto` is reserved and **not implemented** (`implemented: not_implemented`). It is declared and registered as a parameter (`AG300_CTL01Params.c:836`, global `glOneOverTAuto`) with a range of `0`–`1` and default `0`, but no code reads it — writing it has no effect.

## How it works

The keyword has no runtime behaviour today. The firmware records its intended purpose in a comment in the 1/T computation block (`AG300_CTL01ControlInterrupt.c:7622`–`7623`):

> *"OneOverTAuto mode is not implemented at the moment. It shall automatically set OneOverTFreq and OneOverTGap for optimal resolution and no overflows."*

When implemented, `OneOverTAuto = 1` would therefore let the controller choose [OneOverTFreq](OneOverTFreq.md) (the timer-frequency divider) and [OneOverTGap](OneOverTGap.md) (the count gap) automatically — picking the finest resolution that still avoids capture-timer overflow as speed changes — instead of requiring those two values to be set manually. Until then, configure the 1/T measurement with [OneOverTFreq](OneOverTFreq.md) and [OneOverTGap](OneOverTGap.md) directly.

## See also

- [OneOverTOn](OneOverTOn.md) — enable/disable the 1/T velocity calculation
- [OneOverTFreq](OneOverTFreq.md) — 1/T timer-frequency divider (set manually meanwhile)
- [OneOverTGap](OneOverTGap.md) — encoder-count gap per 1/T sample (set manually meanwhile)
- [Vel](Vel.md) — feedback velocity array (`Vel[4]` is the 1/T method)
- [EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) — must be a digital incremental encoder
