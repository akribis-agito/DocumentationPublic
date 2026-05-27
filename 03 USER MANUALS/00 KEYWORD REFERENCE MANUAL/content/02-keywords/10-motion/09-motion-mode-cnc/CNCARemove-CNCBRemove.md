---
summary: Function that removes the last segment from the CNC FIFO A (or B).
---
# CNCARemove/CNCBRemove

Function that removes the last segment from the CNC FIFO A (or B).

## Overview

`CNCARemove` (and its `CNCBRemove` counterpart on the second CNC engine) is a function keyword to remove the last CNC FIFO A segment. It is the per-segment complement to [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md), which empties the entire FIFO.

## How it works

- If the last pushed segment is closed, it is popped out of the CNC FIFO (removed) and its ID is cancelled, so the next pushed segment receives this ID.
- If you are in the middle of pushing parameters to a segment, that segment is cancelled and the controller is ready to accept a new segment (which receives the same ID as the deleted segment).
- `CNCARemove` returns an error if the CNC FIFO A is empty.
- `CNCARemove` fails and returns an error (without removing anything from the CNC FIFO) if the controller is using this segment for motion at the time.

## Examples

```text
CNCARemove          ; remove the last segment from FIFO A
```

## See also

- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — clear all pending segments
- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — push a segment to the FIFO
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
