---
keyword: IndirectArray
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 436
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
  - 1
  - 1
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# IndirectArray

**Definition:**

IndirectArray selects the target array to be accessed indirectly. The value is an array selector, not a CAN code; the only currently supported selection is 1 (GenData), and the valid range is 1..1 with a default of 1. Together with IndirectIndex and IndirectValue, it forms the three-register indirect access mechanism that allows dynamic array addressing. It is a non-axis parameter and is not saved to flash.

**See also:**

[IndirectIndex](IndirectIndex.md), [IndirectValue](IndirectValue.md), [IndirectDo](IndirectDo.md)
