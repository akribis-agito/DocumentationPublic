---
keyword: LoggerOn
summary: Enables or disables the continuous data logger.
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

Enables or disables the continuous data logger.

## Overview

`LoggerOn` starts or stops the continuous data logger. When set to a non-zero value, the logger begins sampling the parameters configured in [LoggerParams](LoggerParams.md) at the rate defined by [LoggerGap](LoggerGap.md); setting it to `0` stops logging. It is a non-axis parameter and is not saved to flash, so the logger always starts disabled after power-up.

Unlike the recording scope (`Rec*` keywords), the continuous logger runs in the background and is intended for long-running capture. Use [LoggerStatus](LoggerStatus.md) to monitor its state and [LoggerUpload](LoggerUpload.md) to retrieve the captured data.

## Examples

```text
ALoggerOn=1          ; start the continuous logger
ALoggerOn=0          ; stop the continuous logger
ALoggerOn           ; query whether the logger is running
```

## See also

- [LoggerParams](LoggerParams.md) — parameters the logger records
- [LoggerGap](LoggerGap.md) — logger sampling interval
- [LoggerStatus](LoggerStatus.md) — logger run state
- [LoggerUpload](LoggerUpload.md) — retrieve logged data
