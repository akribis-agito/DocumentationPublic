---
keyword: FIFOPosCycle
summary: Cycle time, in servo samples, between consecutive FIFO position segments.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 660
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 1
  - 1600
  default: 16
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPosCycle

Cycle time, in servo samples, between consecutive FIFO position segments.

## Overview

`FIFOPosCycle` sets the cycle length, in servo samples, of the position-tracking trajectory: the controller takes one new position target per cycle and interpolates between targets over the samples in between. It therefore sets the time spacing of the streamed targets — the playback rate of the trajectory enabled by [FIFOPosFIFOEn](FIFOPosFIFOEn.md).

The value is given in control-loop samples. The control loop runs at a fixed sampling frequency (typically 16384 Hz), so a cycle of N samples corresponds to N / 16384 seconds. With the default of 16 samples, a new target is consumed roughly every 1 ms.

The range is 1 to 1600 samples (default 16). It is saved to flash and cannot be changed while the axis is in motion.

## How it works

At the first sample of each cycle the controller pops the next target from the queue (or holds the last one if the queue is empty) and prepares the interpolation set by [FIFOPosType](FIFOPosType.md). Over the remaining samples of the cycle it advances the position reference smoothly toward that target:

- A larger `FIFOPosCycle` spaces the targets further apart in time, giving slower motion between points and more interpolation samples per point.
- A smaller value plays the targets back faster, leaving fewer interpolation samples per point.

A host streaming targets must push them at a rate that keeps the queue supplied at the chosen cycle length; otherwise the queue drains and the axis holds its last target. Queue occupancy can be monitored through [FIFOPosStatus](FIFOPosStatus.md).

## Examples

```text
AFIFOPosCycle=16     ; consume one target every 16 samples (~1 ms at 16384 Hz)
AFIFOPosCycle=164    ; one target every ~10 ms
```

## See also

- [FIFOPosType](FIFOPosType.md) — interpolation mode
- [FIFOPosPush](FIFOPosPush.md) — push a position target
- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — enable FIFO position tracking
- [FIFOPosStatus](FIFOPosStatus.md) — queue status
