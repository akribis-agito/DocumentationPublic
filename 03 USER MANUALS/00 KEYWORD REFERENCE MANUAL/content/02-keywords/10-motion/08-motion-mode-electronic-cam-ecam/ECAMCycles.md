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
| \> 0 | ECAM with starting and ending segments, as well as ECAMCycles occurrences of the cyclical pattern, all to one side of the start position. |
| \< 0 | Bidirectional ECAM with starting and ending segments, and 2\*abs(ECAMCycles) occurrences of the cyclical pattern, half on each side of the start position. |

The sign of `ECAMCycles` sets the layout of the cycles relative to where the master starts (set by [ECAMMasterIni](ECAMMasterIni.md)):

- **Positive `ECAMCycles`** — all cycles lie on one side; the master is expected to move forward from its start position through `ECAMCycles` cycles. [ECAMCycCount](ECAMCycCount.md) runs `1 … ECAMCycles`.
- **Negative `ECAMCycles`** — the cycles are spread symmetrically on both sides of the start position, so the master may move either way. There are `2*abs(ECAMCycles)` cycles in total and `ECAMCycCount` may take negative values, running `-ECAMCycles + 1 … ECAMCycles`.

For the two **endless** sentinel values the controller marks the pattern as endless and, internally, treats it as a 2-cycle (or −2-cycle) pattern whose master window simply rolls over each time it reaches the cycle boundary, so the pattern repeats without a positive (and, for `-2147483648`, also negative) master limit. In endless mode the trailing entries between `ECAMEndCyc` and `ECAMEnd` (and, for `-2147483648`, the leading entries between `ECAMStart` and `ECAMStartCyc`) are ignored. A pending [StopECAM](StopECAM.md) cleanly leaves endless mode (see that page).

> **Note:** `ECAMCycles` describes the number of occurrences of the same pattern rather than the repetition number. If `ECAMCycles = 1` there is no repetition: `ECAMStartCyc` and `ECAMEndCyc` do not matter because the pattern within that range is already encapsulated by `ECAMStart` and `ECAMEnd`. In summary, `abs(ECAMCycles)` must be more than 1 for repetition. `ECAMCycles` may not be `0`; a [Begin](../04-motion-command/Begin.md) with zero cycles is rejected.

## Examples

```text
AECAMCycles[1]=3     ; 3 occurrences of the cyclical pattern for cam pattern 1
AECAMCycles[1]      ; read current value
```

Refer to the figures in [Motion mode – Electronic cam (ECAM)](00-overview.md) for more information on the patterning logics.

## See also

- [ECAMCycCount](ECAMCycCount.md) — current cycle index
- [ECAMStartCyc](ECAMStartCyc.md) / [ECAMEndCyc](ECAMEndCyc.md) — bounds of the repeating segment
- [ECAMMasterIni](ECAMMasterIni.md) — places the start position within the cycle layout
- [ECAMGap](ECAMGap.md) — interval and ordering of master values
- [StopECAM](StopECAM.md) — graceful exit, including from endless mode
