---
summary: Pushes parameter values of a CNC segment into the CNC FIFO.
---
# CNCAPushParam/CNCBPushParam

Pushes parameter values of a CNC segment into the CNC FIFO.

## Overview

`CNCAPushParam` (and its `CNCBPushParam` counterpart on the second CNC engine) is used to push values of parameters into the CNC FIFO. It follows a [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) command, which selects the segment type; the required number of `CNCAPushParam` writes supply that segment's parameters.

To push a complete segment (type and parameters) in a single message over Ethernet, see [CNCAPushSeg/CNCBPushSeg](CNCAPushSeg-CNCBPushSeg.md).

## Examples

```text
ACNCAPushParam=1000  ; push one segment parameter into the FIFO
```

## See also

- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — select the segment type
- [CNCAPushSeg/CNCBPushSeg](CNCAPushSeg-CNCBPushSeg.md) — push a full segment in one Ethernet message
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
