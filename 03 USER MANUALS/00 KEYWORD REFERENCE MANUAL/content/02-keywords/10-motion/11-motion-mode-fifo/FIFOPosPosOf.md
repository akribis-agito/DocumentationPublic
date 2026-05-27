---
keyword: FIFOPosPosOf
summary: Position offset added to every FIFO position segment.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 662
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
# FIFOPosPosOf

Position offset added to every FIFO position segment.

## Overview

`FIFOPosPosOf` adds a position offset to every FIFO position segment before it is applied as the axis reference target. It allows a global shift of the entire FIFO position-tracking trajectory without modifying the individual segment data in [FIFOPosTrgt](FIFOPosTrgt.md). It is the position-offset counterpart of the velocity offset [FIFOPosVelOf](FIFOPosVelOf.md) and the current offset [FIFOPosCurrOf](FIFOPosCurrOf.md). It is not saved to flash and can be changed at any time.

## Examples

```text
AFIFOPosPosOf=5000   ; shift the whole position trajectory by 5000
```

## See also

- [FIFOPosTrgt](FIFOPosTrgt.md) — per-segment target position
- [FIFOPosVelOf](FIFOPosVelOf.md) — velocity feedforward offset
- [FIFOPosCurrOf](FIFOPosCurrOf.md) — current feedforward offset
