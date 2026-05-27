---
keyword: ECAMCycCount
summary: Read-only index of the current ECAM cam-pattern repetition cycle.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 307
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ECAMCycCount

Read-only index of the current ECAM cam-pattern repetition cycle.

## Overview

`ECAMCycCount` tracks the index of the cam-pattern repetition cycle during ECAM motion. It is an array of 10 cam patterns, one element per pattern. Its value starts at `1` when ECAM motion begins and increments or decrements according to the master variable and the sign of [ECAMGap](ECAMGap.md). It lets you trace how far ECAM has progressed through the cycles set by [ECAMCycles](ECAMCycles.md).

## Examples

```text
AECAMCycCount[1]    ; read the current cycle index for cam pattern 1
```

Refer to the figures in [Motion mode – Electronic cam (ECAM)](00-overview.md) for more information.

## See also

- [ECAMCycles](ECAMCycles.md) — number of pattern occurrences
- [ECAMGap](ECAMGap.md) — its sign sets the increment/decrement direction
- [ECAMTableNum](ECAMTableNum.md) — selects the active cam pattern
