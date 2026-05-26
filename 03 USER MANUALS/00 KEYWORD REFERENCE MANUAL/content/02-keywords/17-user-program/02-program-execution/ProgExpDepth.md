---
keyword: ProgExpDepth
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 205
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
# ProgExpDepth

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

ProgExpDepth is a user program low level language keyword. ProgExpDepth returns the highest
full location of the relevant numeric stack. If the stack is empty it will return -1. If there is one
value in the stack the highest full location is 0, etc...
