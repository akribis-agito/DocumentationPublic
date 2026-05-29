---
keyword: MapStartPos
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 323
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
summary: Starting position of each error-mapping dimension, in encoder counts.
---
# MapStartPos

Starting position of each error-mapping dimension, in encoder counts.

## Overview

`MapStartPos` is a per-dimension array (`[1]` first dimension, `[2]` second, `[3]` third) that defines the position of the first correction point of each error-mapping dimension, in **encoder counts** (pre-correction, i.e. measured on the [MapEncoder](MapEncoder.md)-selected source). Together with [MapPosGap](MapPosGap.md) (spacing) and [MapLength](MapLength.md) (number of points) it fully describes the lookup grid covered by the [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) entries.

It is an axis-scoped array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

## How it works

Each control cycle the firmware takes the selected encoder's uncorrected reading and converts it to a fractional table index for that dimension:

$$
\text{index}_f = \frac{\text{PosBeforeCorrection} - \text{MapStartPos}[d]}{\text{MapPosGap}[d]}
$$

The covered range of dimension `d` is therefore `MapStartPos[d]` up to `MapStartPos[d] + (MapLength[d] − 1) × MapPosGap[d]`. Readings **at or below** `MapStartPos[d]` clamp to the first point of that dimension; readings at or above the top clamp to the last point — outside the range the correction is held flat (no extrapolation). So `MapStartPos` should be set so the table brackets the full travel you want corrected.

## Examples

```text
AMapStartPos[1]=0        ; first dimension starts at encoder count 0
AMapStartPos[1]=-50000   ; first dimension starts at -50000 counts
AMapStartPos[1]          ; read the start position of the first dimension
```

## Changes between versions

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Data type | 32-bit (`long`) | **64-bit (`long long`)** |
| Range | ±2,147,483,647 | ±2,251,799,813,685,247 |

In **v5** the position pipeline is 64-bit, so the map start positions are stored as 64-bit values to match the wider [Pos](../10-motion/01-kinematics-status/Pos.md)/[PosBeforeMap](PosBeforeMap.md) range. v5 is **central-i only**; on standalone `MapStartPos` remains the 32-bit v4 value.

## See also

- [MapLength](MapLength.md) — number of correction points per dimension
- [MapPosGap](MapPosGap.md) — spacing between correction points
- [MapEncoder](MapEncoder.md) — encoder source for each dimension
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values at each point
- [Pos](../10-motion/01-kinematics-status/Pos.md) / [PosBeforeMap](PosBeforeMap.md) — corrected and pre-correction feedback
