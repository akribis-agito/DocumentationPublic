---
keyword: AInFilt
summary: Digital low-pass filter coefficient for each analog input.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 218
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
  - 1
  - 50000
  default: 10000
  scaling: 1.0
  implemented: final
overrides: {}
---
# AInFilt

Digital low-pass filter coefficient for each analog input.

## Overview

`AInFilt` sets the digital low-pass filter coefficient applied to an analog input, the first digital stage of the [analog-input signal path](00-overview.md). The array index is the analog-input number (e.g. `AInFilt[2]` is analog input 2).

## How it works

The filtered output of the current controller cycle ($y_{i}$) depends on the current filter input ($u_{i}$) and the previous filtered output ($y_{i-1}$):

$$
y_{i} = \frac{AInFilt}{65536}u_{i} + \left( 1 - \frac{AInFilt}{65536} \right)y_{i - 1}
$$

To pass the signal through unfiltered ($y_{i} = u_{i}$), set `AInFilt = 65536`.

## Examples

```text
AAInFilt[1]=10000    ; moderate low-pass filtering on analog input 1
AAInFilt[1]=65536    ; no filtering
```

## See also

- [AInPort](AInPort.md) — resulting readings
- [AInOffset](AInOffset.md), [AInGain](AInGain.md) — later stages of the chain
