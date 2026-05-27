---
summary: Read-only array holding the raw segment data queued in the CNC FIFO for queue A (or B).
---
# CNCAFIFO/CNCBFIFO

Read-only array holding the raw segment data queued in the CNC FIFO for queue A (or B).

## Overview

`CNCAFIFO` (and its `CNCBFIFO` counterpart) is a read-only array that holds the raw segment data currently queued in the CNC motion FIFO for queue A (or B). Reading it allows inspection of the pending motion segments before they are executed. It is a non-axis, read-only array that is not saved to flash.

Segments are loaded into the FIFO with [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) and removed with [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md).

## Examples

```text
ACNCAFIFO[1]        ; read the first queued segment word (arrays are 1-indexed)
```

## See also

- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — push a segment to the FIFO
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — clear all pending segments
- [StopCNCA](StopCNCA.md) — stop CNC motion on queue A
