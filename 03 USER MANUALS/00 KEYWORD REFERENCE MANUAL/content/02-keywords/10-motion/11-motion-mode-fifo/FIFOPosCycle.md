---
keyword: FIFOPosCycle
summary: Cycle time, in servo samples, between consecutive FIFO position segments.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`FIFOPosCycle` sets the cycle time, in servo samples, between consecutive position segments popped from the FIFO position queue and applied as the axis reference. It controls the playback rate of the position-tracking trajectory enabled by [FIFOPosFIFOEn](FIFOPosFIFOEn.md). It is saved to flash and cannot be changed while the axis is in motion.

## Examples

```text
FIFOPosCycle=16     ; apply a new position segment every 16 servo samples
```

## See also

- [FIFOPosType](FIFOPosType.md) — select the position-tracking mode
- [FIFOPosPush](FIFOPosPush.md) — push a position segment
- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — enable FIFO position tracking
