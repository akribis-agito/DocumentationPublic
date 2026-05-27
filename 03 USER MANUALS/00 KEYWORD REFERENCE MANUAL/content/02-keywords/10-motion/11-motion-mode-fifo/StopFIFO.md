---
keyword: StopFIFO
summary: Command that makes the currently executing FIFO segment the last one, ending the sequence.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 291
attributes:
  access: ro
  scope: axis
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
# StopFIFO

Command that makes the currently executing FIFO segment the last one, ending the sequence.

## Overview

`StopFIFO` stops a FIFO motion by making the currently executing motion segment the last segment of the sequence. Unlike the general [Stop](../04-motion-command/Stop.md) command, which decelerates the axis to zero speed, `StopFIFO` lets the active segment complete and then ends the motion, so the FIFO trajectory finishes gracefully.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## Examples

```text
StopFIFO=0          ; end the FIFO motion after the current segment
```

## See also

- [Stop](../04-motion-command/Stop.md) — decelerate the axis to zero speed
- [FIFOType](FIFOType.md) — full FIFO mode description
- [FIFOStatus](FIFOStatus.md) — FIFO queue status
