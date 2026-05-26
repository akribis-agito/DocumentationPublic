---
keyword: ProgArg
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 439
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 20
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgArg

**Definition:**

ProgArg is an array parameter that holds the argument values passed to a user program task. Each element corresponds to one argument slot for the indexed task. It is a non-axis parameter and is not saved to flash.

**See also:**

[ProgArgThis](ProgArgThis.md), [ProgPushArg](ProgPushArg.md)
