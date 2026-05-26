---
keyword: ProgPriority
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 296
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 10
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgPriority

**Definition:**

ProgPriority sets the scheduling priority of a user program task. It is an array parameter indexed by task number, saved to flash, and is a non-axis parameter.

**See also:**

[ProgReset](ProgReset.md), [ProgStatAll](ProgStatAll.md)
