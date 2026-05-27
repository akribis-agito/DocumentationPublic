---
keyword: ECAMStart
summary: GenData index where the ECAM cam pattern starts.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 300
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1000
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ECAMStart

GenData index where the ECAM cam pattern starts.

## Overview

`ECAMStart` defines the [GenData](../../20-arrays/GenData.md) index where the cam pattern starts. It is an array of 10 cam patterns, one element per pattern. It is the lower bound of the overall pattern, paired with the upper bound [ECAMEnd](ECAMEnd.md), while [ECAMStartCyc](ECAMStartCyc.md) and [ECAMEndCyc](ECAMEndCyc.md) bound the repeating segment.

## How it works

`ECAMStart` must satisfy the ordering from which the overall cam pattern is derived:

$$
ECAMStart \leq ECAMStartCyc < ECAMEndCyc \leq ECAMEnd
$$

## Examples

```text
ECAMStart[1]=1      ; cam pattern 1 starts at GenData index 1
ECAMStart[1]?       ; read current value
```

## See also

- [ECAMEnd](ECAMEnd.md) — end index of the overall pattern
- [ECAMStartCyc](ECAMStartCyc.md) / [ECAMEndCyc](ECAMEndCyc.md) — bounds of the repeating segment
- [GenData](../../20-arrays/GenData.md) — array storing the cam pattern
