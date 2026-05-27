---
keyword: ECAMEndCyc
summary: GenData index where the cyclical/repeating ECAM cam pattern ends.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 302
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
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
---
# ECAMEndCyc

GenData index where the cyclical/repeating ECAM cam pattern ends.

## Overview

`ECAMEndCyc` defines the [GenData](../../20-arrays/GenData.md) index where the cyclical/repeating cam pattern ends. It is an array of 10 cam patterns, one element per pattern. It is the upper bound of the repeating segment that is replayed [ECAMCycles](ECAMCycles.md) times, paired with the lower bound [ECAMStartCyc](ECAMStartCyc.md). The overall pattern is bounded by [ECAMStart](ECAMStart.md) and [ECAMEnd](ECAMEnd.md).

## How it works

`ECAMEndCyc` must satisfy the ordering from which the overall cam pattern is derived:

$$
ECAMStart \leq ECAMStartCyc < ECAMEndCyc \leq ECAMEnd
$$

## Examples

```text
AECAMEndCyc[1]=80    ; repeating segment of cam pattern 1 ends at GenData index 80
AECAMEndCyc[1]      ; read current value
```

## See also

- [ECAMStartCyc](ECAMStartCyc.md) — start index of the repeating segment
- [ECAMStart](ECAMStart.md) / [ECAMEnd](ECAMEnd.md) — bounds of the overall pattern
- [ECAMCycles](ECAMCycles.md) — number of times the repeating segment occurs
