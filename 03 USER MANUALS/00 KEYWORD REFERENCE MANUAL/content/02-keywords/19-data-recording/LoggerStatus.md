---
keyword: LoggerStatus
summary: Reports the current state of the continuous data logger.
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

Reports the current state of the continuous data logger.

## Overview

`LoggerStatus` is a read-only array that reports the current state of the data logger, including whether it is active, the number of samples collected, and the buffer fill level. It lets a host poll the logger started by [LoggerOn](LoggerOn.md) to decide when to call [LoggerUpload](LoggerUpload.md). It is a non-axis status variable and is not saved to flash. The buffer-full behavior it reflects is governed by [LoggerFullMod](LoggerFullMod.md).

> **Documentation pending:** the per-index layout of the 6-element array is not specified in the source material.

## Examples

```text
ALoggerStatus[1]    ; query the first status element
```

## See also

- [LoggerOn](LoggerOn.md) — start/stop the logger
- [LoggerFullMod](LoggerFullMod.md) — buffer-full behavior
- [LoggerAbout](LoggerAbout.md) — session metadata
- [LoggerUpload](LoggerUpload.md) — retrieve logged data
