---
keyword: AInOffset
summary: Offset (mV) added to each analog input.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 216
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
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AInOffset

Offset (mV) added to each analog input.

## Overview

`AInOffset` adds a fixed offset, in millivolts, to an analog input — the offset stage of the [analog-input signal path](00-overview.md), applied after digital filtering and before the first deadband. The array index is the analog-input number (e.g. `AInOffset[3]` is analog input 3). Use it to null out a sensor's bias.

## How it works

$$
y = u + AInOffset
$$

## Examples

```text
AAInOffset[1]=-50    ; subtract 50 mV of bias from analog input 1
```

## See also

- [AInGain](AInGain.md) — gain stage applied after the deadband
- [AInPort](AInPort.md) — resulting readings
