---
keyword: ForceRefFOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 579
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
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
# ForceRefFOn

**Definition:**

ForceRefFOn is the switch for force command first-order low-pass filter. If ForceRefFOn = 1, filter is enabled. If ForceRefFOn = 0, filter is disabled (bypassed).

The filter is disabled by default.
