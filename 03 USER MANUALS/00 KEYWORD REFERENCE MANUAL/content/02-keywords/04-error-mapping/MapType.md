---
keyword: MapType
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`MapType` selects the error-mapping correction mode applied to the axis position feedback. Error mapping corrects the measured feedback ([Pos](../10-motion/01-kinematics-status/Pos.md)) rather than the command ([PosRef](../10-motion/01-kinematics-status/PosRef.md)), so a non-zero value enables position-error compensation using the correction values stored in the [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) arrays. The valid range is `0` to `3`.

The geometry of the map is defined by [MapStartPos](MapStartPos.md), [MapPosGap](MapPosGap.md), and [MapLength](MapLength.md); [MapEncoder](MapEncoder.md) chooses the encoder source per dimension; and [MapStartIndex](MapStartIndex.md) selects the first active table entry. The uncorrected position is available as [PosBeforeMap](PosBeforeMap.md) for diagnostics. `MapType` is axis-scoped, is not saved to flash, and cannot be changed while the axis is in motion.

## How it works

`MapType` is read once per control cycle in the feedback pipeline (in the control interrupt) to choose the correction branch. The supported values are fixed in firmware:

| `MapType` | Mode | Lookup dimensions | Interpolation |
|:---------:|------|-------------------|---------------|
| 0 | Off (`NO_ENCODER_MAPPING`) | none — `Pos = PosBeforeMap` | none |
| 1 | 1D (`ENCODER_MAPPING_1D`) | first encoder only | linear (2-point) |
| 2 | 2D (`ENCODER_MAPPING_2D`) | first encoder = row, second = column | bilinear (4-point) |
| 3 | 3D (`ENCODER_MAPPING_3D`) | first/second/third encoders | trilinear (8-point) |

Each cycle the firmware records `PosBeforeMap = EncoderPos` (the decoded main encoder), then — if the motor is **not** in simulation — runs the selected branch to compute a correction and forms `Pos = EncoderPos + (ramped correction)`. `DeltaPos` is recomputed afterwards so the velocity estimate also reflects the corrected position. In **simulation** mode mapping is skipped entirely (`Pos = EncoderPos`) to avoid the closed loop `EncoderPos = PosRef → Pos = f(EncoderPos) → PosRef = Pos` that would form in motor-off.

### Internal vs. requested type, and the engage/disengage ramp

Writing `MapType` does **not** switch the correction on or off abruptly. The firmware keeps a separate internal copy (`gsMapTypeInternal`) and a 0..1 ramp counter:

- **Engaging** (write `MapType` 1/2/3 from 0): the internal type is set immediately and the ramp counter starts at 0, climbing toward full scale at a rate set by [MapErrOnStep](MapErrOnStep.md). Until it reaches full scale the correction is scaled by `counter / SAMPLES_PER_SECOND`, so the correction (and the [MapErrOffset](MapErrOffset.md) component) fades in smoothly with no position step.
- **Disengaging** (write `MapType` 0): the user value goes to 0 but the internal type stays active and the correction ramps **down**; only when the counter reaches 0 does the internal type revert to off. With `MapErrOnStep = 0` the change is immediate (one cycle).

This ramp logic is shared by all of `MapType`, [MapErrOnStep](MapErrOnStep.md), [MapErrOffset](MapErrOffset.md), and [MapErrOffRamp](MapErrOffRamp.md). Engaging can also be performed automatically during a homing sequence.

### Multi-axis maps require the source axes to be standing

For 2D/3D maps the table is built/validated with the additional source axes (selected by [MapEncoder](MapEncoder.md)) **motor-on and not moving**; the first dimension must reference this axis's own main encoder. Mapping cannot be enabled in motion (`ok_in_motion = false`).

## Examples

```text
AMapType=1           ; enable 1D error mapping
AMapType=0           ; disable error mapping (ramps out per MapErrOnStep)
AMapType             ; read the active mapping mode
```

## See also

- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values applied by mapping
- [MapEncoder](MapEncoder.md) — encoder source used for each map segment
- [MapStartIndex](MapStartIndex.md) — first active map segment
- [PosBeforeMap](PosBeforeMap.md) — feedback position before correction is applied
- [Pos](../10-motion/01-kinematics-status/Pos.md) — corrected feedback position that mapping adjusts
