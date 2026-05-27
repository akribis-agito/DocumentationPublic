---
summary: Read-only array holding the raw segment data queued in the CNC FIFO for queue A (or B).
---
# CNCAFIFO/CNCBFIFO

Read-only array holding the raw segment data queued in the CNC FIFO for queue A (or B).

## Overview

`CNCAFIFO` (and its `CNCBFIFO` counterpart on the second CNC engine) is a read-only array that exposes the raw contents of the CNC segment queue (FIFO) for queue A (or B). Reading it lets you inspect the pending motion segments before — and while — they are executed. It is a non-axis, read-only array that is not saved to flash. Like all communication arrays it is 1-indexed: index 0 is reserved so element indexes start at 1.

Segments are loaded with [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) plus [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md) (or [CNCAPushSeg/CNCBPushSeg](CNCAPushSeg-CNCBPushSeg.md)), consumed during playback, and flushed with [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md).

## How it works

The array is the backing store of the queue. Segments are packed into consecutive elements as a stream of words, **not** one element per segment:

- The first word of each segment holds the segment's ID (upper 24 bits) and an entry count (lower 8 bits).
- The second word holds the same type/involved-axes encoding used by [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) (top byte = type, lower 24 bits = involved axes).
- The following words hold the segment's parameters, in push order.

So opening a segment consumes two slots (header + type word) and each parameter consumes one more. The capacity differs between the two queues and between products: queue A typically holds on the order of a few thousand words, while queue B may be much smaller on some products. Use [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) to read the actual free space rather than assuming a fixed size — element 7 of the status array reports free words, and a freshly cleared queue reports the full usable capacity.

Reading raw words is mainly a diagnostic aid; the meaning of each word follows the layout above and the parameter order of each segment type listed in [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md).

## Examples

```text
ACNCAFIFO[1]        ; read the first queued word (arrays are 1-indexed)
ACNCAFIFO[2]        ; read the type/involved-axes word of the first segment
```

## See also

- [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) — free space, queue pointers and motion state
- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — push a segment to the queue
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — clear all pending segments
- [StopCNCA](StopCNCA.md) — stop CNC motion on queue A
