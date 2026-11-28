---
keyword: ECAMEnd
summary: GenData index where the ECAM cam pattern ends.
availability:
- controller
- ci-master
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
  - 5000
  default: 100
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - 0
    - 1000
  agc300-et:
    range:
    - 0
    - 1000
  agd200-et-2d01:
    range:
    - 0
    - 1000
  agd200-et-2d02:
    range:
    - 0
    - 1000
  agd200-et-2d05:
    range:
    - 0
    - 1000
  agd200-et-2d05-71:
    range:
    - 0
    - 1000
  agd155-af-2a06:
    range:
    - 0
    - 1000
  agd155-af-2a10:
    range:
    - 0
    - 1000
  agd155-ec:
    range:
    - 0
    - 1000
  agd155-ec-var34:
    range:
    - 0
    - 1000
  agd155-ec-var34-3:
    range:
    - 0
    - 1000
  agd156-ec:
    range:
    - 0
    - 1000
  agd101-ec-34a:
    range:
    - 0
    - 1000
  agd101-ec-17a:
    range:
    - 0
    - 1000
last_updated: '2026-06-02'
doc_revision: '2026.06'
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

`ECAMEnd` is the last entry of the pattern, terminating the trailing one-shot segment that runs from `ECAMEndCyc` to `ECAMEnd` after all repeating cycles complete (see the segment table in [ECAMStart](ECAMStart.md)). While the master sits at or beyond the master position that maps to `ECAMEnd` (the *post-end* region), the follower reference is clamped to `GenData[ECAMEnd]` so the follower holds steady at the end of the profile. This applies for either sign of [ECAMGap](ECAMGap.md): a negative `ECAMGap` reverses direction by internally negating the master reading, but the post-end clamp still uses `GenData[ECAMEnd]` (and the pre-start clamp still uses `GenData[ECAMStart]`). If a [StopECAM](StopECAM.md) is pending when the master reaches this clamp, the motion ends there.

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
