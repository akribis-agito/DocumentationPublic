---
keyword: PDFact
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 110
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -16777215
  - 16777215
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDFact

**Definition:**

PDFact is the numerator of the scaling factor applied onto the number of pulses detected, before the sign correction and accumulation on internal counter (PDPos).
