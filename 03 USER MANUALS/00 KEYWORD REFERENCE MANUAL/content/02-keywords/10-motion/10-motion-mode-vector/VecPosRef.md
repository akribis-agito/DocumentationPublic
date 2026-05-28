---
keyword: VecPosRef
summary: Read-only running position along the vector path (0 to VecAbsTrgt), always positive.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 643
attributes:
  access: ro
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
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# VecPosRef

Read-only running position along the vector path (0 to VecAbsTrgt), always positive.

## Overview

`VecPosRef` is a status parameter that reports the current position reference of the vector motion profile, measured along the vector path. It starts from a value of 0 and, upon end of motion, reaches the value of [VecAbsTrgt](VecAbsTrgt.md). `VecPosRef` is always positive. Its time derivative is reported by [VecdPosRef](VecdPosRef.md).

## How it works

`VecPosRef` is the master coordinate of the whole vector move. A vector move runs a single velocity profile along the path; each control cycle the controller advances the path velocity (shaped by [VecSpeed](VecSpeed.md), [VecAccel](VecAccel.md), [VecDecel](VecDecel.md) and [VecJerk](VecJerk.md)) and accumulates it into `VecPosRef`, so this one number climbs monotonically from 0 to [VecAbsTrgt](VecAbsTrgt.md).

The accumulation is carried internally at higher precision so that fractional path motion builds up without drift; `VecPosRef` is reported by rounding that value back to user units. An optional path-position filter can be applied to smooth the reference before it is split across the axes.

Each cycle the controller converts `VecPosRef` into the per-axis position references according to the geometry ([VecType](VecType.md)):

- **Linear** — each member axis is set to its start point plus the path fraction (`VecPosRef ÷ VecAbsTrgt`) times that axis's total travel, so the axes trace the straight line together.
- **Arc** — `VecPosRef ÷ radius` gives the angle swept from the start angle (in the direction set by [VecArcDir](VecArcDir.md)); the two axis positions are then the center coordinate plus radius × cosine / sine of that angle.

Because all axes are derived from this single coordinate, they remain exactly coordinated on the path regardless of their individual speeds. The move is declared complete when `VecPosRef` reaches `VecAbsTrgt` and the path velocity has fallen to (near) zero, at which point the member axes are snapped to their exact end points.

## Examples

```text
AVecPosRef          ; read the current position along the vector path
```

## See also

- [VecAbsTrgt](VecAbsTrgt.md) — total path distance (end value of `VecPosRef`)
- [VecdPosRef](VecdPosRef.md) — derivative of `VecPosRef` (path speed)
