---
keyword: LoggerStatus
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 534
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 6
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
# LoggerStatus

**Definition:**

LoggerStatus is a read-only array parameter that reports the current state of the data logger, including whether it is active, the number of samples collected, and buffer fill level. It is a non-axis status variable and is not saved to flash.

**See also:**

[LoggerOn](LoggerOn.md), [LoggerFullMod](LoggerFullMod.md), [LoggerAbout](LoggerAbout.md)
