---
keyword: HallsAngle
summary: Array mapping each Hall-sensor state to the electrical angle used for commutation.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 384
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 7
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 360
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# HallsAngle

Array mapping each Hall-sensor state to the electrical angle used for commutation.

## Overview

`HallsAngle` is an array that stores the commutation angle associated with each Hall-sensor state. Each valid Hall state combination (the six legal states reported by [HallsValue](HallsValue.md)) is mapped to the corresponding electrical angle used for commutation. This table lets the controller derive the motor electrical angle directly from the Hall sensors. The raw angle can be smoothed with [HallOnlyFilt](HallOnlyFilt.md) when running in Hall-only commutation mode (selected via [ComtMode](ComtMode.md)), and the resulting angle is reported by [ComtAng](ComtAng.md). Being an array, axis-scope, and flash-saved, it cannot be changed while the motor is on or in motion (per-element range 0–360).

## How it works

The array is 1-indexed and the index is the [HallsValue](HallsValue.md) reading: elements `[1]` … `[6]` hold the electrical angle (degrees) for Hall states 1 … 6 (Hall values 0 and 7 are illegal and have no entry). During Hall-based commutation the controller reads the current Hall state, looks up its angle here, and uses it as the electrical angle.

The default of every element is `-1`, meaning "not configured". When the table is left at the default, the controller fills it with a standard map for a nominally wired motor. The interpretation of the stored angles is selected on central-i v5 by [HallsAngleSw](HallsAngleSw.md):

**Middle-angle map** (`HallsAngleSw = 0`, the default and the only behavior on v4/standalone) — each entry is the electrical angle at the *middle* of the state:

| Hall value (CBA) | Default angle |
|---|---|
| 5 (101) | 60° |
| 1 (001) | 120° |
| 3 (011) | 180° |
| 2 (010) | 240° |
| 6 (110) | 300° |
| 4 (100) | 360° |

**Switch-angle map** (`HallsAngleSw = 1`, central-i v5 only) — each entry is the electrical angle at the *transition* between adjacent states. Default transition angles: 30°, 90°, 150°, 210°, 270°, 330°.

## Examples

```text
AHallsAngle[1]      ; query the angle mapped to Hall state 1
AHallsAngle[1]=120   ; set the electrical angle (deg) for Hall state 1
```

## See also

- [HallsValue](HallsValue.md) — current raw Hall sensor state (the index source)
- [HallsAngleSw](HallsAngleSw.md) — selects how these entries are interpreted (state mid-point vs. transition/switch angles)
- [HallOnlyFilt](HallOnlyFilt.md) — filter for the Hall-based commutation angle
- [ComtMode](ComtMode.md) — selects the commutation method
