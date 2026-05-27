---
keyword: FIFOPushLinV
summary: Pushes a constant-velocity (linear) segment into the FIFO motion queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`FIFOPushLinV` appends a **linear-by-velocity** segment (type 2 in [FIFOType](FIFOType.md)) to the queue. The value is the velocity reference, held constant for the duration of the segment. The segment starts from the previous position reference and advances by a fixed per-sample step equal to that velocity.

It is one of the `FIFOPush*` functions used to fill the queue before or during motion. The entry is added at the tail. If the queue is full, the push is rejected with an error.

Unlike [FIFOPushLinP](FIFOPushLinP.md), which specifies how far to move and lets the velocity follow from the cycle time, this function specifies the velocity directly. The distance covered therefore depends on the active [FIFOCycleTime](FIFOCycleTime.md).

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## How it works

When the controller reaches this segment, it advances the position reference by the supplied velocity every control sample for the segment duration. The velocity is reported in [FIFOStatus](FIFOStatus.md) (index 4); the acceleration (index 5) is 0. The accepted range is -1 300 000 000 to 1 300 000 000.

## Examples

```text
AFIFOPushLinV=500000 ; queue a constant-velocity segment at velocity 500000
```

## See also

- [FIFOPushLinP](FIFOPushLinP.md) — push a linear segment by position delta
- [FIFOPushCycle](FIFOPushCycle.md) — set the segment duration
- [FIFOType](FIFOType.md) — full FIFO mode description
