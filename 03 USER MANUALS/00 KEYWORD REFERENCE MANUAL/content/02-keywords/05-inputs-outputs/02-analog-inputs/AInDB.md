---
keyword: AInDB
summary: First analog-input deadband (mV) per input.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 215
attributes:
  access: rw
  scope: non-axis
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
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
    data_type: float32
    range: null
---
# AInDB

First analog-input deadband (mV) per input.

## Overview

`AInDB` sets the **first** deadband, in millivolts, applied to an analog input — the deadband stage between offset ([AInOffset](AInOffset.md)) and gain ([AInGain](AInGain.md)) in the [analog-input signal path](00-overview.md). The array index is the analog-input number (e.g. `AInDB[3]` is analog input 3). Inputs within the deadband are forced to zero, suppressing noise around 0 mV; outside the band the offset-corrected value is **subtracted by the deadband width** so the output is continuous (no step) at the band edge.

## How it works

The deadband is applied to the offset-corrected value `u`:

| Input `u` | Output |
|-----------|--------|
| `u > AInDB` | `u − AInDB` |
| `u < −AInDB` | `u + AInDB` |
| otherwise (within the band) | `0` |

So the deadband **shifts** the signal rather than clipping it: at exactly the edge the output is 0 and grows linearly outside, giving a continuous characteristic. Because this stage runs before the gain, the deadband width is specified at the input (post-offset) side in mV.

For example, with a 20 mV deadband, the output (mV) as a function of the input (mV) is:

```desmos-graph
left=-120; right=120; bottom=-90; top=90
height=300;
xAxisLabel=Input (mV)
yAxisLabel=Output (mV)
---
y=\{x>20:x-20,x<-20:x+20,0\}|blue
x=20|black|dashed
x=-20|black|dashed

```

## Examples

```text
AAInDB[1]=20         ; ±20 mV deadband on analog input 1
```

### Edge cases

- **Index 0** — invalid; valid indices are `AInDB[1]`–`AInDB[4]`. `AInDB[0]` is the reserved comm/internal slot (not user-accessible) and `AInDB[5]` does not exist.
- **Out of range** — negative values are not accepted (range begins at `0`); a zero `AInDB` disables this stage entirely.
- **At the band edge** — the upper comparison is strict (`u > AInDB`) and the lower strict (`u < −AInDB`), so a value exactly at `±AInDB` is forced to `0` (the band is inclusive on its boundary).
- **Interaction with [AInOffset](AInOffset.md)** — the band is centred on the offset-corrected zero; tune `AInOffset` first to null any DC bias.
- **Interaction with [AInGain](AInGain.md)** — the band width is specified in input (post-offset) mV, before gain; after gain, the equivalent threshold seen on `AInPort` is `AInDB × AInGain / 65536`.
- **Motor on/off and mode independence** — runs every cycle regardless of `MotorOn` or [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md).
- **Save** — `AInDB` is flash-saveable.
- **Platform** — central-i v5 stores the value as `float32`; behaviour is unchanged.

## See also

- [AInMuteRange](AInMuteRange.md) — second deadband (after gain)
- [AInGain](AInGain.md) — gain stage
