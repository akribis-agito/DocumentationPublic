---
keyword: ECAMCycles
summary: Number of occurrences of the cyclical ECAM cam pattern (and endless modes).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 305
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
  - -2147483648
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ECAMCycles

Number of occurrences of the cyclical ECAM cam pattern (and endless modes).

## Overview

`ECAMCycles` defines the number of occurrences of the repeating/cyclical cam pattern. It is an array of 10 cam patterns, one element per pattern. Together with the sign of [ECAMGap](ECAMGap.md) it selects the overall ECAM configuration; the current cycle is reported by [ECAMCycCount](ECAMCycCount.md). The repeating segment is bounded by [ECAMStartCyc](ECAMStartCyc.md) and [ECAMEndCyc](ECAMEndCyc.md).

## How it works

| Value | ECAM properties |
|----|----|
| -2147483648 | Endless ECAM without starting nor ending segments |
| 2147483647 | Endless ECAM with only starting segment |
| \> 0 | ECAM with starting and ending segments, as well as ECAMCycles number of occurrences of cyclical patterns. |
| \< 0 | ECAM with starting and ending segments, as well as 2\*ECAMCycles number of occurrences of repeating patterns |

> **Note:** `ECAMCycles` describes the number of occurrences of the same pattern rather than the repetition number. If `ECAMCycles = 1` there is no repetition: `ECAMStartCyc` and `ECAMEndCyc` do not matter because the pattern within that range is already encapsulated by `ECAMStart` and `ECAMEnd`. In summary, `abs(ECAMCycles)` must be more than 1 for repetition.

## Examples

```text
AECAMCycles[1]=3     ; 3 occurrences of the cyclical pattern for cam pattern 1
AECAMCycles[1]      ; read current value
```

Refer to the figures in [Motion mode – Electronic cam (ECAM)](00-overview.md) for more information on the patterning logics.

## See also

- [ECAMCycCount](ECAMCycCount.md) — current cycle index
- [ECAMStartCyc](ECAMStartCyc.md) / [ECAMEndCyc](ECAMEndCyc.md) — bounds of the repeating segment
- [ECAMGap](ECAMGap.md) — interval and ordering of master values
