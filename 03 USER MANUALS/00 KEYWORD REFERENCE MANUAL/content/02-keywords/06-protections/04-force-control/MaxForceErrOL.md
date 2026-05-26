---
keyword: MaxForceErrOL
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 591
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
  default: 50000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxForceErrOL

**Definition:**

MaxForceErrOL sets the maximum allowable force error in open-loop force control mode (OL = open loop). If the force error exceeds this limit in open-loop operation, the controller generates a fault. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

**See also:**

[MaxForceErr](MaxForceErr.md)
