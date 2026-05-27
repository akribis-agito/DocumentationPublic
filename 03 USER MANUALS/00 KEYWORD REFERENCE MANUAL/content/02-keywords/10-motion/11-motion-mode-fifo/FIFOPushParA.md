---
keyword: FIFOPushParA
summary: Pushes a parabolic (constant-acceleration) segment into the FIFO motion queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 288
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
  range:
  - -2000000000
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPushParA

Pushes a parabolic (constant-acceleration) segment into the FIFO motion queue.

## Overview

`FIFOPushParA` pushes an acceleration-type motion segment into the FIFO, in which the acceleration reference is held constant for the segment duration, producing a parabolic position profile. It is the acceleration-based counterpart of [FIFOPushParP](FIFOPushParP.md), which defines the parabolic segment by position. It is one of the `FIFOPush*` functions used to fill the FIFO before or during motion; the push is rejected with an error if the FIFO is full.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## Examples

```text
AFIFOPushParA=100000 ; push a constant-acceleration (parabolic) segment
```

## See also

- [FIFOPushParP](FIFOPushParP.md) — parabolic segment defined by position
- [FIFOPushCycle](FIFOPushCycle.md) — set the segment duration
- [FIFOType](FIFOType.md) — full FIFO mode description
