---
keyword: FIFOCycleTime
summary: Duration, in control samples, of the FIFO motion segment currently being executed.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 283
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 65536
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - 1
    - 65536000
---
# FIFOCycleTime

Duration, in control samples, of the FIFO motion segment currently being executed.

## Overview

`FIFOCycleTime` is the time length of each FIFO motion segment, expressed as a number of control-loop samples. It can be modified at any time the controller is ending one segment and starting a new one, allowing the segment duration to vary across the FIFO sequence.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## Examples

```text
AFIFOCycleTime      ; query the current segment duration in control samples
```

## See also

- [FIFOType](FIFOType.md) — full FIFO mode description
- [FIFOPushCycle](FIFOPushCycle.md) — push a cycle-time entry into the FIFO
- [FIFOStatus](FIFOStatus.md) — FIFO queue status
