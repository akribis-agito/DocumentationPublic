---
keyword: LoggerUpload
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 536
attributes:
  access: ro
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
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# LoggerUpload

**Definition:**

LoggerUpload is a command that initiates the transfer of the logged data buffer from the controller to the host. It can be invoked while the logger is active or after it has stopped. It is a non-axis command and is not saved to flash.

**See also:**

[LoggerOn](LoggerOn.md), [LoggerStatus](LoggerStatus.md), [LoggerAbout](LoggerAbout.md)
