---
keyword: ECAMStart
summary: GenData index where the ECAM cam pattern starts.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 300
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
overrides:
  central-i.v5:
    range:
    - 0
    - 10000
---
# ECAMStart

GenData index where the ECAM cam pattern starts.

## Overview

`ECAMStart` defines the [GenData](../../20-arrays/GenData.md) index where the cam pattern starts. It is an array of 10 cam patterns, one element per pattern. It is the lower bound of the overall pattern, paired with the upper bound [ECAMEnd](ECAMEnd.md), while [ECAMStartCyc](ECAMStartCyc.md) and [ECAMEndCyc](ECAMEndCyc.md) bound the repeating segment.

## How it works

`ECAMStart` must satisfy the ordering from which the overall cam pattern is derived:

$$
\text{ECAMStart} \leq \text{ECAMStartCyc} < \text{ECAMEndCyc} \leq \text{ECAMEnd}
$$

The four index keywords divide the cam pattern into three parts that the controller plays back as the master advances:

| Segment | Index range | Role |
|----|----|----|
| Leading (one-shot) | `ECAMStart` … `ECAMStartCyc` | Played once as the master enters the range; acts as a lead-in/acceleration segment. |
| Repeating | `ECAMStartCyc` … `ECAMEndCyc` | Replayed `abs(ECAMCycles)` times (see [ECAMCycles](ECAMCycles.md)). |
| Trailing (one-shot) | `ECAMEndCyc` … `ECAMEnd` | Played once as the master leaves the cycles; acts as a lead-out/deceleration segment. |

`ECAMStart` is the very first entry of the pattern. While the master sits at or below the master position that maps to `ECAMStart` (the *pre-start* region), the follower reference is clamped to `GenData[ECAMStart]` (for positive [ECAMGap](ECAMGap.md)) so it holds steady rather than running off the table; with negative `ECAMGap` the roles of `ECAMStart` and `ECAMEnd` as the clamped ends are swapped. If a [StopECAM](StopECAM.md) is pending when the master reaches this clamp, the motion ends there.

If `ECAMCycles = 1` there is no repetition, so `ECAMStartCyc` and `ECAMEndCyc` are not used and the whole pattern is simply `ECAMStart` … `ECAMEnd`.

## Examples

```text
AECAMStart[1]=1      ; cam pattern 1 starts at GenData index 1
AECAMStart[1]       ; read current value
```

## See also

- [ECAMEnd](ECAMEnd.md) — end index of the overall pattern
- [ECAMStartCyc](ECAMStartCyc.md) / [ECAMEndCyc](ECAMEndCyc.md) — bounds of the repeating segment
- [ECAMGap](ECAMGap.md) — master-to-index mapping and direction
- [GenData](../../20-arrays/GenData.md) — array storing the cam pattern
