---
keyword: RefOffsetStep
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 166
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RefOffsetStep

**Definition:**

RefOffsetStep sets the magnitude of each incremental position offset applied per servo sample during a reference offset correction. Together with RefOffsetSamp it controls the rate at which a position correction is introduced into the reference trajectory. It is an axis-related parameter in user units, not saved to flash, and can be changed at any time.

**See also:**

[RefOffsetSamp](RefOffsetSamp.md)
