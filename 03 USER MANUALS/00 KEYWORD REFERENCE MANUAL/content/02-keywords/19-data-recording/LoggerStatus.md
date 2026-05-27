---
keyword: LoggerStatus
summary: Reports the current state of the continuous data logger.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`LoggerStatus` is a read-only array that reports the live state of the continuous data logger: its run state, how much buffer space is free, the current packet size, the running packet identifier, and a count of lost packets. It lets a host poll the logger started by [LoggerOn](LoggerOn.md) to decide when to call [LoggerUpload](LoggerUpload.md). It is a non-axis status variable and is not saved to flash. The buffer-full behavior it reflects is governed by [LoggerFullMod](LoggerFullMod.md).

## How it works

The array is 1-indexed. Each element reports one aspect of the logger:

| Index | Reports | Meaning |
|---|---|---|
| 1 | Packet size | Number of buffer slots one logged sample occupies (a time stamp plus one slot per configured parameter). 0 or 1 means no parameters are configured, so nothing is being logged. |
| 2 | Free space | Number of free slots remaining in the internal buffer. A full packet can be stored only while this is at least the packet size (index 1). |
| 3 | Run state | `0` not logging; `1` logging; `2` paused because the buffer is full (only possible when [LoggerFullMod](LoggerFullMod.md) = 0). |
| 4 | Packet identifier | Counter that advances by one each time a sample is due, whether or not it could be stored. Useful for detecting gaps. |
| 5 | Lost-packets counter | Number of due samples that could not be stored normally (buffer full): in stop mode (index 3 = 2) they were dropped; in overwrite mode the oldest sample was discarded to make room. |

A host typically starts the logger with [LoggerOn](LoggerOn.md), then polls index 3 for the run state and index 2 for accumulated data, and calls [LoggerUpload](LoggerUpload.md) to retrieve completed packets. A non-zero, growing index 5 indicates the buffer is not being uploaded fast enough.

## Examples

```text
ALoggerStatus[3]    ; query the logger run state (0/1/2)
ALoggerStatus[5]    ; query the lost-packets counter
```

## See also

- [LoggerOn](LoggerOn.md) — start/stop the logger
- [LoggerFullMod](LoggerFullMod.md) — buffer-full behavior
- [LoggerAbout](LoggerAbout.md) — session metadata
- [LoggerUpload](LoggerUpload.md) — retrieve logged data
