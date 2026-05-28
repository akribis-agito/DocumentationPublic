---
keyword: AInMuteRange
summary: Second analog-input deadband (mV) per input, applied after gain.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# AInMuteRange

Second analog-input deadband (mV) per input, applied after gain.

## Overview

`AInMuteRange` sets the **second** deadband, in millivolts, applied to an analog input — the final stage of the [analog-input signal path](00-overview.md), after the gain ([AInGain](AInGain.md)). Unlike the first deadband ([AInDB](AInDB.md)), values outside the band pass through **unchanged** (no subtraction): it is a pure mute, not a shift. The array index is the analog-input number (e.g. `AInMuteRange[2]` is analog input 2). Because it runs after the gain, the threshold is specified on the output (post-gain) value in mV.

## How it works

The mute is applied to the post-gain value `y`. The comparison is **inclusive** on both edges, so a value exactly equal to the threshold is muted:

| Output `y` | Result |
|------------|--------|
| `−AInMuteRange ≤ y ≤ AInMuteRange` | `0` |
| otherwise | `y` (unchanged) |

This leaves a step discontinuity at the band edge (the value jumps from 0 to ±`AInMuteRange`), in contrast to [AInDB](AInDB.md) which is continuous. The result is what is stored in `AInPort[1]`–`AInPort[4]` and routed to control functions by [AInMode](AInMode.md).

## Examples

```text
AAInMuteRange[1]=10  ; mute analog input 1 within ±10 mV of zero
AAInMuteRange[1]=0   ; no mute (default)
```

## See also

- [AInDB](AInDB.md) — first deadband, before the gain (continuous, subtractive)
- [AInGain](AInGain.md) — gain stage applied before this mute
- [AInPort](AInPort.md) — resulting readings
