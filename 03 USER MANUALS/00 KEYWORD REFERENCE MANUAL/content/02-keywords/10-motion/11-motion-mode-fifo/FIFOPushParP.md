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

If the delta and cycle time resolve to an acceleration of magnitude below 16 384 counts/s² (one control-sample frequency at the standard 16 384 Hz rate — the smallest acceleration the per-sample velocity step can resolve), the segment faults the motion.

### Worked example

The shape is easiest to picture in continuous terms: with `FIFOCycleTime = 16384` samples (≈ 1 s at 16384 Hz), a previous velocity of `0`, and `FIFOPushParP = 20000`, the ideal constant acceleration that travels 20 000 units in 1 s starting from rest is `a = 2 × 20000 / 1² = 40000` units/s². The velocity ramps linearly from 0 toward that figure and the position follows the matching parabola.

In firmware the per-sample velocity step is derived with integer arithmetic — the position delta is divided by the cycle time as integers — so the resolved acceleration is quantized and does not always match the textbook value above. If the resolved magnitude falls below 16 384 counts/s² (one control-sample frequency at the standard 16 384 Hz rate — the smallest acceleration the per-sample velocity step can resolve), the segment faults the motion (motor off). The 20 000-unit-over-16 384-sample case shown here in fact resolves to a sub-threshold acceleration and would fault; it is given only to convey the parabola shape, not as a runnable point. For a segment that clears the threshold, choose a delta and cycle time whose integer-resolved acceleration is well above 16 384 counts/s² — for example a 200 000 000-unit delta over a 16 384-sample (≈ 1 s) cycle resolves to roughly 24 000 counts/s² — and read its acceleration as an approximate, quantized figure rather than the exact `2 × delta / t²` value.

## Examples

```text
AFIFOPushParP=20000  ; queue a parabolic segment that travels 20000 units
```

## See also

- [FIFOPushParA](FIFOPushParA.md) — parabolic segment defined by acceleration
- [FIFOPushCycle](FIFOPushCycle.md) — set the segment duration
- [FIFOType](FIFOType.md) — full FIFO mode description
