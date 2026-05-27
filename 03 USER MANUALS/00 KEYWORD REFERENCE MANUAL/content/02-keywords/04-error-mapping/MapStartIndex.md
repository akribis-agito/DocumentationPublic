---
keyword: MapStartIndex
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 321
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 1
  - 300000
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
summary: MapTable index where the active error-mapping data begins.
---
# MapStartIndex

MapTable index where the active error-mapping data begins.

## Overview

`MapStartIndex` sets the [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) index at which the active error-mapping data begins. The correction values for a given map are not required to start at the first table element, so this lets several maps share the table region or lets unused leading entries be skipped. Correction proceeds from this index across the points defined by [MapStartPos](MapStartPos.md), [MapPosGap](MapPosGap.md), and [MapLength](MapLength.md), for the dimensions selected by [MapType](MapType.md).

It is an axis-scoped parameter saved to flash, and cannot be changed while the axis is in motion or the motor is on.

## How it works

`MapStartIndex` is the base index of every table read during correction — the firmware's table-fetch routine maps a single 1-based index onto the chained banks (`MapTable`, then `MapTableB…MapTableE`), so the index space is **continuous across all five banks** and `MapStartIndex` may legitimately point into any of them. The per-dimension lookup adds offsets to this base:

- **1D:** entries `MapStartIndex … MapStartIndex + MapLength[1] − 1`.
- **2D:** `index = MapStartIndex + column × MapLength[1] + row` (first dimension varies fastest).
- **3D:** `index = MapStartIndex + layer × MapLength[1] × MapLength[2] + column × MapLength[1] + row`.

The map must fit within the available table size from `MapStartIndex` onward; the upper bound of the keyword tracks the combined bank size. Because indices are **1-based**, `MapStartIndex = 1` selects `MapTable[1]` as the first entry.

## Examples

```text
AMapStartIndex=1     ; mapping data starts at MapTable[1]
AMapStartIndex=5000  ; mapping data starts 5000 entries in (may fall in a later bank)
AMapStartIndex       ; read the current start index
```

## See also

- [MapType](MapType.md) — selects 1D/2D/3D mapping
- [MapStartPos](MapStartPos.md) — start position of each dimension
- [MapLength](MapLength.md) — number of points per dimension
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — table that this index points into
