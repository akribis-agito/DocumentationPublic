---
keyword: ProgFuncCall
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 430
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 1
  - 254
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgFuncCall

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

When the line AProgFuncCall,1 is reached, the program execution jumps to the location of the
label keyword ProgFunc[1]. Return will cause a jump back to the user program that will continue
execution on the next line.
Use multiple ProgFunc[] labels for multiple functions.
**Note:**
Use ProgHalt at the end of the program if your program is not an endless loop. Otherwise
execution will continue into the first function and the "return" keyword will cause an error.
