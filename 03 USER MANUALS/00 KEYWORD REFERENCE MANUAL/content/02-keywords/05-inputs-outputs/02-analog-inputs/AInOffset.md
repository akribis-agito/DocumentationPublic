---
keyword: AInOffset
summary: Offset (mV) added to each analog input.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# AInOffset

Offset (mV) added to each analog input.

## Overview

`AInOffset` adds a fixed offset, in millivolts, to an analog input — the offset stage of the [analog-input signal path](00-overview.md), applied to the filtered ([AInFilt](AInFilt.md)) value and before the first deadband ([AInDB](AInDB.md)). The array index is the analog-input number (e.g. `AInOffset[3]` is analog input 3). Use it to null out a sensor's bias so that 0 mV at the terminal reads as 0.

## How it works

In the per-cycle conditioning code the offset is added to the filtered reading before any deadband or gain (`AG300_CTL01ControlInterrupt.c:11933`):

$$
y = u + AInOffset
$$

Because the offset is added *before* the first deadband, the deadband is applied around the corrected zero, not the raw zero — so nulling a sensor's bias with `AInOffset` also centres the deadband correctly.

## Examples

```text
AAInOffset[1]=-50    ; subtract 50 mV of bias from analog input 1
AAInOffset[1]=0      ; no offset
```

## See also

- [AInFilt](AInFilt.md) — filter stage applied before the offset
- [AInDB](AInDB.md) — first deadband, applied right after the offset
- [AInGain](AInGain.md) — gain stage applied after the deadband
- [AInPort](AInPort.md) — resulting readings
