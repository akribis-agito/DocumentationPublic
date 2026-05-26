---
keyword: AInDB
summary: First analog-input deadband (mV) per input.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 215
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
# AInDB

First analog-input deadband (mV) per input.

## Overview

`AInDB` sets the **first** deadband, in millivolts, applied to an analog input — the deadband stage between offset and gain in the [analog-input signal path](00-overview.md). The array index is the analog-input number (e.g. `AInDB[3]` is analog input 3). Inputs within the deadband are forced to zero, suppressing noise around 0 mV.

## How it works

| abs(Input) | Output |
|------------|--------|
| ≤ AInDB | 0 |
| > AInDB | Input − Sign(Input)·AInDB |

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
AInDB[1]=20         ; ±20 mV deadband on analog input 1
```

## See also

- [AInMuteRange](AInMuteRange.md) — second deadband (after gain)
- [AInGain](AInGain.md) — gain stage
