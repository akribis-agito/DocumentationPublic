---
keyword: LoggerUpload
summary: Command that transfers the logged data buffer to the host.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

Command that transfers the logged data buffer to the host.

## Overview

`LoggerUpload` is a command that initiates transfer of the logged data buffer from the controller to the host. It can be invoked while the logger started by [LoggerOn](LoggerOn.md) is active or after it has stopped. It is the continuous-logger counterpart of [RecUpload](RecUpload.md) for the recording scope. It is a non-axis command and is not saved to flash. Use [LoggerAbout](LoggerAbout.md) to interpret the uploaded contents.

## Examples

```text
ALoggerUpload        ; stream the logged data buffer to the host
```

## See also

- [LoggerOn](LoggerOn.md) — start/stop the logger
- [LoggerStatus](LoggerStatus.md) — logger run state and buffer fill
- [LoggerAbout](LoggerAbout.md) — session metadata
- [RecUpload](RecUpload.md) — equivalent upload for the recording scope
