---
keyword: MapPosGap
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 325
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
  - 8000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
summary: Encoder-count spacing between adjacent error-mapping points.
---
# MapPosGap

Encoder-count spacing between adjacent error-mapping points.

## Overview

`MapPosGap` is a per-dimension array (`[1]`/`[2]`/`[3]`) that sets the position spacing, in encoder counts, between consecutive correction points along each error-mapping dimension. A larger gap spreads the same number of points ([MapLength](MapLength.md)) across a wider range, giving coarser resolution; a smaller gap gives finer correction over a shorter range. Together with [MapStartPos](MapStartPos.md) (start) and [MapLength](MapLength.md) (count) it defines the lookup grid of [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md).

It is an axis-scoped array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

## How it works

The gap is the denominator that converts an encoder reading to a table index:

$$
\text{index}_f = \frac{\text{PosBeforeCorrection} - \text{MapStartPos}[d]}{\text{MapPosGap}[d]}
$$

To keep this cheap in the real-time control interrupt, the controller precomputes the reciprocal $1 / \text{MapPosGap}[d]$ (as a single-precision float) whenever `MapPosGap` is written, and multiplies by it each cycle. Two consequences follow:

- **Must not be zero.** A zero gap would divide by zero, so the firmware silently substitutes the default `1000` if you set it to 0.
- **Upper limit 8,000,000.** The reciprocal is held in a 32-bit float (24-bit mantissa); the range is capped so the gap is represented exactly and the index stays accurate.

The integer part of `index_f` selects the lower grid point; the fractional part is the interpolation weight toward the next point.

## Examples

```text
AMapPosGap[1]=1000   ; correction points 1000 encoder counts apart
AMapPosGap[1]        ; read the spacing for the first dimension
```

## See also

- [MapLength](MapLength.md) — number of correction points per dimension
- [MapStartPos](MapStartPos.md) — start position of each dimension
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — correction values at each point
- [Pos](../10-motion/01-kinematics-status/Pos.md) / [PosBeforeMap](PosBeforeMap.md) — corrected and pre-correction feedback
