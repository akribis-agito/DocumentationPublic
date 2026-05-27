---
keyword: MapStartPos
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
summary: Starting position of each error-mapping dimension, in encoder counts.
---
# MapStartPos

Starting position of each error-mapping dimension, in encoder counts.

## Overview

`MapStartPos` is a per-dimension array that defines the position of the first correction point of each error-mapping dimension, in encoder counts. Together with [MapPosGap](MapPosGap.md) (spacing between points) and [MapLength](MapLength.md) (number of points) it fully describes the coordinates of the error-mapping points covered by the [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) entries. [MapEncoder](MapEncoder.md) selects which encoder each dimension is referenced to.

It is an axis-scoped array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

## Examples

```text
AMapStartPos[1]=0        ; first dimension starts at encoder count 0
AMapStartPos[1]=-50000   ; first dimension starts at -50000 counts
AMapStartPos[1]         ; query the start position of the first dimension
```

## See also

- [MapLength](MapLength.md) — number of correction points per dimension
- [MapPosGap](MapPosGap.md) — spacing between correction points
- [MapEncoder](MapEncoder.md) — encoder source for each dimension
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values at each point
