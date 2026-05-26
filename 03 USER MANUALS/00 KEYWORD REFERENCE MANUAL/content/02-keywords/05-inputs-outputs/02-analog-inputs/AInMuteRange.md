---
keyword: AInMuteRange
summary: Second analog-input deadband (mV) per input, applied after gain.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 377
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
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AInMuteRange

Second analog-input deadband (mV) per input, applied after gain.

## Overview

`AInMuteRange` sets the **second** deadband, in millivolts, applied to an analog input — the final stage of the [analog-input signal path](00-overview.md), after the gain. Unlike the first deadband ([AInDB](AInDB.md)), values above the threshold pass through unchanged (no subtraction). The array index is the analog-input number (e.g. `AInMuteRange[2]` is analog input 2).

## How it works

| abs(Input) | Output |
|------------|--------|
| ≤ AInMuteRange | 0 |
| > AInMuteRange | Input |

## Examples

```text
AInMuteRange[1]=10  ; mute analog input 1 within ±10 mV of zero
```

## See also

- [AInDB](AInDB.md) — first deadband (before gain)
- [AInPort](AInPort.md) — resulting readings
