---
keyword: WaitTime
summary: Suspends the current task for a specified time in milliseconds.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 193
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
  - 0
  - 10000000
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# WaitTime

Suspends the current task for a specified time in milliseconds.

## Overview

`WaitTime` is a user-program instruction that suspends execution of the current task for a specified time duration in milliseconds. It is the time-based counterpart of [WaitStatus](WaitStatus.md), which instead waits for a status condition. It can be used during motion and with the motor on. It is a non-axis command and is not saved to flash.

## Examples

```text
AWaitTime,1000      ; pause the current task for 1000 ms (1 second)
```

## See also

- [WaitStatus](WaitStatus.md) — hold a task until a status reaches a value
