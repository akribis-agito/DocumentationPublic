---
keyword: Reset
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 234
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Reset

**Definition:**

Reset command will perform software power cycle operation on the controller. Flash parameters will be loaded upon power up, overriding all unsaved changes on volatile memory.
