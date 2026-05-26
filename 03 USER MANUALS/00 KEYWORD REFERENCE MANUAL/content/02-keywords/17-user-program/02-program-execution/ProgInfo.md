---
keyword: ProgInfo
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 297
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
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
# ProgInfo

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

Inquires the list of information strings that are included with the user program: CRC value, Date,
CUP File name and the text information (see the "#information" compiler directive)
