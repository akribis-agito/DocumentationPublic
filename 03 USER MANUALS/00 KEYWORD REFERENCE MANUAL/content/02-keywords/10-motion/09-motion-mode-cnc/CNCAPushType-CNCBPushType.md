---
summary: Command that pushes a new motion segment into the CNC FIFO queue A (or B).
---
# CNCAPushType/CNCBPushType

Command that pushes a new motion segment into the CNC FIFO queue A (or B).

## Overview

`CNCAPushType` (and its `CNCBPushType` counterpart) is a command used to push a new motion segment into the CNC FIFO queue A (or B). The argument selects the segment type (for example, linear or arc) and the segment parameters are taken from the associated CNC parameter set. It is a non-axis command function that can be issued at any time.

After selecting the type, the segment's parameters are supplied with [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md). Over Ethernet, [CNCAPushSeg/CNCBPushSeg](CNCAPushSeg-CNCBPushSeg.md) can push the type and parameters in a single message.

## Examples

```text
ACNCAPushType=1      ; push a new segment of the selected type into FIFO A
```

## See also

- [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md) — supply the segment parameters
- [CNCAPushSeg/CNCBPushSeg](CNCAPushSeg-CNCBPushSeg.md) — push a full segment in one Ethernet message
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — clear all pending segments
