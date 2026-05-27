---
keyword: MapLength
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 324
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
  - 60000
  default: 10
  scaling: 1.0
  implemented: final
overrides: {}
summary: Number of correction points along each error-mapping dimension.
---
# MapLength

Number of correction points along each error-mapping dimension.

## Overview

`MapLength` is a per-dimension array that specifies how many correction points exist along each error-mapping dimension. Together with [MapStartPos](MapStartPos.md) (where the points begin) and [MapPosGap](MapPosGap.md) (how far apart they are) it defines the positional extent covered by the [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) entries. The number of map points determines how many `MapTable` entries are consumed by the dimension (the value ranges from `1` to `60000`).

It is an axis-scoped array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

## Examples

```text
AMapLength[1]=100    ; first dimension has 100 correction points
AMapLength[1]       ; query the number of points in the first dimension
```

## See also

- [MapStartPos](MapStartPos.md) — start position of each dimension
- [MapPosGap](MapPosGap.md) — spacing between correction points
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values at each point
