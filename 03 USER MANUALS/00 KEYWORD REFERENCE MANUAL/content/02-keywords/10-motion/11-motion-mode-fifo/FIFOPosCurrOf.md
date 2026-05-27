---
keyword: FIFOPosCurrOf
summary: Current (torque) feedforward offset added to every FIFO position segment.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 664
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
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPosCurrOf

Current (torque) feedforward offset added to every FIFO position segment.

## Overview

`FIFOPosCurrOf` adds a current (torque) feedforward offset to every FIFO position segment, applying a constant bias current feedforward to all tracked segments. It is the current counterpart of the position offset [FIFOPosPosOf](FIFOPosPosOf.md) and the velocity offset [FIFOPosVelOf](FIFOPosVelOf.md). It is not saved to flash and can be changed at any time.

## Examples

```text
AFIFOPosCurrOf=2000  ; add a uniform current feedforward bias
```

## See also

- [FIFOPosPosOf](FIFOPosPosOf.md) — position offset
- [FIFOPosVelOf](FIFOPosVelOf.md) — velocity feedforward offset
- [FIFOPosTrgt](FIFOPosTrgt.md) — per-segment target position
