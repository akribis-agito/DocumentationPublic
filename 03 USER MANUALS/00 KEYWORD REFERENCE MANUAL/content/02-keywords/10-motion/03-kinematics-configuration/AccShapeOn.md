---
keyword: AccShapeOn
summary: Enables acceleration shaping to reduce vibration via a shaped acceleration curve.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 162
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AccShapeOn

Enables acceleration shaping to reduce vibration via a shaped acceleration curve.

## Overview

`AccShapeOn` enables the acceleration-shaping feature, which modifies the acceleration profile to reduce mechanical vibration by applying a shaped (filtered) acceleration curve. When set to `1`, the [AccShapeDist](AccShapeDist.md) and [AccShapeFact](AccShapeFact.md) arrays define the shaping profile applied on top of the base [Accel](Accel.md) ramp. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## How it works

Acceleration shaping scales the acceleration (and deceleration) used by the profiler as a function of the **remaining distance to the target**, using a 10-entry lookup table. While `AccShapeOn != 0`, each control cycle the profiler computes the distance to target `d = |AbsTrgt − PosRef|` and finds the first table segment whose distance threshold exceeds `d`:

```text
if d < AccShapeDist[1]      factor = AccShapeFact[1]  / 65536
else if d < AccShapeDist[2] factor = AccShapeFact[2]  / 65536
   ... up to ...
else if d < AccShapeDist[10] factor = AccShapeFact[10] / 65536
else                         factor = 1.0
```

The chosen `factor` then multiplies both the acceleration and the deceleration limits for that cycle:

```text
AccelFinal = Accel × AccelFact × factor
DecelFinal = Decel × AccelFact × factor
```

So the segments are keyed by *distance from the target* (the table is consulted nearest-to-target first), letting you taper the acceleration as the axis closes in, which softens the approach and suppresses residual vibration. Beyond the largest distance threshold the factor is `1.0`, i.e. no shaping — the full acceleration is used during the bulk of the move.

The [AccShapeFact](AccShapeFact.md) entries are **fixed-point fractions scaled by 65536**, so `65536` means ×1.0, `32768` means ×0.5, and `0` means no acceleration in that band. Whenever any element of [AccShapeDist](AccShapeDist.md) or [AccShapeFact](AccShapeFact.md) is written, the controller re-sorts the (distance, factor) pairs into ascending distance order so the lookup above always scans from the smallest distance upward — you do not have to enter the table pre-sorted.

![Acceleration-shaping lookup by distance to target](accshape-lookup.svg)

## Examples

```text
AAccShapeOn=1        ; enable acceleration shaping
AAccShapeOn=0        ; disable acceleration shaping
AAccShapeOn         ; query state
```

## See also

- [AccShapeDist](AccShapeDist.md) — per-segment shaping distances
- [AccShapeFact](AccShapeFact.md) — per-segment shaping factors
- [Accel](Accel.md) — base acceleration that shaping modifies
