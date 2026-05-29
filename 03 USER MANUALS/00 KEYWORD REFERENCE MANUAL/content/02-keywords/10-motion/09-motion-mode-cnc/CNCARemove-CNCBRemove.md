---
summary: Reserved CNC FIFO segment-removal keyword (not exposed in current firmware).
---
# CNCARemove/CNCBRemove

Reserved CNC FIFO segment-removal keyword. Not exposed by current firmware.

## Overview

`CNCARemove` / `CNCBRemove` were intended as the per-segment complement to [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md), removing the most recently pushed segment from the CNC FIFO without discarding the rest of the queue.

> **Not in current firmware.** Neither `CNCARemove` nor `CNCBRemove` is exposed as a keyword by the present firmware (LTS v3.X.X or develop). To undo a queued segment today, the only option is to flush the queue with [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) and re-push the segments to keep.

## See also

- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — clear all pending segments
- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — push a segment to the queue
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
- [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) — queue free space and the open-segment parameter count
