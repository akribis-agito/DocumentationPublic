---
keyword: ProgArgThis
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 433
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 21
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
# ProgArgThis

**Definition:**

ProgArgThis is an array parameter that reads back the argument values received by the currently executing user program task. It provides the calling task with access to its own argument list. It is a non-axis parameter and is not saved to flash.

**See also:**

[ProgArg](ProgArg.md), [ProgPushArg](ProgPushArg.md)
