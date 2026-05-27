---
keyword: FIFOPushLinP
summary: Pushes a linear segment defined by a position delta into the FIFO motion queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 285
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
# FIFOPushLinP

Pushes a linear segment defined by a position delta into the FIFO motion queue.

## Overview

`FIFOPushLinP` pushes a linear (constant-velocity) motion segment into the FIFO, defined by a position delta. The segment starts from the last position reference, and the final target position is calculated from the given delta. It is one of the `FIFOPush*` functions used to fill the FIFO before or during motion; the push is rejected with an error if the FIFO is full.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## Examples

```text
FIFOPushLinP=10000  ; push a linear segment with a position delta of 10000
```

## See also

- [FIFOPushLinV](FIFOPushLinV.md) — push a linear segment by velocity
- [FIFOPushCycle](FIFOPushCycle.md) — set the segment duration
- [FIFOType](FIFOType.md) — full FIFO mode description
