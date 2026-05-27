---
keyword: FIFOPushLinP
summary: Pushes a linear segment defined by a position delta into the FIFO motion queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`FIFOPushLinP` appends a **linear-by-position-delta** segment (type 1 in [FIFOType](FIFOType.md)) to the queue. The value is the position delta to travel during the segment. The segment starts from the previous position reference and reaches that reference plus the delta at the end of the segment, moving at constant velocity.

It is one of the `FIFOPush*` functions used to fill the queue before or during motion. The entry is added at the tail. If the queue is full, the push is rejected with an error.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## How it works

When the controller reaches this segment, it divides the position delta by the active [FIFOCycleTime](FIFOCycleTime.md) to obtain a constant per-sample step, then advances the position reference by that step every control sample for the duration of the segment. The requested delta is reached exactly on the final sample. The resulting constant velocity is reported in [FIFOStatus](FIFOStatus.md) (index 4); the acceleration (index 5) is 0.

## Examples

```text
AFIFOPushLinP=10000  ; queue a constant-velocity segment that travels 10000 units
```

## See also

- [FIFOPushLinV](FIFOPushLinV.md) — push a linear segment by velocity
- [FIFOPushCycle](FIFOPushCycle.md) — set the segment duration
- [FIFOType](FIFOType.md) — full FIFO mode description
