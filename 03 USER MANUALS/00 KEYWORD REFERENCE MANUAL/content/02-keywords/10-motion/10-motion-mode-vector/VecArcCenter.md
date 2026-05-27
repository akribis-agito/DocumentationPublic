---
keyword: VecArcCenter
summary: Per-axis coordinate of the arc center, from which the controller derives the arc radius.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 633
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# VecArcCenter

Per-axis coordinate of the arc center, from which the controller derives the arc radius.

## Overview

For an arc vector ([VecType](VecType.md) = 1), `VecArcCenter` defines the location of the arc center so the controller can calculate the radius. Like all vector-motion keywords, it is per axis: the coordinate of the arc center is given by the `VecArcCenter` of the two member axes that form the arc plane. It must be set up before motion, together with [VecArcDir](VecArcDir.md) (sweep direction) and [VecNumCircles](VecNumCircles.md) (number of revolutions).

It is saved to flash and cannot be modified while in motion.

## Examples

```text
AVecArcCenter=50000  ; this axis's coordinate of the arc center (user units)
```

## See also

- [VecType](VecType.md) — selects linear vs. arc vector
- [VecArcDir](VecArcDir.md) — arc sweep direction (CW/CCW)
- [VecNumCircles](VecNumCircles.md) — number of full arcs to run
