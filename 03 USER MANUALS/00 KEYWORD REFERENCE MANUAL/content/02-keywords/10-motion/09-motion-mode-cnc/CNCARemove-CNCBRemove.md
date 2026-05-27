---
summary: Function that removes the last segment from the CNC FIFO A (or B).
---
# CNCARemove/CNCBRemove

Function that removes the last segment from the CNC FIFO A (or B).

## Overview

`CNCARemove` (and its `CNCBRemove` counterpart on the second CNC engine) removes the most recently pushed segment from the CNC segment queue (FIFO) for queue A (or B). It is the per-segment complement to [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md), which empties the entire queue. Use it to undo a push — for example, to back out the last segment of a path that was queued in error — without discarding the rest of the queue.

## How it works

`CNCARemove` works at the tail of the queue (the last-pushed end), the opposite end from where playback drains segments:

- If the last pushed segment is **closed**, it is popped out of the queue and its ID is cancelled, so the next pushed segment receives that same ID. The queue's free space (element 7 of [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md)) increases by the words the segment occupied.
- If you are **part-way through pushing** parameters to a segment (element 5 of the status array is non-zero), that incomplete segment is cancelled and the controller is ready to accept a new one, which receives the same ID as the cancelled segment.
- `CNCARemove` returns an error if the queue is empty.
- `CNCARemove` fails and returns an error (removing nothing) if the segment at the tail is the one the engine is currently using for motion.

## Examples

```text
ACNCARemove          ; remove the last segment from FIFO A
```

## See also

- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — clear all pending segments
- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — push a segment to the queue
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
- [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) — queue free space and the open-segment parameter count
