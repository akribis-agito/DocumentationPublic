---
keyword: MapEncoder
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 322
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
  - 8
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
summary: Selects which axis encoder drives each error-mapping dimension.
---
# MapEncoder

Selects which axis encoder drives each error-mapping dimension.

## Overview

`MapEncoder` is a per-dimension array that selects which encoder supplies the *uncorrected* position used to look up the error-mapping table. Index `[1]` is the first (and for 1D, only) dimension; `[2]` and `[3]` add the second and third dimensions for [MapType](MapType.md) = 2 and 3. The looked-up encoder reading is what indexes the table — see [MapStartPos](MapStartPos.md)/[MapPosGap](MapPosGap.md)/[MapLength](MapLength.md) for how the index is formed — so a 2D/3D map can make the correction depend on more than one axis's position.

`MapEncoder` is an axis-scoped array saved to flash and cannot be changed in motion or motor-on.

## How it works

Each element encodes both the *axis* and the *main-or-auxiliary* selection in one integer. The controller decodes it during background setup to select the chosen encoder's pre-correction reading:

- **Odd value** → the **main** encoder of axis number `value >> 1`.
- **Even value** → the **auxiliary** encoder ([AuxPos](../10-motion/01-kinematics-status/AuxPos.md)) of axis number `(value >> 1) − 1`.

So the mapping is:

| Value | Source encoder |
|:-----:|----------------|
| 1 | Axis A main encoder |
| 2 | Axis A auxiliary encoder |
| 3 | Axis B main encoder |
| 4 | Axis B auxiliary encoder |
| … | … (pattern repeats per axis) |

The default is `1` (this axis's own main encoder). For the table-building/correction routine to accept the map, `MapEncoder[1]` **must** point to this axis's own main encoder; for 2D/3D, the second/third entries must point to **main** encoders of standing, motor-on axes (a wrong selection raises a "must be main encoders" / "must be first encoder" event). The valid range spans `1 … (number of axes) × 2`; on a single-axis controller only `1` and `2` are meaningful.

## Examples

```text
AMapEncoder[1]=1     ; first dimension uses this axis's main encoder (typical)
AMapEncoder[2]=3     ; second dimension uses axis B's main encoder (2D map)
AMapEncoder[1]       ; read the encoder selected for the first dimension
```

### Edge cases

- **Index 0** — invalid; valid indices are `MapEncoder[1]`/`[2]`/`[3]`.
- **Motor on / in motion at write** — rejected while the motor is on or the axis is in motion.
- **Out of range** — values outside `1`–`number-of-axes × 2` are rejected.
- **`MapEncoder[1]` wrong** — must point at this axis's own main encoder for the table build to accept the map; otherwise the build raises a "must be first encoder" event.
- **2D/3D requires main encoders** — additional encoders for 2D/3D must be **main** encoders of motor-on, standing axes; auxiliary encoders for `[2]`/`[3]` are rejected with a "must be main encoders" event.
- **`MapType = 0`** — value stored but not consulted.
- **Save** — flash-saveable.

## See also

- [MapType](MapType.md) — selects 1D/2D/3D mapping
- [MapStartPos](MapStartPos.md) — start position of each map segment
- [MapLength](MapLength.md) — number of correction entries per segment
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values indexed by the mapped position
- [Pos](../10-motion/01-kinematics-status/Pos.md) / [PosBeforeMap](PosBeforeMap.md) — corrected and pre-correction feedback
- [AuxPos](../10-motion/01-kinematics-status/AuxPos.md) — auxiliary encoder reading, selectable as a map source
