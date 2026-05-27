---
keyword: AccShapeDist
summary: Array of per-segment distances defining the acceleration-shaping profile.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 163
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - 0
    - 2251799813685247
---
# AccShapeDist

Array of per-segment distances defining the acceleration-shaping profile.

## Overview

`AccShapeDist` is an array (10 usable entries, indices 1–10) that defines the **distance-to-target threshold** of each segment in the acceleration-shaping profile. Together with [AccShapeFact](AccShapeFact.md) it specifies how the acceleration magnitude is distributed over the move to reduce mechanical vibration. The shaping is only applied when [AccShapeOn](AccShapeOn.md) is enabled. It is an axis-related array saved to flash and can be changed at any time.

## How it works

Each control cycle the profiler compares the remaining distance to target, `|AbsTrgt − PosRef|`, against these thresholds and uses the matching [AccShapeFact](AccShapeFact.md) entry as the acceleration scale (`AG300_CTL01Profiler.c:1028`–`1054`). The thresholds are interpreted **nearest-to-target first**: the first entry whose distance exceeds the remaining distance selects the band. If the remaining distance is larger than every threshold, the factor is `1.0` (no shaping).

The values are in the same user units as position. You do **not** need to enter them in order — when any `AccShapeDist`/`AccShapeFact` element is written the firmware re-sorts the (distance, factor) pairs into ascending distance order before they are used (`SpAccShape`, `SpecialFuncs.c:5868`). The array is declared with size 11 so that command indices can start at `1`; only indices 1–10 carry data (`ACCSHAPE_SIZE = 11`, `AG300_CTL01ParamsCommon.h:653`). See [AccShapeOn](AccShapeOn.md) for the full lookup mechanism.

## Examples

```text
AAccShapeDist[1]=5000    ; nearest band: remaining distance < 5000 user units
AAccShapeDist[2]=8000    ; next band: 5000 .. 8000 user units
AAccShapeDist[1]        ; query first segment distance
```

## Changes between versions

In **v5 (central-i)** the distance thresholds are 64-bit (matching the 64-bit position pipeline), giving the larger range shown in the frontmatter; the shaping mechanism is otherwise unchanged. **v5 is central-i only**, so on standalone the thresholds remain the v4 32-bit values.

## See also

- [AccShapeOn](AccShapeOn.md) — enables acceleration shaping
- [AccShapeFact](AccShapeFact.md) — per-segment acceleration scaling factors
