---
keyword: StopOnHome
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 169
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
# StopOnHome

**Definition:**

StopOnHome configures which digital home input, when asserted, will automatically stop axis motion. Setting this to a non-zero value enables the home-switch stop function so that the axis halts when the home signal is detected during a move. It is an axis-related parameter, not saved to flash, and can be changed at any time.

**See also:**

[StopOnIndex](StopOnIndex.md), [HomeStat](HomeStat.md)
