---
keyword: IndirectIndex
summary: Holds the array index used by the indirect access mechanism.
availability:
- controller
- ci-master
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
  - 5000
  default: 1
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - 1
    - 1000
  agc300-et:
    range:
    - 1
    - 1000
  agd200-et-2d01:
    range:
    - 1
    - 1000
  agd200-et-2d02:
    range:
    - 1
    - 1000
  agd200-et-2d05:
    range:
    - 1
    - 1000
  agd200-et-2d05-71:
    range:
    - 1
    - 1000
  agd155-af-2a06:
    range:
    - 1
    - 1000
  agd155-af-2a10:
    range:
    - 1
    - 1000
  agd155-ec:
    range:
    - 1
    - 1000
  agd155-ec-var34:
    range:
    - 1
    - 1000
  agd155-ec-var34-3:
    range:
    - 1
    - 1000
  agd156-ec:
    range:
    - 1
    - 1000
  agd101-ec-34a:
    range:
    - 1
    - 1000
  agd101-ec-17a:
    range:
    - 1
    - 1000
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# IndirectIndex

**Definition:**

IndirectIndex holds the array index used by the indirect access mechanism. It is written before IndirectDo is executed to select which element of the array specified by IndirectArray will be accessed. Indexes are 1-based, with a minimum of 1 and a default of 1; the maximum is the number of user elements in the selected array (the GenData array size, which depends on the controller model). If the index is below 1 or above the array size when IndirectDo runs, the write is rejected with error 116. It is a non-axis parameter and is not saved to flash.

**See also:**

[IndirectArray](IndirectArray.md), [IndirectValue](IndirectValue.md), [IndirectDo](IndirectDo.md)
