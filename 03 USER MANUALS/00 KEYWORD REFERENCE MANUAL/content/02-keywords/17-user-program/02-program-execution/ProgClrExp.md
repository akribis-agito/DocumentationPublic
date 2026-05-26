---
keyword: ProgClrExp
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 203
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 10
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# ProgClrExp

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

ProgClrExp is a user program low level language keyword. It is used to clear the numeric stack of
the current thread. It is recommended to begin new programs by using ProgClrExp.
Please refer to the User Program Language Manual for more information.
