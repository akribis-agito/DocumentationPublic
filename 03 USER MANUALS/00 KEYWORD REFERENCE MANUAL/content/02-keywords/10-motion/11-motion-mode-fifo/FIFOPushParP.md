---
keyword: FIFOPushParP
summary: Pushes a parabolic segment defined by a position value into the FIFO motion queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 287
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPushParP

Pushes a parabolic segment defined by a position value into the FIFO motion queue.

## Overview

`FIFOPushParP` pushes a parabolic (constant-acceleration) motion segment into the FIFO, defined by a position value. It is the position-based counterpart of [FIFOPushParA](FIFOPushParA.md), which defines the parabolic segment by acceleration. It is one of the `FIFOPush*` functions used to fill the FIFO before or during motion; the push is rejected with an error if the FIFO is full.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## Examples

```text
AFIFOPushParP=20000  ; push a parabolic segment defined by position
```

## See also

- [FIFOPushParA](FIFOPushParA.md) — parabolic segment defined by acceleration
- [FIFOPushCycle](FIFOPushCycle.md) — set the segment duration
- [FIFOType](FIFOType.md) — full FIFO mode description
