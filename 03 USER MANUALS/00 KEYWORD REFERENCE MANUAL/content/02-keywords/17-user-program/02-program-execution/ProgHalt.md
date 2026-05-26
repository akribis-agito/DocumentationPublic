---
keyword: ProgHalt
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 197
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
  implemented: partial
overrides: {}
---
# ProgHalt

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

"ProgHalt[Thread no.]" will halt the thread number. Halting is not the same as resetting the
program. If ProgRun is entered again for the same thread it will continue from the point it was
halted in.
