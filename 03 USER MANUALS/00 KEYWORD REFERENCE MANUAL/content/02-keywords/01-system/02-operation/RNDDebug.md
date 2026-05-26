---
keyword: RNDDebug
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 1022
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 1
  - 30
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# RNDDebug

**Definition:**

RNDDebug is a partially-implemented diagnostic function reserved for internal R&D and debugging purposes. Its behaviour depends on the firmware build and is not intended for use in production applications.

%%
Needs verification
This keyword is marked PARTIAL in the firmware table; exact semantics may vary by firmware version.
%%
