---
keyword: ProgCallDepth
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 277
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgCallDepth

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

Inquires the empty spaces at the program calls stack of the specified thread.

Please refer to the User Program Language Manual for more information.
