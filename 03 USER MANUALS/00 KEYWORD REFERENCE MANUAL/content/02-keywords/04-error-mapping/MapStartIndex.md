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
  ok_motor_on: true
  units: none
  range:
  - 1
  - 300000
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
summary: MapTable index where the active error-mapping data begins.
last_updated: '2026-10-17'
doc_revision: '2026.06'
---
# MapStartIndex

MapTable index where the active error-mapping data begins.

## Overview

`MapStartIndex` sets the [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) index at which the active error-mapping data begins. The correction values for a given map are not required to start at the first table element, so this lets several maps share the table region or lets unused leading entries be skipped. Correction proceeds from this index across the points defined by [MapStartPos](MapStartPos.md), [MapPosGap](MapPosGap.md), and [MapLength](MapLength.md), for the dimensions selected by [MapType](MapType.md).

It is an axis-scoped parameter saved to flash, and can be changed with the motor on, but not while the axis is in motion.

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

### Edge cases

- **Motor on / in motion at write** — accepted with the motor on at standstill; rejected while the axis is in motion (error 21).
- **Out of range** — values outside `1`–`300 000` are rejected.
- **Past the table** — values beyond the combined bank size dispatch to uninitialised memory; combine carefully with [MapLength](MapLength.md).
- **`MapType = 0`** — value stored but not consulted.
- **1-based** — `MapStartIndex = 1` points at `MapTable[1]`. Index `0` is invalid.
- **Save** — flash-saveable.

> **Changing the map with the motor on.** A write at standstill takes effect on the next control sample. Because the map corrects the feedback ([Pos](../10-motion/01-kinematics-status/Pos.md)), the corrected position can step once, and the servo moves the axis by that step. To make the change gradual instead (the axis still moves by the whole correction, once as it ramps out and again as it ramps in), first set a small [MapErrOnStep](MapErrOnStep.md) (the ramp takes `16384 / MapErrOnStep` cycles, so e.g. `16` gives about 1024 cycles; `0`, the default, and `16384` switch the whole correction in one cycle, which is itself a step), then set [MapType](MapType.md) = `0`, wait for the disengage ramp to finish (about `16384 / MapErrOnStep` control cycles; `Pos` equalling `PosBeforeMap` is not a reliable sign, because a small correction can read 0 while the ramp is still running), change the map, and switch `MapType` back on so the correction ramps back in. The applied offset is held at 0 once the disengage ramp has finished (the [MapErrOffset](MapErrOffset.md) keyword keeps its value) and slews back in at [MapErrOffRamp](MapErrOffRamp.md) after mapping is switched back on. Writes are refused while the axis is in motion (error 21). On firmware before this change, writes with the motor on are refused (error 22).

## See also

- [MapType](MapType.md) — selects 1D/2D/3D mapping
- [MapStartPos](MapStartPos.md) — start position of each dimension
- [MapLength](MapLength.md) — number of points per dimension
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — table that this index points into
