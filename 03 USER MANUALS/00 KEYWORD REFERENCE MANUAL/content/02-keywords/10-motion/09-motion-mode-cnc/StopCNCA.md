---
keyword: StopCNCA
summary: Command that stops execution of the CNC motion queue A.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 456
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# StopCNCA

Command that stops execution of the CNC motion queue A.

## Overview

`StopCNCA` is a command function that stops the CNC motion engine driving queue A. The currently executing segment is aborted and the axis decelerates to rest. Because it is a command, it can be issued at any time, including during motion.

Use `StopCNCA` to halt motion while leaving the queue intact, as opposed to [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md), which empties the segment FIFO. The companion command for the second engine is [StopCNCB](StopCNCB.md).

## Examples

```text
AStopCNCA            ; stop CNC motion on queue A
```

## See also

- [StopCNCB](StopCNCB.md) — stop command for the second CNC engine
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — clear all pending segments from the queue
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — inspect queued segment data
