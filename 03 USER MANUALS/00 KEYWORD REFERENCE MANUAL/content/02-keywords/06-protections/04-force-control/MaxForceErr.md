---
keyword: MaxForceErr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 585
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
  - 327680
  default: 2000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxForceErr

**Definition:**

MaxForceErr sets the maximum allowable force error in closed-loop force control mode. If the difference between the commanded force and the measured force exceeds this threshold, the controller generates a fault. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

**See also:**

[MaxForceErrOL](MaxForceErrOL.md)
