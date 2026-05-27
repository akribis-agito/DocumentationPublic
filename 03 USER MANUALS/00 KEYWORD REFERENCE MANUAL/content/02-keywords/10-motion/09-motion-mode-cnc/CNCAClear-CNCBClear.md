---
summary: Command that clears all pending segments from the CNC FIFO queue A (or B).
---
# CNCAClear/CNCBClear

Command that clears all pending segments from the CNC FIFO queue A (or B).

## Overview

`CNCAClear` (and its `CNCBClear` counterpart) is a command that clears all pending segments from the CNC motion FIFO queue A (or B). It resets the queue so that new segments can be loaded from a clean state. It is a non-axis command function that can be issued at any time, including during motion.

Unlike [StopCNCA](StopCNCA.md)/[StopCNCB](StopCNCB.md), which halt motion but leave the queue intact, `CNCAClear` empties the FIFO loaded by [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md).

## Examples

```text
CNCAClear           ; flush all queued segments from FIFO A
```

## See also

- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
- [StopCNCA](StopCNCA.md) — stop motion without clearing the queue
- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — push a segment to the FIFO
