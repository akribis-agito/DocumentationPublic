---
keyword: SchedulePos
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 264
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 2147483647
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
    default: 2251799813685247
---
# SchedulePos

Position thresholds that divide the travel into bands for position-based gain scheduling.

## Overview

`SchedulePos` holds the position band edges used when [ScheduleMode](ScheduleMode.md) is `5` (stepped, by position range) or `10` (interpolated, by position range). The values are in user position units and must increase monotonically with array index.

## How it works

The controller compares the axis position against the thresholds and picks a gain set:

- Set 1 if position ≤ `SchedulePos[1]`
- Set 2 if `SchedulePos[1]` < position ≤ `SchedulePos[2]`
- Set 3 if `SchedulePos[2]` < position ≤ `SchedulePos[3]`
- Set 4 if `SchedulePos[3]` < position ≤ `SchedulePos[4]`
- Set 5 if position > `SchedulePos[4]`

(Element `SchedulePos[5]` is part of the array but is not used as an upper edge — anything above the fourth threshold maps to set 5.)

In the stepped mode (`ScheduleMode = 5`), the gains step to the selected set. In the interpolated mode (`ScheduleMode = 10`), the gains are blended linearly across each band rather than stepping; this requires the first four thresholds to be strictly increasing, otherwise scheduling is disabled, set 1 is used, and [ScheduleSet](ScheduleSet.md) reports `-1`.

When the axis is under gantry-paired scheduling, the gantry feedback position is compared against these thresholds instead of the axis position (see [ScheduleGntry](ScheduleGntry.md)).

## Examples

```text
ASchedulePos[1]=100000; ASchedulePos[2]=200000; ASchedulePos[3]=300000; ASchedulePos[4]=400000
AScheduleMode[1]=5            ; select position-band scheduling
```

## See also

- [ScheduleMode](ScheduleMode.md) — modes 5 and 10 use these thresholds
- [ScheduleSet](ScheduleSet.md) — band currently selected
- [ScheduleVel](ScheduleVel.md) / [ScheduleTemp](ScheduleTemp.md) — analogous thresholds for the other range modes (the band-mapping diagram is on [ScheduleVel](ScheduleVel.md))
