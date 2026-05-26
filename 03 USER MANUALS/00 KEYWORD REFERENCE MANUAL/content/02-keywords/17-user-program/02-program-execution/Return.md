---
keyword: Return
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 432
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 7
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 10
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Return

Return will cause a jump back to the user program that will continue execution on the next line
after a function call.
**Note:**
Use ProgHalt at the end of the program if your program is not an endless loop. Otherwise
execution will continue into the first function and the "return" keyword will cause an error.
