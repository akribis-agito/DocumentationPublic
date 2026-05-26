---
keyword: AuxPos
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 3
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: aux_user_units
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AuxPos

**Definition:**

AuxPos reports the auxiliary encoder feedback, in terms of auxiliary user unit (configurable by AuxUsrUnits).

AuxPos can be set to any desired value when the axis is disabled. Its value is reset to 0 upon power up.
