---
keyword: FIFOPushCycle
summary: Pushes a cycle-time (segment-duration) entry into the FIFO motion queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 284
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - 1
    - 65536000
---
# FIFOPushCycle

Pushes a cycle-time (segment-duration) entry into the FIFO motion queue.

## Overview

`FIFOPushCycle` pushes an entry into the FIFO that sets the cycle time (segment duration in control samples) for subsequent motion segments. It is one of the `FIFOPush*` functions used to fill the FIFO before or during motion. Like all FIFO pushes, it is rejected with an error if the FIFO is full.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## Examples

```text
AFIFOPushCycle=16    ; push a segment-duration entry of 16 control samples
```

## See also

- [FIFOCycleTime](FIFOCycleTime.md) — current segment duration
- [FIFOPushLinP](FIFOPushLinP.md), [FIFOPushLinV](FIFOPushLinV.md) — push linear segments
- [FIFOPushParP](FIFOPushParP.md), [FIFOPushParA](FIFOPushParA.md) — push parabolic segments
- [FIFOType](FIFOType.md) — full FIFO mode description
