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

`FIFOPushParP` appends a **parabolic-by-position-delta** segment (type 3 in [FIFOType](FIFOType.md)) to the queue. The value is the position delta to travel during the segment. The motion is at constant acceleration, so the position follows a parabola: it begins from the current profiler velocity and reaches the previous position reference plus the delta at the end of the segment. It is the position-based counterpart of [FIFOPushParA](FIFOPushParA.md), which defines the segment by acceleration instead.

It is one of the `FIFOPush*` functions used to fill the queue before or during motion. The entry is added at the tail. If the queue is full, the push is rejected with an error.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## How it works

When the controller reaches this segment, it computes the constant acceleration needed to travel the requested delta over the active [FIFOCycleTime](FIFOCycleTime.md), starting from the current velocity. It then ramps the velocity by that acceleration each control sample, advancing the position reference accordingly, so the delta is reached on the final sample. The evolving velocity and acceleration are reported in [FIFOStatus](FIFOStatus.md) (indexes 4 and 5).

If the delta and cycle time resolve to an acceleration below the smallest the controller can represent (one position unit per second, per second), the segment faults the motion.

## Examples

```text
AFIFOPushParP=20000  ; queue a parabolic segment that travels 20000 units
```

## See also

- [FIFOPushParA](FIFOPushParA.md) — parabolic segment defined by acceleration
- [FIFOPushCycle](FIFOPushCycle.md) — set the segment duration
- [FIFOType](FIFOType.md) — full FIFO mode description
