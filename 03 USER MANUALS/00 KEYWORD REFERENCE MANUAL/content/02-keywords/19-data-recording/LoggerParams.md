---
keyword: LoggerParams
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 532
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 41
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
# LoggerParams

**Definition:**

LoggerParams is an array parameter that specifies which controller parameters the continuous data logger records. Each element identifies one parameter to be sampled during a logging session. It is a non-axis parameter saved to flash.

**See also:**

[LoggerOn](LoggerOn.md), [LoggerGap](LoggerGap.md), [LoggerAbout](LoggerAbout.md), [LoggerUpload](LoggerUpload.md)
