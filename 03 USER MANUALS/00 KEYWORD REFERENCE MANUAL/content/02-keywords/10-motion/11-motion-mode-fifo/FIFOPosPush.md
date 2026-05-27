---
keyword: FIFOPosPush
summary: Command that pushes a new position segment into the FIFO position queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 666
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
# FIFOPosPush

Command that pushes a new position segment into the FIFO position queue.

## Overview

`FIFOPosPush` pushes a new position segment into the FIFO position queue. The segment type is specified by its argument, and the segment data is taken from the associated FIFO position parameters: [FIFOPosTrgt](FIFOPosTrgt.md), [FIFOPosPosOf](FIFOPosPosOf.md), [FIFOPosVelOf](FIFOPosVelOf.md), and [FIFOPosCurrOf](FIFOPosCurrOf.md). It can be issued at any time, including during motion.

## Examples

```text
AFIFOPosPush=0       ; push a position segment using the current FIFOPos* parameters
```

## See also

- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — enable FIFO position tracking
- [FIFOPosType](FIFOPosType.md) — select the position-tracking mode
- [FIFOPosClear](FIFOPosClear.md) — clear the queue
- [FIFOPosStatus](FIFOPosStatus.md) — queue status
