---
keyword: LoggerOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 530
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# LoggerOn

**Definition:**

LoggerOn enables or disables the continuous data logger. When set to a non-zero value, the logger begins sampling the parameters configured in LoggerParams at the rate defined by LoggerGap. It is a non-axis parameter and is not saved to flash.

**See also:**

[LoggerParams](LoggerParams.md), [LoggerGap](LoggerGap.md), [LoggerStatus](LoggerStatus.md), [LoggerUpload](LoggerUpload.md)
