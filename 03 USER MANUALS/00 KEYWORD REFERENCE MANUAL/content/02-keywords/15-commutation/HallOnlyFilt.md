---
keyword: HallOnlyFilt
availability:
  standalone:
  - v4
  central-i:
  - v4
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

**Definition:**

HallOnlyFilt sets the digital filter applied to the Hall-sensor-based commutation angle when operating in Hall-only commutation mode. A higher value applies more filtering to reduce noise on the Hall signal at the cost of phase lag. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[HallsValue](HallsValue.md), [HallsAngle](HallsAngle.md), [ComtMode](ComtMode.md)
