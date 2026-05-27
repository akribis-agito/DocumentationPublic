---
keyword: LoggerAbout
summary: Reports metadata about the current continuous logger session.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

Reports metadata about the current continuous logger session.

## Overview

`LoggerAbout` is a read-only array that reports metadata about the current logger session, including the list of logged parameters and session configuration information. It lets a host application interpret the data returned by [LoggerUpload](LoggerUpload.md) without separately re-querying the configuration. It is a non-axis status variable and is not saved to flash. The configuration it describes is set through [LoggerParams](LoggerParams.md), [LoggerGap](LoggerGap.md), and [LoggerOn](LoggerOn.md).

> **Documentation pending:** the per-index layout of the 44-element array is not specified in the source material.

## Examples

```text
ALoggerAbout[1]     ; query the first metadata element
```

## See also

- [LoggerOn](LoggerOn.md) — start/stop the logger
- [LoggerParams](LoggerParams.md) — parameters the logger records
- [LoggerStatus](LoggerStatus.md) — logger run state
- [LoggerUpload](LoggerUpload.md) — retrieve logged data
