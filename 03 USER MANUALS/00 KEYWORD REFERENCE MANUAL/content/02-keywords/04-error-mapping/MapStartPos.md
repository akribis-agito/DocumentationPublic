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
summary: Starting position of each error-mapping dimension, in encoder counts.
last_updated: '2026-10-17'
doc_revision: '2026.06'
---
# MapStartPos

Starting position of each error-mapping dimension, in encoder counts.

## Overview

`MapStartPos` is a per-dimension array (`[1]` first dimension, `[2]` second, `[3]` third) that defines the position of the first correction point of each error-mapping dimension, in **encoder counts** (pre-correction, i.e. measured on the [MapEncoder](MapEncoder.md)-selected source). Together with [MapPosGap](MapPosGap.md) (spacing) and [MapLength](MapLength.md) (number of points) it fully describes the lookup grid covered by the [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) entries.

It is an axis-scoped array saved to flash, and can be changed with the motor on, but not while the axis is in motion.

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

### Edge cases

- **Index 0** — invalid; valid indices are `MapStartPos[1]` (1D), `[2]` (2D), `[3]` (3D). `MapStartPos[0]` does not exist.
- **Motor on / in motion at write** — accepted with the motor on at standstill; rejected while the axis is in motion (error 21).
- **`MapType = 0`** — the value is stored but not consulted; only the active dimensions of [MapType](MapType.md) are used (1D → only `[1]`; 2D → `[1]` and `[2]`; 3D → all three).
- **Below the range** — readings ≤ `MapStartPos` clamp to the first correction entry (held flat, no extrapolation).
- **Beyond the range** — readings ≥ `MapStartPos + (MapLength − 1) × MapPosGap` clamp to the last correction entry.
- **Encoder counts** — units are pre-correction encoder counts on the selected [MapEncoder](MapEncoder.md), NOT user units.
- **Save** — flash-saveable.
- **Platform** — v5 widens to 64-bit; v4 is 32-bit.

## Changes between versions

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Data type | 32-bit (`long`) | **64-bit (`long long`)** |
| Range | ±2,147,483,647 | ±2,251,799,813,685,247 |

In **v5** the position pipeline is 64-bit, so the map start positions are stored as 64-bit values to match the wider [Pos](../10-motion/01-kinematics-status/Pos.md)/[PosBeforeMap](PosBeforeMap.md) range. v5 is **central-i only**; on standalone `MapStartPos` remains the 32-bit v4 value.

> **Changing the map with the motor on.** A write at standstill takes effect on the next control sample. Because the map corrects the feedback ([Pos](../10-motion/01-kinematics-status/Pos.md)), the corrected position can step once, and the servo moves the axis by that step. To make the change gradual instead (the axis still moves by the whole correction, once as it ramps out and again as it ramps in), first set a small [MapErrOnStep](MapErrOnStep.md) (the ramp takes `16384 / MapErrOnStep` cycles, so e.g. `16` gives about 1024 cycles; `0`, the default, and `16384` switch the whole correction in one cycle, which is itself a step), then set [MapType](MapType.md) = `0`, wait for the disengage ramp to finish (about `16384 / MapErrOnStep` control cycles; `Pos` equalling `PosBeforeMap` is not a reliable sign, because a small correction can read 0 while the ramp is still running), change the map, and switch `MapType` back on so the correction ramps back in. The applied offset is held at 0 once the disengage ramp has finished (the [MapErrOffset](MapErrOffset.md) keyword keeps its value) and slews back in at [MapErrOffRamp](MapErrOffRamp.md) after mapping is switched back on. Writes are refused while the axis is in motion (error 21). On firmware before this change, writes with the motor on are refused (error 22).

## See also

- [MapLength](MapLength.md) — number of correction points per dimension
- [MapPosGap](MapPosGap.md) — spacing between correction points
- [MapEncoder](MapEncoder.md) — encoder source for each dimension
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values at each point
- [Pos](../10-motion/01-kinematics-status/Pos.md) / [PosBeforeMap](PosBeforeMap.md) — corrected and pre-correction feedback
