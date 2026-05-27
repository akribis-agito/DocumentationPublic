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

`MapLength` is a per-dimension array (`[1]`/`[2]`/`[3]`) that specifies how many correction points exist along each error-mapping dimension. Together with [MapStartPos](MapStartPos.md) (where the points begin) and [MapPosGap](MapPosGap.md) (spacing) it defines the positional extent covered by the [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) entries: dimension `d` spans `MapStartPos[d] … MapStartPos[d] + (MapLength[d] − 1) × MapPosGap[d]`.

It is an axis-scoped array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

## How it works

`MapLength` controls both the corrected range and how many table entries the map occupies. The firmware uses it directly to compute the **last** table index of each dimension and the **stride** between rows/columns/layers:

| [MapType](MapType.md) | Table entries consumed | Memory layout |
|:---------:|------------------------|---------------|
| 1D | `MapLength[1]` | a single vector |
| 2D | `MapLength[1] × MapLength[2]` | `MapLength[2]` rows of `MapLength[1]` (first dim varies fastest) |
| 3D | `MapLength[1] × MapLength[2] × MapLength[3]` | `MapLength[3]` stacked 2D layers |

Because the entries are addressed as one flat array starting at [MapStartIndex](MapStartIndex.md), the total must fit within the combined [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) banks. Each per-dimension value ranges `1 … 60000`; for 2D/3D the **product** is the real constraint.

## Examples

```text
AMapLength[1]=100    ; first dimension has 100 correction points
AMapLength[1]        ; read the number of points in the first dimension
```

## See also

- [MapStartPos](MapStartPos.md) — start position of each dimension
- [MapPosGap](MapPosGap.md) — spacing between correction points
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values at each point
- [MapStartIndex](MapStartIndex.md) — table index where the map begins
- [MapType](MapType.md) — selects 1D/2D/3D (sets which dimensions are used)
