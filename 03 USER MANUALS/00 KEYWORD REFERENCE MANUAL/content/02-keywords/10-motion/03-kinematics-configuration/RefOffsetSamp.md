---
keyword: RefOffsetSamp
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 165
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RefOffsetSamp

**Definition:**

RefOffsetSamp sets the number of servo samples over which the reference offset is applied when ramping in a position correction step. It works in conjunction with RefOffsetStep to spread a position offset correction gradually over time. It is an axis-related parameter, not saved to flash, and can be changed at any time.

**See also:**

[RefOffsetStep](RefOffsetStep.md)
