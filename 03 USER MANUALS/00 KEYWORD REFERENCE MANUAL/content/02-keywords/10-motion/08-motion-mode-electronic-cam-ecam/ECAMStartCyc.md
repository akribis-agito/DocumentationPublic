---
keyword: ECAMStartCyc
summary: GenData index where the cyclical/repeating ECAM cam pattern starts.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 301
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
# ECAMStartCyc

GenData index where the cyclical/repeating ECAM cam pattern starts.

## Overview

`ECAMStartCyc` defines the [GenData](../../20-arrays/GenData.md) index where the cyclical/repeating cam pattern starts. It is an array of 10 cam patterns, one element per pattern. It is the lower bound of the repeating segment that is replayed [ECAMCycles](ECAMCycles.md) times, paired with the upper bound [ECAMEndCyc](ECAMEndCyc.md). The overall pattern is bounded by [ECAMStart](ECAMStart.md) and [ECAMEnd](ECAMEnd.md).

## How it works

`ECAMStartCyc` must satisfy the ordering from which the overall cam pattern is derived:

$$
ECAMStart \leq ECAMStartCyc < ECAMEndCyc \leq ECAMEnd
$$

## Examples

```text
ECAMStartCyc[1]=20  ; repeating segment of cam pattern 1 starts at GenData index 20
ECAMStartCyc[1]?    ; read current value
```

## See also

- [ECAMEndCyc](ECAMEndCyc.md) — end index of the repeating segment
- [ECAMStart](ECAMStart.md) / [ECAMEnd](ECAMEnd.md) — bounds of the overall pattern
- [ECAMCycles](ECAMCycles.md) — number of times the repeating segment occurs
