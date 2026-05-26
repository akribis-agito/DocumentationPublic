---
keyword: ProgStatAll
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 298
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 2
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgStatAll

**Definition:**

ProgStatAll is a read-only parameter that returns a combined status word reflecting the execution state of all user program tasks. It is a non-axis status variable and is not saved to flash.

**See also:**

[ProgPointer](ProgPointer.md), [ProgPriority](ProgPriority.md), [ProgReset](ProgReset.md)
