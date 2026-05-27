---
keyword: RecLength
summary: Number of data points captured per parameter per scope (recording period).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 241
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 16500
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecLength

Number of data points captured per parameter per scope (recording period).

## Overview

`RecLength` is an array that defines the number of data points to capture per parameter, thereby determining the period of the recording. Combined with the down-sampling factor [RecGap](RecGap.md), it sets how long a scope records. Each array index selects a scope.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

## How it works

The recording period is:

$$
Period\ of\ recording\ for\ scope\ x\ \lbrack s\rbrack = \frac{RecLength\lbrack x\rbrack \bullet RecGap\lbrack x\rbrack}{Controller\ cycle\ rate\ \lbrack Hz\rbrack}
$$

The maximum value is product-dependent (see the [Data recording](00-overview.md) overview for per-product point limits). [RecTrigPos](RecTrigPos.md) splits these points into pre-trigger and post-trigger portions.

## Examples

```text
ARecLength[1]=16384  ; capture 16384 points per parameter on the first scope
ARecLength[1]       ; query the first scope record length
```

## See also

- [RecGap](RecGap.md) — down-sampling factor (sets the frequency)
- [RecTrigPos](RecTrigPos.md) — pre-trigger fraction of RecLength
- [RecStart](RecStart.md) — start recording once setup is complete
