---
keyword: PushConstant
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 201
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# PushConstant

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

PushConstant is a user program low level language keyword. It is used to push the value of a
constant into the numeric stack of the current user program thread.
Normally, the user does not need to be concerned with generating the code since the user
program IDE environment on the PC Suite will automatically generate it during compilation.
