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

`FIFOPosPush` appends one absolute position target to the position-tracking queue. The value written with the command is the target position, in position counts, that is stored. When the queue is active ([FIFOPosFIFOEn](FIFOPosFIFOEn.md) set to `1`), the controller later pops these targets one per cycle and interpolates the motion reference toward each of them.

It can be issued at any time, including during motion, which is how a host streams a continuous trajectory: it keeps pushing targets ahead of playback so the queue never empties.

## How it works

The queue is a cyclic buffer of a fixed depth (see the note below). Each push:

1. Checks for free space. If the queue is full, the push is rejected and an error is returned; nothing is added.
2. Otherwise stores the value at the next free (newest) slot and reduces the free-space count.

The controller consumes targets from the oldest end at the cycle rate set by [FIFOPosCycle](FIFOPosCycle.md). If pushes fall behind playback and the queue empties, the axis holds its last target rather than ending motion. Queue depth, free space, and fullness can be read from [FIFOPosStatus](FIFOPosStatus.md), and the whole queue can be emptied with [FIFOPosClear](FIFOPosClear.md).

The interpolation applied between pushed targets is set by [FIFOPosType](FIFOPosType.md), and the streamed reference is shifted by [FIFOPosPosOf](FIFOPosPosOf.md) / [FIFOPosVelOf](FIFOPosVelOf.md) / [FIFOPosCurrOf](FIFOPosCurrOf.md) as it is applied.

> The queue depth depends on the product. On compact-controller and certain processor builds it holds 32 targets; on the larger drive platform it holds 1024 targets. Use [FIFOPosStatus](FIFOPosStatus.md) to read the actual free space rather than assuming a fixed depth.

## Examples

```text
AFIFOPosTrgt=100000  ; (optional) stage a working value
AFIFOPosPush=100000  ; append target 100000 to the queue
AFIFOPosPush=120000  ; append the next target
```

## See also

- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — enable queue streaming
- [FIFOPosType](FIFOPosType.md) — interpolation mode
- [FIFOPosCycle](FIFOPosCycle.md) — samples per target
- [FIFOPosClear](FIFOPosClear.md) — clear the queue
- [FIFOPosStatus](FIFOPosStatus.md) — queue status
