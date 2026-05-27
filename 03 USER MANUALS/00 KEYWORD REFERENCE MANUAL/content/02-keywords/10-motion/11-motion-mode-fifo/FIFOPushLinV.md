---
keyword: FIFOPushLinV
summary: Pushes a constant-velocity (linear) segment into the FIFO motion queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 286
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
  - -1300000000
  - 1300000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPushLinV

Pushes a constant-velocity (linear) segment into the FIFO motion queue.

## Overview

`FIFOPushLinV` pushes a velocity-type motion segment into the FIFO, in which the velocity reference is held constant for the segment duration. The segment starts naturally from the last position reference. It is one of the `FIFOPush*` functions used to fill the FIFO before or during motion; the push is rejected with an error if the FIFO is full.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## Examples

```text
FIFOPushLinV=500000 ; push a constant-velocity segment
```

## See also

- [FIFOPushLinP](FIFOPushLinP.md) — push a linear segment by position delta
- [FIFOPushCycle](FIFOPushCycle.md) — set the segment duration
- [FIFOType](FIFOType.md) — full FIFO mode description
