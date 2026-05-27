---
keyword: FIFOPosFIFOEn
summary: Enables or disables FIFO position-tracking mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 665
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPosFIFOEn

Enables or disables FIFO position-tracking mode.

## Overview

`FIFOPosFIFOEn` switches the queue feeding the position-tracking trajectory on or off. While the axis runs in position-tracking mode, the working target ([FIFOPosTrgt](FIFOPosTrgt.md)) is the value the controller interpolates toward each cycle. This keyword controls where that working target comes from:

- `1` — the queue is active. At the start of every cycle the controller pops the oldest target from the position queue and adopts it as the new working target. This is the normal streaming mode: a host pushes a stream of targets with [FIFOPosPush](FIFOPosPush.md) and the controller plays them back.
- `0` — the queue is bypassed. The controller does not pop from the queue; it simply uses whatever value currently sits in [FIFOPosTrgt](FIFOPosTrgt.md). A host can then drive the axis by writing `FIFOPosTrgt` directly each cycle.

It is saved to flash and cannot be changed while the axis is in motion.

## How it works

Position tracking always runs on a fixed cycle whose length in servo samples is set by [FIFOPosCycle](FIFOPosCycle.md). At the first sample of each cycle:

1. If `FIFOPosFIFOEn` is `1` and the queue is not empty, the oldest queued target is removed and copied into the working target. If the queue is empty, the previous working target is held (the axis keeps its last commanded position rather than ending motion).
2. The interpolation rule selected by [FIFOPosType](FIFOPosType.md) is set up for the new cycle.

For the remaining samples of the cycle, the position reference is interpolated toward the working target and shifted by the offsets [FIFOPosPosOf](FIFOPosPosOf.md), [FIFOPosVelOf](FIFOPosVelOf.md), and [FIFOPosCurrOf](FIFOPosCurrOf.md). The result is always clamped by the software position limits, and the axis still decelerates and waits if it runs into a forward or reverse limit switch.

Unlike the main FIFO mode (see [FIFOType](FIFOType.md)), which automatically ends the motion when its queue runs dry, position tracking does not self-terminate on an empty queue — it holds the last target. Use [Stop](../04-motion-command/Stop.md) to decelerate to rest.

## Examples

```text
AFIFOPosFIFOEn=1     ; stream targets from the queue
AFIFOPosFIFOEn=0     ; follow FIFOPosTrgt written directly each cycle
```

## See also

- [FIFOPosType](FIFOPosType.md) — interpolation mode
- [FIFOPosPush](FIFOPosPush.md) — push a position target
- [FIFOPosTrgt](FIFOPosTrgt.md) — working target
- [FIFOPosCycle](FIFOPosCycle.md) — samples per target (cycle length)
- [FIFOPosStatus](FIFOPosStatus.md) — queue status
