---
summary: Command that clears all pending segments from the CNC FIFO queue A (or B).
---
# CNCAClear/CNCBClear

Command that clears all pending segments from the CNC FIFO queue A (or B).

## Overview

`CNCAClear` (and its `CNCBClear` counterpart on the second CNC engine) clears all pending segments from the CNC segment queue (FIFO) for queue A (or B) and resets it so new segments can be loaded from a clean state. It is a non-axis command function.

Unlike [StopCNCA](StopCNCA.md)/[StopCNCB](StopCNCB.md), which halt motion but leave the queue intact, `CNCAClear` empties the queue loaded by [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md).

## How it works

- `CNCAClear` is **rejected with an error while a CNC motion is in progress** on that queue. Stop the motion first ([StopCNCA](StopCNCA.md)/[StopCNCB](StopCNCB.md)), then clear. When the queue is idle (or simply being filled with no motion yet), the clear is accepted.
- Clearing restores the queue to its empty state: the free-space count returns to the full usable capacity (reported by element 7 of [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md)), the queue pointers and segment IDs are reset, and the engine again expects the first segment (so the next push must follow the first-segment rules described in [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md)).
- The end-of-segment correction counter [CNCAEndErrCnt/CNCBEndErrCnt](CNCAEndErrCnt-CNCBEndErrCnt.md) and the velocity-jump / acceleration-limit counters are reset to 0, and the per-axis maximum velocity-jump and acceleration limits return to their defaults.

## Examples

```text
ACNCAClear           ; flush all queued segments from FIFO A
```

## See also

- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
- [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) — free space and motion state (must be idle to clear)
- [StopCNCA](StopCNCA.md) — stop motion without clearing the queue
- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — push a segment to the queue
- [CNCARemove/CNCBRemove](CNCARemove-CNCBRemove.md) — remove only the last segment
