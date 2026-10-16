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
  ok_motor_on: true
  units: none
  range:
  - 1
  - 60000
  default: 10
  scaling: 1.0
  implemented: final
overrides: {}
summary: Number of correction points along each error-mapping dimension.
last_updated: '2026-10-16'
doc_revision: '2026.06'
---
# MapLength

Number of correction points along each error-mapping dimension.

## Overview

`MapLength` is a per-dimension array (`[1]`/`[2]`/`[3]`) that specifies how many correction points exist along each error-mapping dimension. Together with [MapStartPos](MapStartPos.md) (where the points begin) and [MapPosGap](MapPosGap.md) (spacing) it defines the positional extent covered by the [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) entries: dimension `d` spans `MapStartPos[d] … MapStartPos[d] + (MapLength[d] − 1) × MapPosGap[d]`.

It is an axis-scoped array saved to flash, and can be changed with the motor on, but not while the axis is in motion.

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

### Edge cases

- **Index 0** — invalid; valid indices are `MapLength[1]`/`[2]`/`[3]`.
- **Motor on / in motion at write** — accepted with the motor on at standstill; rejected while the axis is in motion (error 21).
- **Out of range** — values outside `1`–`60 000` per dimension are rejected.
- **Product overflow** — for 2D/3D the **product** of dimensions must fit within the combined [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) banks starting at [MapStartIndex](MapStartIndex.md); the parameter table does not pre-check this product, so an oversize map will read uninitialised entries.
- **`MapType = 0`** — value stored but not consulted.
- **Save** — flash-saveable.

> **Changing the map with the motor on.** A write at standstill takes effect on the next control sample. Because the map corrects the feedback ([Pos](../10-motion/01-kinematics-status/Pos.md)), the corrected position can step once, and the servo moves the axis by that step. To make the change gradual instead (the axis still moves by the whole correction, once as it ramps out and again as it ramps in), first set a non-zero [MapErrOnStep](MapErrOnStep.md) (at its default of `0` the correction switches in and out in one cycle, which is itself a step), then set [MapType](MapType.md) = `0`, wait for the disengage ramp to finish (about `16384 / MapErrOnStep` control cycles; `Pos` equalling `PosBeforeMap` is not a reliable sign, because a small correction can read 0 while the ramp is still running), change the map, and switch `MapType` back on so the correction ramps back in. A non-zero [MapErrOffset](MapErrOffset.md) is forced to 0 while mapping is off and slews back in at [MapErrOffRamp](MapErrOffRamp.md). Writes are refused while the axis is in motion (error 21). On firmware before this change, writes with the motor on are refused (error 22).

## See also

- [MapStartPos](MapStartPos.md) — start position of each dimension
- [MapPosGap](MapPosGap.md) — spacing between correction points
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values at each point
- [MapStartIndex](MapStartIndex.md) — table index where the map begins
- [MapType](MapType.md) — selects 1D/2D/3D (sets which dimensions are used)
