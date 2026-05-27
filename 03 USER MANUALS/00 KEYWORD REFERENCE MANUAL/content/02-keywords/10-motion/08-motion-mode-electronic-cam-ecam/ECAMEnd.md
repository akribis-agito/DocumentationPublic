---
keyword: ECAMEnd
summary: GenData index where the ECAM cam pattern ends.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 303
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
# ECAMEnd

GenData index where the ECAM cam pattern ends.

## Overview

`ECAMEnd` defines the [GenData](../../20-arrays/GenData.md) index where the cam pattern ends. It is an array of 10 cam patterns, one element per pattern. It is the upper bound of the overall pattern, paired with the lower bound [ECAMStart](ECAMStart.md), while [ECAMStartCyc](ECAMStartCyc.md) and [ECAMEndCyc](ECAMEndCyc.md) bound the repeating segment.

## How it works

`ECAMEnd` must satisfy the ordering from which the overall cam pattern is derived:

$$
ECAMStart \leq ECAMStartCyc < ECAMEndCyc \leq ECAMEnd
$$

## Examples

```text
AECAMEnd[1]=100      ; cam pattern 1 ends at GenData index 100
AECAMEnd[1]         ; read current value
```

## See also

- [ECAMStart](ECAMStart.md) — start index of the overall pattern
- [ECAMStartCyc](ECAMStartCyc.md) / [ECAMEndCyc](ECAMEndCyc.md) — bounds of the repeating segment
- [GenData](../../20-arrays/GenData.md) — array storing the cam pattern
