---
keyword: FIFOPosType
summary: Selects the operating mode of the FIFO position-tracking feature.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 659
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
# FIFOPosType

Selects the operating mode of the FIFO position-tracking feature.

## Overview

`FIFOPosType` selects the operating mode of the FIFO position-tracking feature, choosing how position segments pushed into the queue are interpreted. It is the configuration keyword for the FIFO position-tracking subsystem, enabled by [FIFOPosFIFOEn](FIFOPosFIFOEn.md) and fed by [FIFOPosPush](FIFOPosPush.md). It is saved to flash and cannot be changed while the axis is in motion.

## Examples

```text
AFIFOPosType=0       ; select FIFO position-tracking mode 0
```

## See also

- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — enable FIFO position tracking
- [FIFOPosPush](FIFOPosPush.md) — push a position segment
- [FIFOPosStatus](FIFOPosStatus.md) — position-tracking queue status
