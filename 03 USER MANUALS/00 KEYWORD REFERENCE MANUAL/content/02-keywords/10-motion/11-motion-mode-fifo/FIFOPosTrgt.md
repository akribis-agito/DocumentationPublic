---
keyword: FIFOPosTrgt
summary: Target position carried by the next FIFO position segment.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 661
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPosTrgt

Target position carried by the next FIFO position segment.

## Overview

`FIFOPosTrgt` is the working position target of the position-tracking subsystem — the absolute position the controller currently interpolates toward. It is expressed in position counts and is not saved to flash; it can be changed at any time, including during motion.

The role of `FIFOPosTrgt` depends on whether the queue is active (see [FIFOPosFIFOEn](FIFOPosFIFOEn.md)):

- **Queue active** (`AFIFOPosFIFOEn=1`): at the start of each cycle the controller overwrites `FIFOPosTrgt` with the oldest target popped from the queue. Reading it then shows the target the axis is currently tracking.
- **Queue bypassed** (`AFIFOPosFIFOEn=0`): the controller does not overwrite it. A host drives the axis by writing `FIFOPosTrgt` directly, once per cycle, and the controller interpolates toward each new value.

When the axis enters position-tracking mode, `FIFOPosTrgt` is initialized to the current position reference so tracking begins from the present location.

## How it works

The target value is interpreted as an absolute position. Before it is applied as the motion reference it is shifted by [FIFOPosPosOf](FIFOPosPosOf.md), so the actual commanded position is the target plus that offset. The interpolation between successive targets is governed by [FIFOPosType](FIFOPosType.md), and the resulting reference is clamped by the software position limits.

## Examples

```text
AFIFOPosTrgt=100000  ; set the working target (used by the next push, or tracked directly)
```

## See also

- [FIFOPosPush](FIFOPosPush.md) — push a target into the queue
- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — enable queue streaming
- [FIFOPosPosOf](FIFOPosPosOf.md) — global position offset
- [FIFOPosStatus](FIFOPosStatus.md) — queue status
