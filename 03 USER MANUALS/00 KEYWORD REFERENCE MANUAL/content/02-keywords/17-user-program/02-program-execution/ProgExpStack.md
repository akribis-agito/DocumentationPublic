---
keyword: ProgExpStack
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 204
attributes:
  access: rw
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
  - 51
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# ProgExpStack

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

ProgExpStack is a user program low level language keyword. It is used to read the top number of
the numeric stack without popping it. This keyword is most useful for debug.
