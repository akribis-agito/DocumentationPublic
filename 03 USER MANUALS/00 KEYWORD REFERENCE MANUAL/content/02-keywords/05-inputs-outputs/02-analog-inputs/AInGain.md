---
keyword: AInGain
summary: DC gain (×65536 fixed-point) applied to each analog input.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 217
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 65536
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# AInGain

DC gain (×65536 fixed-point) applied to each analog input.

## Overview

`AInGain` is the analog-input DC gain, stored as the actual gain multiplied by 65536 so that fractional gains can be represented with an integer. It is the gain stage of the [analog-input signal path](00-overview.md), applied after the first deadband ([AInDB](AInDB.md)) and before the mute range ([AInMuteRange](AInMuteRange.md)). The array index is the analog-input number (e.g. `AInGain[1]` is analog input 1).

## How it works

In the per-cycle conditioning code the deadband output is multiplied by `AInGain` scaled by 1/65536 (`AG300_CTL01ControlInterrupt.c:11944`):

$$
y = \frac{AInGain}{65536}\,u
$$

The scale factor `1/65536` is the constant `DIVIDE_BY_65536`; both input and output are in millivolts. A negative `AInGain` inverts the input. For unity gain, set `AInGain = 65536`.

## Examples

```text
AAInGain[1]=131072   ; gain of 2.0 on analog input 1
AAInGain[1]=65536    ; unity gain
AAInGain[1]=-65536   ; invert analog input 1
```

## See also

- [AInOffset](AInOffset.md) — offset stage (before the first deadband)
- [AInDB](AInDB.md), [AInMuteRange](AInMuteRange.md) — deadbands around the gain stage
- [AInPort](AInPort.md) — resulting readings
