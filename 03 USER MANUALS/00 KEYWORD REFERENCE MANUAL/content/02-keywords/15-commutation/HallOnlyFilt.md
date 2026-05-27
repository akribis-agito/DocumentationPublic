---
keyword: HallOnlyFilt
summary: Digital filter applied to the Hall-sensor-based commutation angle in Hall-only commutation mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 477
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
  - 99
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HallOnlyFilt

Digital filter applied to the Hall-sensor-based commutation angle in Hall-only commutation mode.

## Overview

`HallOnlyFilt` sets the digital filter applied to the Hall-sensor-based commutation angle when the axis operates in Hall-only commutation mode. A higher value applies more filtering to reduce noise on the Hall signal, at the cost of additional phase lag. It is used to clean up the commutation angle derived from the raw Hall state ([HallsValue](HallsValue.md)) and its associated angle map ([HallsAngle](HallsAngle.md)) when no encoder-based commutation is available. The commutation method itself is selected through [ComtMode](ComtMode.md). Being axis-scope and flash-saved, it can be changed at any time, including while the motor is on or in motion (range 0–99, default 0).

## Examples

```text
AHallOnlyFilt=10     ; apply moderate filtering to the Hall-based angle
AHallOnlyFilt       ; query the current filter setting
```

## See also

- [HallsValue](HallsValue.md) — raw Hall sensor state being filtered
- [HallsAngle](HallsAngle.md) — electrical angle mapped to each Hall state
- [ComtMode](ComtMode.md) — selects the commutation method
