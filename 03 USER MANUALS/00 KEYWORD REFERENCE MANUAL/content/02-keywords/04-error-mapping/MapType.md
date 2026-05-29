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

`MapType` is read once per control cycle in the feedback pipeline to choose the correction branch. The supported values are:

| `MapType` | Mode | Lookup dimensions | Interpolation |
|:---------:|------|-------------------|---------------|
| 0 | Off | none — `Pos = PosBeforeMap` | none |
| 1 | 1D | first encoder only | linear (2-point) |
| 2 | 2D | first encoder = row, second = column | bilinear (4-point) |
| 3 | 3D | first/second/third encoders | trilinear (8-point) |

Each cycle the controller records `PosBeforeMap` (the decoded main-encoder position), then — if the motor is **not** in simulation — runs the selected branch to compute a correction and forms `Pos = PosBeforeMap + (ramped correction)`. `DeltaPos` is recomputed afterwards so the velocity estimate also reflects the corrected position. In **simulation** mode mapping is skipped entirely (`Pos = PosBeforeMap`) to avoid the closed loop that would otherwise form in motor-off, where the corrected position feeds back into the commanded position.

### Internal vs. requested type, and the engage/disengage ramp

Writing `MapType` does **not** switch the correction on or off abruptly. The controller keeps a separate internal copy of the active type and a 0..1 ramp counter:

- **Engaging** (write `MapType` 1/2/3 from 0): the internal type is set immediately and the ramp counter starts at 0, climbing toward a full scale of `16384` (one second at the 16 kHz base sampling rate) at a rate set by [MapErrOnStep](MapErrOnStep.md). Until it reaches full scale the correction is scaled by `counter / 16384`, so the correction (and the [MapErrOffset](MapErrOffset.md) component) fades in smoothly with no position step.
- **Disengaging** (write `MapType` 0): the user value goes to 0 but the internal type stays active and the correction ramps **down**; only when the counter reaches 0 does the internal type revert to off. With [MapErrOnStep](MapErrOnStep.md) = 0 the engage / disengage transition is immediate (one cycle).

This ramp logic is shared by all of `MapType`, [MapErrOnStep](MapErrOnStep.md), [MapErrOffset](MapErrOffset.md), and [MapErrOffRamp](MapErrOffRamp.md). Engaging can also be performed automatically during a homing sequence.

### Multi-axis maps require the source axes to be standing

For 2D/3D maps the table is built/validated with the additional source axes (selected by [MapEncoder](MapEncoder.md)) **motor-on and not moving**; the first dimension must reference this axis's own main encoder. Mapping cannot be enabled in motion (`ok_in_motion = false`).

## Examples

```text
AMapType=1           ; enable 1D error mapping
AMapType=0           ; disable error mapping (ramps out per MapErrOnStep)
AMapType             ; read the active mapping mode
```

### Edge cases

- **Motion in progress** — `ok_in_motion = false`. Writes during motion are rejected; the change must be made while the axis is standing.
- **Phasing complete** — mapping operates on the post-commutation feedback path; in practice the axis must already be commutated for mapping to make sense.
- **Simulation motor** — mapping is **skipped entirely** when [MotorType](../02-motor-and-amplifier/MotorType.md) = simulation, because feeding the corrected position back into the simulated encoder would close a loop with the position reference. `Pos = PosBeforeMap` in this case regardless of `MapType`.
- **Wrong dimension** — values outside `0`–`3` are rejected at the parameter table.
- **Multi-dim (`MapType` = 2 or 3)** — additional encoder axes referenced by [MapEncoder](MapEncoder.md)`[2]`/`[3]` must be motor-on, not moving, and pointing at **main** encoders; otherwise the table build raises a "must be main encoders" / "must be first encoder" event.
- **First-encoder constraint** — [MapEncoder](MapEncoder.md)`[1]` must point at this axis's own main encoder; otherwise the table build is rejected.
- **`MapErrOnStep = 0`** — engage / disengage is immediate; useful for tests but produces a position step.
- **Motor off** — the user-visible `MapType` can be written (`ok_motor_on = true`); the ramp counter continues to update so re-enabling the motor finds the engagement smooth.

## See also

- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values applied by mapping
- [MapEncoder](MapEncoder.md) — encoder source used for each map segment
- [MapStartIndex](MapStartIndex.md) — first active map segment
- [PosBeforeMap](PosBeforeMap.md) — feedback position before correction is applied
- [Pos](../10-motion/01-kinematics-status/Pos.md) — corrected feedback position that mapping adjusts
