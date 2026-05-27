---
keyword: FIFOPosVelOf
summary: Velocity feedforward offset added to every FIFO position segment.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 663
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
  - -1300000000
  - 1300000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPosVelOf

Velocity feedforward offset added to every FIFO position segment.

## Overview

`FIFOPosVelOf` adds a velocity feedforward offset to every FIFO position segment, biasing the velocity feedforward of all tracked segments uniformly. It is the velocity counterpart of the position offset [FIFOPosPosOf](FIFOPosPosOf.md) and the current offset [FIFOPosCurrOf](FIFOPosCurrOf.md). It is not saved to flash and can be changed at any time.

## Examples

```text
FIFOPosVelOf=10000  ; add a uniform velocity feedforward bias
```

## See also

- [FIFOPosPosOf](FIFOPosPosOf.md) — position offset
- [FIFOPosCurrOf](FIFOPosCurrOf.md) — current feedforward offset
- [FIFOPosTrgt](FIFOPosTrgt.md) — per-segment target position
