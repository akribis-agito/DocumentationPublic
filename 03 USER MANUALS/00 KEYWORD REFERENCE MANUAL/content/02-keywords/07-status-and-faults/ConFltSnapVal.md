---
keyword: ConFltSnapVal
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 529
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 15
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - -2147483648
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ConFltSnapVal

**Definition:**

ConFltSnapVal is a read-only array that holds the parameter values captured at the moment the last controller fault occurred, as configured by ConFltSnapSrc. Reading this array after a fault provides a snapshot of the system state for fault diagnosis. It is an axis-related array that is not saved to flash.

**See also:**

[ConFltSnapSrc](ConFltSnapSrc.md), [ConFlt](ConFlt.md)
