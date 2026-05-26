---
keyword: IdRef
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 29
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# IdRef

**Definition:**

IdRef is the reference current of direct axis, in milliamperes used in dq0-domain current control. Currently, IdRef is always 0. Please contact Agito if application involving IdRef (e.g. flux weakening) is needed.
