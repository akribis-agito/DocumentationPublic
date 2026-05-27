---
keyword: StopCNCB
summary: Command that stops execution of the CNC motion queue B.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 688
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
# StopCNCB

Command that stops execution of the CNC motion queue B.

## Overview

`StopCNCB` is a command function that stops the CNC motion engine driving queue B. The currently executing segment is aborted and the axis decelerates to rest. Because it is a command, it can be issued at any time, including during motion.

`StopCNCB` is the second-engine counterpart of [StopCNCA](StopCNCA.md). It halts motion while leaving the queue intact, as opposed to [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md), which empties the segment FIFO.

## Examples

```text
AStopCNCB            ; stop CNC motion on queue B
```

## See also

- [StopCNCA](StopCNCA.md) — stop command for the first CNC engine
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — clear all pending segments from the queue
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — inspect queued segment data
