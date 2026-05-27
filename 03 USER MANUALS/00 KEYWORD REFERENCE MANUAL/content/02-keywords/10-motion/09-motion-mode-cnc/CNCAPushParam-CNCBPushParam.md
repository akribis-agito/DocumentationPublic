---
summary: Pushes parameter values of a CNC segment into the CNC FIFO.
---
# CNCAPushParam/CNCBPushParam

Pushes parameter values of a CNC segment into the CNC FIFO.

## Overview

`CNCAPushParam` (and its `CNCBPushParam` counterpart on the second CNC engine) supplies one parameter value of the segment currently being pushed into the CNC segment queue (FIFO) for queue A (or B). It always follows a [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md), which opens the segment and fixes how many parameters that segment needs; the required number of `CNCAPushParam` writes then complete it. When the last expected parameter is pushed, the segment is **closed** and becomes a queued entry available for playback.

To push a complete segment (type and all parameters) in a single message over Ethernet, see [CNCAPushSeg/CNCBPushSeg](CNCAPushSeg-CNCBPushSeg.md).

## How it works

Opening a segment with `CNCAPushType` records the total number of parameters that segment expects (see the segment-type table in [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md)). Each `CNCAPushParam` write does the following:

- It is rejected with an error if no segment is currently open — that is, if the queue is empty or the previous segment is already closed. A `CNCAPushType` must come first.
- The value is stored in the queue and the count of still-needed parameters is decremented by one.
- When the count reaches zero the segment is **closed**: its parameters are validated as a set (for example, an arc's start and end radius derived from the centre must agree, and a continuous-motion segment must follow on from the previous segment's end speed). A validation failure rejects the segment.

Parameters must be pushed in the exact order listed for the segment type. Until a segment is closed it is not eligible for playback, so a half-pushed segment at the tail of the queue does not protect against an [underrun](CNCAPushType-CNCBPushType.md) — the motion engine treats "last segment still being filled" the same as "no segment ready".

The number of free queue slots is reported by [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md). Each push consumes one slot; a push is rejected if the queue is full.

## Examples

```text
ACNCAPushType=value  ; open, e.g., a 2-axis linear move (needs 4 parameters)
ACNCAPushParam=1000  ; parameter 1: target position of first axis
ACNCAPushParam=2000  ; parameter 2: target position of second axis
ACNCAPushParam=50000 ; parameter 3: path speed
ACNCAPushParam=0     ; parameter 4: end speed -> segment now closed and queued
```

## See also

- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — open the segment and choose its type
- [CNCAPushSeg/CNCBPushSeg](CNCAPushSeg-CNCBPushSeg.md) — push a full segment in one Ethernet message
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
- [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) — free slots and how many parameters the open segment still needs
