---
keyword: IndirectValue
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 435
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# IndirectValue

**Definition:**

IndirectValue holds the source value for the indirect access operation. Set IndirectValue to the value to be stored before executing IndirectDo, which writes it into the selected array element. It accepts the full 32-bit signed range, -2147483648 to 2147483647, and defaults to 0. It is a non-axis parameter and is not saved to flash.

**See also:**

[IndirectIndex](IndirectIndex.md), [IndirectArray](IndirectArray.md), [IndirectDo](IndirectDo.md)
