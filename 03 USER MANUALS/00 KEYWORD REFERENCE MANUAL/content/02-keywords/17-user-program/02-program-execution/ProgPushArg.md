---
keyword: ProgPushArg
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 431
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgPushArg

**Definition:**

ProgPushArg is a command that pushes a value onto the argument stack of a target user program task, preparing arguments before invoking or resuming the task. It is a non-axis command and is not saved to flash.

**See also:**

[ProgArg](ProgArg.md), [ProgArgThis](ProgArgThis.md)
