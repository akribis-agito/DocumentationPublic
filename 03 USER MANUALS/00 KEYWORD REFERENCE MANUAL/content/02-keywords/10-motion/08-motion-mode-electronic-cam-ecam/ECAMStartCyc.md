---
keyword: ECAMStartCyc
summary: GenData index where the cyclical/repeating ECAM cam pattern starts.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`ECAMStartCyc` and [ECAMEndCyc](ECAMEndCyc.md) bound the repeating segment that is replayed `abs(ECAMCycles)` times (see [ECAMStart](ECAMStart.md) for the leading / repeating / trailing segment model). As the master advances past `ECAMEndCyc`, the controller wraps the master window back by one cycle width, replays the segment from `ECAMStartCyc` again, and steps [ECAMCycCount](ECAMCycCount.md). The master spacing of one cycle equals `abs(ECAMGap) * (ECAMEndCyc - ECAMStartCyc)`.

To keep the follower moving continuously across cycles even when `GenData[ECAMStartCyc]` and `GenData[ECAMEndCyc]` differ, the controller adds the height difference `GenData[ECAMEndCyc] - GenData[ECAMStartCyc]` to an accumulated slave offset on each completed cycle (and subtracts it when stepping backwards). The follower therefore advances by that amount per cycle instead of snapping back to the segment's first value.

If the master jumps by more than one full cycle width in a single control cycle, the controller cannot resolve which cycle it belongs to and faults the axis (motor off).

## Examples

```text
AECAMStartCyc[1]=20  ; repeating segment of cam pattern 1 starts at GenData index 20
AECAMStartCyc[1]    ; read current value
```

## See also

- [ECAMEndCyc](ECAMEndCyc.md) — end index of the repeating segment
- [ECAMStart](ECAMStart.md) / [ECAMEnd](ECAMEnd.md) — bounds of the overall pattern (segment model)
- [ECAMCycles](ECAMCycles.md) — number of times the repeating segment occurs
- [ECAMCycCount](ECAMCycCount.md) — current cycle index, stepped at each wrap
