---
summary: Electrical angle at which commutation switches from Hall-based to encoder-based feedback during startup.
keyword: HallsAngleSw
availability:
  standalone: []
  central-i:
  - v5
can_code: 679
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HallsAngleSw

Selects how the [HallsAngle](HallsAngle.md) table entries are interpreted: as Hall-state mid-point angles or as Hall-state transition (switch) angles.

## Overview

`HallsAngleSw` is a mode selector (range 0–1, default 0) that determines how the angles stored in [HallsAngle](HallsAngle.md) are interpreted, and which default angle map the controller installs when `HallsAngle` is left unconfigured. It is an axis-scope, flash-saved parameter available on central-i v5 only; it cannot be changed while the motor is on or in motion.

| Value | Meaning |
|---|---|
| 0 (default) | **Middle-angle** style — each `HallsAngle` entry is the electrical angle at the *middle* of the corresponding Hall state. Default map: state 5 → 60°, 1 → 120°, 3 → 180°, 2 → 240°, 6 → 300°, 4 → 360°. |
| 1 | **Switch-angle** style — each entry is the electrical angle at the *transition* between adjacent Hall states. Default transition angles: 30°, 90°, 150°, 210°, 270°, 330°. |

## How it works

When the [HallsAngle](HallsAngle.md) table is at its default (every element `-1`, "not configured"), the controller installs one of the two default maps above according to `HallsAngleSw`. The selected style also defines how the stored angles are applied when deriving the commutation angle from the Hall sensors during Hall-based commutation methods (see [ComtMode](ComtMode.md)).

> [!note]
> Despite the legacy one-line summary in this page's metadata, `HallsAngleSw` is **not** a switch-over angle threshold between Hall- and encoder-based feedback. It is a 0/1 selector for the Hall-angle table interpretation, as described above.

## Examples

```text
AHallsAngleSw=0      ; interpret HallsAngle as state mid-point angles (default)
AHallsAngleSw=1      ; interpret HallsAngle as state transition (switch) angles
AHallsAngleSw       ; query the current interpretation mode
```

## See also

- [HallsAngle](HallsAngle.md) — electrical angle mapped to each Hall state (interpreted per this selector)
- [HallsValue](HallsValue.md) — current raw Hall sensor state
- [HallOnlyFilt](HallOnlyFilt.md) — filter for the Hall-based commutation angle
- [ComtMode](ComtMode.md) — selects the commutation method
