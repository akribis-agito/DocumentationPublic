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
  - 2
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
summary: Selects which axis encoder drives each error-mapping dimension.
---
# MapEncoder

Selects which axis encoder drives each error-mapping dimension.

## Overview

`MapEncoder` is a per-dimension array that selects which axis's encoder is used as the position reference for the error-mapping table. For multi-dimensional maps ([MapType](MapType.md) = 2 or 3) each element points the corresponding map axis at a chosen encoder, so a correction can depend on more than one axis's position. Each element accepts a value of `1` or `2`.

`MapEncoder` works with the segment-geometry keywords [MapStartPos](MapStartPos.md), [MapPosGap](MapPosGap.md), and [MapLength](MapLength.md), and with the correction values in [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md). It is an axis-scoped array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

## Examples

```text
AMapEncoder[1]=1     ; first map dimension uses encoder 1
AMapEncoder[2]=2     ; second map dimension uses encoder 2
AMapEncoder[1]      ; query the encoder selected for the first dimension
```

## See also

- [MapType](MapType.md) — selects 1D/2D/3D mapping
- [MapStartPos](MapStartPos.md) — start position of each map segment
- [MapLength](MapLength.md) — number of correction entries per segment
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values indexed by the mapped position
