---
keyword: MapPosGap
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 325
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 4
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 1
  - 8000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
summary: Encoder-count spacing between adjacent error-mapping points.
---
# MapPosGap

Encoder-count spacing between adjacent error-mapping points.

## Overview

`MapPosGap` is a per-dimension array that sets the position spacing, in encoder counts, between consecutive correction points along each error-mapping dimension. A larger gap spreads the same number of points across a wider positional range, giving coarser resolution. Together with [MapStartPos](MapStartPos.md) (start) and [MapLength](MapLength.md) (count) it defines the coordinates of the points stored in [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md).

It is an axis-scoped array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

## Examples

```text
AMapPosGap[1]=1000   ; correction points 1000 encoder counts apart
AMapPosGap[1]       ; query the spacing for the first dimension
```

## See also

- [MapLength](MapLength.md) — number of correction points per dimension
- [MapStartPos](MapStartPos.md) — start position of each dimension
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values at each point
