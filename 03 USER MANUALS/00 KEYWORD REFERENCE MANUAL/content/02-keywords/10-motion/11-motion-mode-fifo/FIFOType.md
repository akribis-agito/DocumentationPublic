---
keyword: FIFOType
summary: Read-only array reporting the type of each entry stored in the FIFO motion queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 281
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 129
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 5
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOType

Read-only array reporting the type of each entry stored in the FIFO motion queue.

## Overview

`FIFOType` is the hub page for FIFO (First In, First Out) motion mode and reports the entry type of each element currently held in the FIFO. It works together with [FIFOValue](FIFOValue.md), which carries the matching data value for each entry.

FIFO is a special motion mode in which the controller performs a sequence of linear and parabolic segments, defined by the user before the motion and optionally also during the motion. The motion is created from motion segments stored in a FIFO memory. Segment definitions can be pushed to the FIFO at any time (before or during the motion), provided the FIFO is not full; if the FIFO is full, the push operation is rejected with a suitable error.

If, during a motion in this mode, the controller reaches and completes the last element in the FIFO and no new element has been pushed, the motion is automatically ended. The motion can also be stopped using the [Stop](../04-motion-command/Stop.md) or the [StopFIFO](StopFIFO.md) functions: `Stop` decelerates to zero speed, while `StopFIFO` makes the currently executing motion segment the last segment.

This page describes the FIFO motion mode and all related keywords: [FIFOValue](FIFOValue.md), [FIFOStatus](FIFOStatus.md), [FIFOCycleTime](FIFOCycleTime.md), [FIFOPushCycle](FIFOPushCycle.md), [FIFOPushLinP](FIFOPushLinP.md), [FIFOPushLinV](FIFOPushLinV.md), [FIFOPushParP](FIFOPushParP.md), [FIFOPushParA](FIFOPushParA.md), [FIFORemove](FIFORemove.md), [FIFOClear](FIFOClear.md), and [StopFIFO](StopFIFO.md).

## How it works

Each motion segment can be of type **Velocity** or **Acceleration**:

- A **Velocity** type segment is one in which the velocity reference is constant.
- An **Acceleration** type segment is one in which the acceleration reference is constant.

The time length of each segment ([FIFOCycleTime](FIFOCycleTime.md)) is a fixed number of control samples. It can be modified at any time the controller is ending one segment and starting a new one.

The FIFO holds up to 512 entries. Each entry has a type and a value. If all entries are motion entries, the FIFO can hold up to 512 motion segments. The FIFO can be re-filled over the communication channel during the motion sequence.

For a velocity-type motion segment:

- Segment duration is given in number of samples (the sample time of the control loop) and is stored in [FIFOCycleTime](FIFOCycleTime.md).
- The segment starts naturally from the last position reference.
- The motion can be defined by a linear position delta. The final target position is calculated from the given delta, which is scaled by the controller `SAMPLING_FREQUENCY` (typically 16384 Hz).

> **Documentation pending:** The full enumeration of `FIFOType` entry codes (range 0–5) and the complete segment-definition details were truncated in the source reference. Verify the exact type codes against current firmware before relying on specific values.

## Examples

```text
AFIFOType[1]        ; query the type of the first FIFO entry
```

## See also

- [FIFOValue](FIFOValue.md) — value paired with each FIFO entry type
- [FIFOStatus](FIFOStatus.md) — FIFO queue status
- [FIFOCycleTime](FIFOCycleTime.md) — segment duration in control samples
- [StopFIFO](StopFIFO.md) — end the current segment as the last one
- [Stop](../04-motion-command/Stop.md) — decelerate to zero speed
