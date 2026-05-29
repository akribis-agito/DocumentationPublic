---
keyword: ECAMEnd
summary: GenData index where the ECAM cam pattern ends.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
\text{ECAMStart} \leq \text{ECAMStartCyc} < \text{ECAMEndCyc} \leq \text{ECAMEnd}
$$

`ECAMEnd` is the last entry of the pattern, terminating the trailing one-shot segment that runs from `ECAMEndCyc` to `ECAMEnd` after all repeating cycles complete (see the segment table in [ECAMStart](ECAMStart.md)). While the master sits at or beyond the master position that maps to `ECAMEnd` (the *post-end* region), the follower reference is clamped to `GenData[ECAMEnd]` (for positive [ECAMGap](ECAMGap.md)) so the follower holds steady at the end of the profile; with negative `ECAMGap` the clamped ends are swapped with `ECAMStart`. If a [StopECAM](StopECAM.md) is pending when the master reaches this clamp, the motion ends there.

In the endless modes that keep only a starting segment (`ECAMCycles = 2147483647`) or no tails at all (`ECAMCycles = -2147483648`), the table entries beyond `ECAMEndCyc` up to `ECAMEnd` are ignored — see [ECAMCycles](ECAMCycles.md).

## Examples

```text
AECAMEnd[1]=100      ; cam pattern 1 ends at GenData index 100
AECAMEnd[1]         ; read current value
```

## See also

- [ECAMStart](ECAMStart.md) — start index of the overall pattern (segment model and clamping)
- [ECAMStartCyc](ECAMStartCyc.md) / [ECAMEndCyc](ECAMEndCyc.md) — bounds of the repeating segment
- [ECAMCycles](ECAMCycles.md) — endless modes that ignore the trailing segment
- [GenData](../../20-arrays/GenData.md) — array storing the cam pattern
