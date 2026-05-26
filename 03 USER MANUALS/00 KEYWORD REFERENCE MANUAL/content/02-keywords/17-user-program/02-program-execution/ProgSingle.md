---
keyword: ProgSingle
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 191
attributes:
  access: rw
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
  - 1
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# ProgSingle

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

ProgSingle is a user program related command that is normally issued by the PCsuite.
AProgSingle[1],0
Executes the next line of thread 1 and halts. This is like a debugger "step into".
AProgSingle[1],1
Is equivalent to debugger "step over" for internal wait loops.
