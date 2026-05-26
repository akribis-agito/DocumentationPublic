---
keyword: ProgRun
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 198
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
  - 254
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# ProgRun

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

"ProgRun[Thread no.], Task no." will run the required task as the required thread number. For
**example:**
AProgRun[3],5
Runs task 5 as thread 3.
To run the "main" program that starts at the beginning of the file use "-1" as the task number.
