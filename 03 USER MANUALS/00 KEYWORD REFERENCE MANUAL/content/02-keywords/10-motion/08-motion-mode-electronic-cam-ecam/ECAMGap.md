---
keyword: ECAMGap
summary: Linear spacing between successive ECAM master values; its sign sets pattern direction.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 304
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
  - -8000000
  - 8000000
  default: 100
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - -2147483647
    - 2147483647
---
# ECAMGap

Linear spacing between successive ECAM master values; its sign sets pattern direction.

## Overview

`ECAMGap` defines the linear interval between master values. It is an array of 10 cam patterns, one element per pattern. Its absolute value is the linear spacing between successive master values that map to successive [GenData](../../20-arrays/GenData.md) indices in the cam look-up table; linear interpolation is used between intervals. Its sign sets the ordering direction of the pattern and the increment/decrement direction of [ECAMCycCount](ECAMCycCount.md).

## How it works

In a simple example where `ECAMCycles = 1`, `ECAMGap = 2000`, `ECAMStart ≤ 400` and `ECAMEnd ≥ 401`: if `GenData[400]` corresponds to a master position of 6554, then `GenData[401]` corresponds to a master position of 8554.

- If `ECAMGap` is positive, the cam pattern follows ascending order: as the master position increases, the corresponding `GenData` index increases.
- If `ECAMGap` is negative, the order is inverted: as the master position increases, the corresponding `GenData` index decreases.

## Examples

```text
AECAMGap[1]=2000     ; master-value spacing for cam pattern 1
AECAMGap[1]         ; read current value
```

Refer to the figures in [Motion mode – Electronic cam (ECAM)](00-overview.md) for more information on the ordering logics.

## See also

- [ECAMCycles](ECAMCycles.md) — number of pattern occurrences (sign also matters)
- [ECAMCycCount](ECAMCycCount.md) — increments/decrements per the sign of `ECAMGap`
- [GenData](../../20-arrays/GenData.md) — array storing the cam pattern
