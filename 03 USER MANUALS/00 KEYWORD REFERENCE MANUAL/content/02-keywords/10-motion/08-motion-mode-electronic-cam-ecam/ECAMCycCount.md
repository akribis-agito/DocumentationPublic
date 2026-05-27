---
keyword: ECAMCycCount
summary: Read-only index of the current ECAM cam-pattern repetition cycle.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

## How it works

`ECAMCycCount` is set to `1` when ECAM motion starts ([Begin](../04-motion-command/Begin.md)) for the active pattern ([ECAMTableNum](ECAMTableNum.md)). Each time the master crosses a cycle boundary — moving from the repeating segment of one cycle into the next — the controller steps the count by one in the direction of master travel:

- When the master advances past the end of the current cycle (`ECAMEndCyc` boundary), `ECAMCycCount` increases.
- When the master retreats below the start of the current cycle (`ECAMStartCyc` boundary), `ECAMCycCount` decreases.

The mapping of master *direction* to count direction depends on the sign of [ECAMGap](ECAMGap.md), because a negative gap inverts how the master reading is applied. For bidirectional patterns (`ECAMCycles < 0`) the count can therefore go negative, spanning `-ECAMCycles + 1 … ECAMCycles`; for forward-only patterns (`ECAMCycles > 0`) it spans `1 … ECAMCycles`. In the endless modes the count keeps stepping each time the master window rolls over.

Although the keyword is stored as an array (one count per pattern), only the active pattern's count advances during a move. Its value is not retained in flash, so it resets at each start.

## Examples

```text
AECAMCycCount[1]    ; read the current cycle index for cam pattern 1
```

Refer to the figures in [Motion mode – Electronic cam (ECAM)](00-overview.md) for more information.

## See also

- [ECAMCycles](ECAMCycles.md) — number of pattern occurrences
- [ECAMGap](ECAMGap.md) — its sign sets the increment/decrement direction
- [ECAMTableNum](ECAMTableNum.md) — selects the active cam pattern
