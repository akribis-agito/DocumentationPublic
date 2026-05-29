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

Each control cycle the profiler compares the remaining distance to target, `|AbsTrgt − PosRef|`, against these thresholds and uses the matching [AccShapeFact](AccShapeFact.md) entry as the acceleration scale. The thresholds are interpreted **nearest-to-target first**: the first entry whose distance exceeds the remaining distance selects the band. If the remaining distance is larger than every threshold, the factor is `1.0` (no shaping).

The values are in the same user units as position. You do **not** need to enter them in order — when any `AccShapeDist`/`AccShapeFact` element is written the controller re-sorts the (distance, factor) pairs into ascending distance order before they are used. The array is declared with size 11 so that command indices can start at `1`; only indices 1–10 carry data. See [AccShapeOn](AccShapeOn.md) for the full lookup mechanism.

## Examples

```text
AAccShapeDist[1]=5000    ; nearest band: remaining distance < 5000 user units
AAccShapeDist[2]=8000    ; next band: 5000 .. 8000 user units
AAccShapeDist[1]        ; query first segment distance
```

### Edge cases

- **Motor off:** values are held; no profiler runs.
- **Out-of-range write:** the parameter system clamps to `0`–`2³¹−1` (v4) or `0`–`2⁵¹−1` (v5); negative values are rejected.
- **Index `[0]`:** does not exist in user-visible space; the keyword is 1-indexed (entries `[1]` … `[10]`). Reading `[0]` returns an error.
- **Simulation mode (`MotorType` = 5):** unchanged.
- **ModRev wrap:** the distance `|AbsTrgt − PosRef|` is in main-encoder units after wrap, so shaping bands behave consistently.
- **Active fault:** the axis is disabled; the table is preserved across the fault.
- **Other motion modes:** only the PTP-family profiler consults the table; ignored elsewhere.
- **Live change in motion:** allowed; the controller re-sorts the (distance, factor) pairs after each write, so the lookup uses the new table on the next cycle.
- **Duplicate or zero distances:** after re-sort, multiple entries with the same threshold collapse into the first one encountered; zero-distance entries are valid (act as the very-near band).

## Changes between versions

In **v5 (central-i)** the distance thresholds are 64-bit (matching the 64-bit position pipeline), giving the larger range shown in the frontmatter; the shaping mechanism is otherwise unchanged. **v5 is central-i only**, so on standalone the thresholds remain the v4 32-bit values.

## See also

- [AccShapeOn](AccShapeOn.md) — enables acceleration shaping
- [AccShapeFact](AccShapeFact.md) — per-segment acceleration scaling factors
