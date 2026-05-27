---
keyword: ScheduleTemp
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 273
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -20
  - 120
  default: 25
  scaling: 1.0
  implemented: final
overrides: {}
---
# ScheduleTemp

Motor-temperature thresholds that divide the temperature range into bands for temperature-based gain scheduling.

## Overview

`ScheduleTemp` holds the motor-temperature band edges used when [ScheduleMode](ScheduleMode.md) is `8` (by temperature range). The values are in degrees Celsius and must increase monotonically with array index.

## How it works

The controller compares the measured motor temperature against the thresholds and picks a gain set:

- Set 1 if temperature ≤ `ScheduleTemp[1]`
- Set 2 if `ScheduleTemp[1]` < temperature ≤ `ScheduleTemp[2]`
- Set 3 if `ScheduleTemp[2]` < temperature ≤ `ScheduleTemp[3]`
- Set 4 if `ScheduleTemp[3]` < temperature ≤ `ScheduleTemp[4]`
- Set 5 if temperature > `ScheduleTemp[4]`

(Element `ScheduleTemp[5]` is part of the array but is not used as an upper edge — anything above the fourth threshold maps to set 5.)

## Examples

```text
AScheduleTemp[1]=30; AScheduleTemp[2]=45; AScheduleTemp[3]=60; AScheduleTemp[4]=80
AScheduleMode[1]=8            ; select temperature-band scheduling
```

## See also

- [ScheduleMode](ScheduleMode.md) — mode 8 uses these thresholds
- [ScheduleSet](ScheduleSet.md) — band currently selected
- [SchedulePos](SchedulePos.md) / [ScheduleVel](ScheduleVel.md) — analogous thresholds for the other range modes
