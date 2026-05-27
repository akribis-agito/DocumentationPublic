---
keyword: FIFOPosFIFOEn
summary: Enables or disables FIFO position-tracking mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`FIFOPosFIFOEn` enables or disables FIFO position-tracking mode. When set to a non-zero value, the controller reads position segments from the FIFO position queue and uses them as the axis reference trajectory. The interpretation of the segments is set by [FIFOPosType](FIFOPosType.md), and segments are loaded with [FIFOPosPush](FIFOPosPush.md). It is saved to flash and cannot be changed while the axis is in motion.

## Examples

```text
FIFOPosFIFOEn=1     ; enable FIFO position tracking
FIFOPosFIFOEn=0     ; disable FIFO position tracking
```

## See also

- [FIFOPosType](FIFOPosType.md) — select the position-tracking mode
- [FIFOPosPush](FIFOPosPush.md) — push a position segment
- [FIFOPosCycle](FIFOPosCycle.md) — segment cycle time
