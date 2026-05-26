---
keyword: LoggerAbout
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 535
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 44
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
# LoggerAbout

**Definition:**

LoggerAbout is a read-only array parameter that reports metadata about the current logger session, including the list of logged parameters and session configuration information. It is a non-axis status variable and is not saved to flash.

**See also:**

[LoggerOn](LoggerOn.md), [LoggerParams](LoggerParams.md), [LoggerStatus](LoggerStatus.md)
