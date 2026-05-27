---
keyword: PosBeforeMap
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 160
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: false
  units: user
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
summary: Read-only feedback position before error-mapping correction.
---
# PosBeforeMap

Read-only feedback position before error-mapping correction.

## Overview

`PosBeforeMap` reports the axis position from the main encoder, in user units, **before** any error-mapping correction has been applied. The corrected value is reported by [Pos](../10-motion/01-kinematics-status/Pos.md); the difference `Pos − PosBeforeMap` is the (ramped, interpolated) correction contributed by the [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) arrays when mapping is enabled with [MapType](MapType.md). Comparing the two is the standard way to verify how much correction the map is injecting.

It is a read-only, axis-scoped status variable that is not saved to flash.

## How it works

`PosBeforeMap` is captured **every** control cycle, at the start of the error-mapping stage, as a snapshot of the decoded main-encoder reading — *before* the correction branch runs. It is recorded unconditionally, so:

- With mapping **off** (`MapType = 0`), `Pos = PosBeforeMap` (no correction). The two reading equal.
- With mapping **on**, the firmware computes the interpolated correction from the [MapEncoder](MapEncoder.md)-selected source and forms `Pos = PosBeforeMap + correction` (correction scaled by the engage ramp; see [MapErrOnStep](MapErrOnStep.md)).
- In **simulation** mode the correction is skipped, so again `Pos = PosBeforeMap`.

Note that `PosBeforeMap` always tracks the **main** encoder of this axis, even if the map looks up a different encoder via [MapEncoder](MapEncoder.md) — it is the pre-correction baseline of the value that mapping reshapes into `Pos`.

## Examples

```text
APosBeforeMap        ; read the uncorrected feedback position
```

## Changes between versions

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Data type | 32-bit (`long`) | **64-bit (`long long`)** |
| Range | ±2,147,483,647 | ±2,251,799,813,685,247 |

In **v5** the feedback pipeline is 64-bit, so `PosBeforeMap` mirrors the wider [Pos](../10-motion/01-kinematics-status/Pos.md) range. v5 is **central-i only**; on standalone it remains the 32-bit v4 value.

## See also

- [Pos](../10-motion/01-kinematics-status/Pos.md) — feedback position after correction; difference equals the map correction
- [MapType](MapType.md) — enables the correction that creates the difference
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values applied to the feedback
- [MapErrOnStep](MapErrOnStep.md) — ramps the correction in/out, so the difference grows/shrinks gradually
