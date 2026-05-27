---
keyword: MapType
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 320
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 3
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
summary: Selects the error-mapping dimension (off, 1D, 2D, or 3D).
---
# MapType

Selects the error-mapping dimension (off, 1D, 2D, or 3D).

## Overview

`MapType` selects the error-mapping correction mode applied to the axis position feedback. Error mapping corrects the measured feedback ([Pos](../10-motion/01-kinematics-status/Pos.md)) rather than the command ([PosRef](../10-motion/01-kinematics-status/PosRef.md)), so a non-zero value enables position-error compensation using the correction values stored in the [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) arrays. The valid range is `0` to `3`, corresponding to mapping off, 1D, 2D, and 3D.

The geometry of the map is defined by [MapStartPos](MapStartPos.md), [MapPosGap](MapPosGap.md), and [MapLength](MapLength.md); [MapEncoder](MapEncoder.md) chooses the encoder source per segment; and [MapStartIndex](MapStartIndex.md) selects the first active segment. The uncorrected position is available as [PosBeforeMap](PosBeforeMap.md) for diagnostics. `MapType` is axis-scoped, is not saved to flash, and cannot be changed while the axis is in motion.

## Examples

```text
AMapType=1           ; enable 1D error mapping
AMapType=0           ; disable error mapping
AMapType            ; query the active mapping mode
```

## See also

- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values applied by mapping
- [MapEncoder](MapEncoder.md) — encoder source used for each map segment
- [MapStartIndex](MapStartIndex.md) — first active map segment
- [PosBeforeMap](PosBeforeMap.md) — feedback position before correction is applied
- [Pos](../10-motion/01-kinematics-status/Pos.md) — corrected feedback position that mapping adjusts
