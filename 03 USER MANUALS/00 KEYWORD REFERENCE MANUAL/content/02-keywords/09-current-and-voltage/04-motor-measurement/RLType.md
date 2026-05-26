---
keyword: RLType
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 375
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
  - 0
  - 1
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# RLType

**Definition:**

RLType defines the type of measurement made by PCSuite’s resistance and inductance measurement tool.

| RLType | Measurement type  |
|--------|-------------------|
| 0      | Phase data        |
| 1      | Line-to-line data |
