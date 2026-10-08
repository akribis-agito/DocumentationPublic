---
keyword: LockLost
summary: Counts the lock samples that did not become a capture of their own, on Central-i masters.
availability:
  standalone: []
  central-i:
  - v5
can_code: 918
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-07'
doc_revision: '2026.09'
---
# LockLost

Counts the lock samples that did not become a capture of their own, on Central-i masters.

## Overview

`LockLost` is a read-only counter that complements [LockCntr](LockCntr-AuxLockCntr.md). `LockCntr` counts the positions that were captured; `LockLost` counts the trigger samples whose position could not be captured on its own, because the remote unit keeps only the position of the most recent edge. Read both after a burst of trigger edges: a non-zero `LockLost` tells you that some edges are missing from [LockValTable](LockValTable-LockValTabB.md) / [LockTimeTable](LockTimeTable-LockTimeTabB.md) even though `LockCntr` advanced.

`LockLost` is cleared to `0` together with `LockCntr` when logging ([LockEn](LockEn-AuxLockEn.md)) is enabled from the disabled state. It is per axis, 32-bit, not saved to flash, and available on Central-i masters only.

## How it works

The remote unit samples the trigger once per control cycle (about 61 µs). It latches the position of the last edge in that cycle and keeps nothing else, so the positions of earlier edges in the same cycle cannot be recovered. A cycle with two or more edges is reported to the master as an error sample. The master reads the retained position over the offline mailbox, which takes a few control cycles to answer, and an edge that arrives during that time replaces the position the next read would return.

`LockLost` advances by one for each of these samples:

| Situation | `LockCntr` | `LockLost` |
|---|---|---|
| One edge in a control cycle | +1 | 0 |
| Two or more edges in one control cycle | +1, with the position of the last edge | +1 |
| An edge while the read for the previous edge is pending | +1 once that read is answered (the edge is read afterwards and recorded as its own entry) | 0 |
| An edge while the read for the previous edge is queued behind a table event, or is waiting to be retried | +1 once that read is answered, with the position of the later edge | +1 |
| A further edge while that follow-up read is still waiting | unchanged by this edge, which shares the follow-up capture | +1 |
| While a read is pending, a control cycle that holds several edges | +1 once the follow-up read is answered | +1 |
| The remote returns no position, or does not answer in time | 0 | +1 |
| Absolute or SinCos main encoder, two or more edges in one control cycle | +1, with the position read in that cycle | +1 |

`LockLost` counts control cycles, not edges: a cycle that holds four edges adds one to `LockCntr` and one to `LockLost`. The captured position of such a cycle is that of the last edge.

[LockTimeTable](LockTimeTable-LockTimeTabB.md) stamps a capture with the control cycle in which its position was read, so an edge that was read after the previous reply carries that later cycle, not the cycle of the edge itself.

To record every edge as its own entry, keep the trigger edges well apart. In a bench measurement with four events at a fixed gap, every edge was recorded at gaps of 200 µs and above.

## Examples

```text
ALockLost            ; read the number of lock samples that were not captured on their own
ALockEn=0
ALockEn=1            ; LockCntr and LockLost both return to 0
```

## See also

- [LockCntr](LockCntr-AuxLockCntr.md) — counts the captured positions and indexes the history arrays
- [LockEn](LockEn-AuxLockEn.md) — enables logging; resets `LockLost` to 0
- [LockSrc](LockSrc-AuxLockSrc.md) — defines the trigger event
- [LockValTable](LockValTable-LockValTabB.md) / [LockTimeTable](LockTimeTable-LockTimeTabB.md) — history arrays
