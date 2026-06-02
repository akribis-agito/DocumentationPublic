---
keyword: IndirectIndex
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 434
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
  - 1000
  default: 1
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - 1
    - 10000
---
# IndirectIndex

**Definition:**

IndirectIndex holds the array index used by the indirect access mechanism. It is written before IndirectDo is executed to select which element of the array specified by IndirectArray will be accessed. Indexes are 1-based, with a minimum of 1 and a default of 1; the maximum is the number of user elements in the selected array (the GenData array size, which depends on the controller model). If the index is below 1 or above the array size when IndirectDo runs, the write is rejected with error 116. It is a non-axis parameter and is not saved to flash.

**See also:**

[IndirectArray](IndirectArray.md), [IndirectValue](IndirectValue.md), [IndirectDo](IndirectDo.md)
