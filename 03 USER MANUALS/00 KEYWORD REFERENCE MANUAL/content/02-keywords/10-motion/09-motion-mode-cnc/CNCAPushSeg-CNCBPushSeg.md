---
summary: Pushes a complete CNC segment (type and parameters) in one Ethernet message.
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# CNCAPushSeg/CNCBPushSeg

Pushes a complete CNC segment (type and parameters) in one Ethernet message.

## Overview

`CNCAPushSeg` (and its `CNCBPushSeg` counterpart on the second CNC engine) pushes a complete segment — its type, involved axes and all parameters — into the CNC segment queue (FIFO) for queue A (or B) using a single Ethernet message. It collapses the multi-message sequence of one [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) followed by the required [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md) writes into one transfer, which significantly raises the rate at which segments can be loaded — the main factor in keeping the queue full enough to avoid an [underrun](CNCAPushType-CNCBPushType.md) when streaming dense paths.

> **Note:** This keyword is supported only over an Ethernet communication connection to the controller. It returns an error over any other connection (such as RS-232 or CAN); on those links, push segments with `CNCAPushType` and `CNCAPushParam` instead.

## How it works

The message carries the same type/involved-axes word used by [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) (top byte = segment type, lower 24 bits = up to six involved axes) followed by exactly the number of parameter values that segment type requires, in the same order as separate `CNCAPushParam` writes would supply them. See the segment-type and parameter tables in [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md).

The controller processes the segment as the equivalent sequence of a type push followed by each parameter push, then closes it so it is immediately eligible for playback. Behaviour at the queue, during playback and on drain is identical to segments pushed the multi-message way.

The number of supplied parameter values must exactly match the count the segment type requires; if it does not, the message is rejected up front and nothing is added to the queue. Errors caught before the segment is opened — a bad or out-of-range type, an ordering violation (such as a "set initial positions" segment that is not first), or insufficient queue space for the whole segment — likewise reject the push cleanly. However, a value that only fails validation as the segment is closed (for example an inconsistent arc radius, a segment that is too short, or a speed out of range) is reported as an error *after* the segment's type entry and its earlier parameters have already been written, leaving a partially built, unclosed segment in the queue. Recover from that case by flushing the queue with [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md).

## Examples

```text
ACNCAPushSeg=...     ; push one full segment (type + parameters) over Ethernet
```

## See also

- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — segment type encoding and parameter counts
- [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md) — push individual segment parameters
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
- [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) — free slots and queue state
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — flush all pending segments
