---
summary: Pushes a complete CNC segment (type and parameters) in one Ethernet message.
---
# CNCAPushSeg/CNCBPushSeg

Pushes a complete CNC segment (type and parameters) in one Ethernet message.

## Overview

`CNCAPushSeg` (and its `CNCBPushSeg` counterpart on the second CNC engine) pushes a complete segment — its type, involved axes and all parameters — into the CNC segment queue (FIFO) for queue A (or B) using a single Ethernet message. It collapses the multi-message sequence of one [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) followed by the required [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md) writes into one transfer, which significantly raises the rate at which segments can be loaded — the main factor in keeping the queue full enough to avoid an [underrun](CNCAPushType-CNCBPushType.md) when streaming dense paths.

> **Note:** This keyword is supported only over an Ethernet communication connection to the controller. It returns an error over any other connection (such as RS-232 or CAN); on those links, push segments with `CNCAPushType` and `CNCAPushParam` instead.

## How it works

The message carries the same type/involved-axes word used by [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) (top byte = segment type, lower 24 bits = up to six involved axes) followed by exactly the number of parameter values that segment type requires, in the same order as separate `CNCAPushParam` writes would supply them. See the segment-type and parameter tables in [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md).

The controller processes the whole segment atomically: it opens the segment, stores every parameter, validates the segment as a set, and closes it so it is immediately eligible for playback. If validation fails or the queue lacks room for the whole segment, the entire push is rejected — a partial segment is never left in the queue. Behaviour at the queue, during playback and on drain is identical to segments pushed the multi-message way.

## Examples

```text
ACNCAPushSeg=...     ; push one full segment (type + parameters) over Ethernet
```

## See also

- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — segment type encoding and parameter counts
- [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md) — push individual segment parameters
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
- [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) — free slots and queue state
