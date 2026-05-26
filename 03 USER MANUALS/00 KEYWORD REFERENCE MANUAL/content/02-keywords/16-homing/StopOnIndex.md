---
keyword: StopOnIndex
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 167
attributes:
  access: rw
  scope: axis
  flash: false
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
# StopOnIndex

**Definition:**

StopOnIndex configures the encoder index pulse to automatically stop axis motion when detected. When set to a non-zero value, the next encoder index pulse causes the axis to halt, which is useful for homing procedures that reference the encoder index position. It is an axis-related parameter, not saved to flash, and can be changed at any time.

**See also:**

[StopOnHome](StopOnHome.md), [HomeStat](HomeStat.md)
