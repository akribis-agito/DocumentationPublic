---
keyword: ProgHeap
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 1021
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 51
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
# ProgHeap

**Definition:**

ProgHeap is the dynamic memory heap used by the user program runtime for variable storage. It is an array parameter that can be read and written at any time. It is a non-axis parameter and is not saved to flash.

**See also:**

[ProgStatAll](ProgStatAll.md), [ProgReset](ProgReset.md)
