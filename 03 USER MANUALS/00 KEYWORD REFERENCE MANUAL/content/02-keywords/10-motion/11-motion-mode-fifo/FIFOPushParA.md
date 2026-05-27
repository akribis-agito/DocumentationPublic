---
keyword: FIFOPushParA
summary: Pushes a parabolic (constant-acceleration) segment into the FIFO motion queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`FIFOPushParA` appends a **parabolic-by-acceleration** segment (type 4 in [FIFOType](FIFOType.md)) to the queue. The value is the acceleration reference, held constant for the duration of the segment, producing a parabolic position profile. The segment begins from the current profiler velocity. It is the acceleration-based counterpart of [FIFOPushParP](FIFOPushParP.md), which defines the segment by position delta instead.

It is one of the `FIFOPush*` functions used to fill the queue before or during motion. The entry is added at the tail. If the queue is full, the push is rejected with an error.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## How it works

When the controller reaches this segment, it ramps the velocity by the supplied acceleration each control sample for the segment duration, advancing the position reference accordingly. The evolving velocity and acceleration are reported in [FIFOStatus](FIFOStatus.md) (indexes 4 and 5).

The acceleration must be at least the smallest value the controller can resolve — one position unit per second, per second. A push with a smaller magnitude is rejected with an error at push time. The accepted range is -2 000 000 000 to 2 000 000 000.

## Examples

```text
AFIFOPushParA=100000 ; queue a constant-acceleration (parabolic) segment
```

## See also

- [FIFOPushParP](FIFOPushParP.md) — parabolic segment defined by position
- [FIFOPushCycle](FIFOPushCycle.md) — set the segment duration
- [FIFOType](FIFOType.md) — full FIFO mode description
