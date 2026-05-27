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

`LoggerAbout` is a read-only array that reports metadata about the current logger session: the buffer-full mode in force, the time logging started, and a snapshot of the logged-parameter list. It lets a host application interpret the data returned by [LoggerUpload](LoggerUpload.md) without separately re-querying the configuration. The snapshot is taken at the moment the logger is enabled, so it reflects the configuration that the captured data was actually recorded with, even if [LoggerParams](LoggerParams.md) or [LoggerFullMod](LoggerFullMod.md) are changed afterward. It is a non-axis status variable and is not saved to flash.

## How it works

The array is 1-indexed and laid out as follows:

| Index | Reports | Meaning |
|---|---|---|
| 1 | (reserved) | Not used in this firmware version; the sampling interval is taken live from [LoggerGap](LoggerGap.md) so it can be changed on the fly. Reads back as an uninitialized marker value. |
| 2 | Buffer-full mode | Snapshot of [LoggerFullMod](LoggerFullMod.md) at the moment logging started: `0` stop when full, `1` overwrite oldest. |
| 3 | Start time | Controller time stamp captured when the session started. |
| 4 onward | Logged parameters | Snapshot of [LoggerParams](LoggerParams.md): index `4` mirrors `LoggerParams[1]`, index `5` mirrors `LoggerParams[2]`, and so on for the configured parameters. |

The snapshot (indices 2 onward) is refreshed each time the logger transitions from off to on through [LoggerOn](LoggerOn.md).

## Examples

```text
ALoggerAbout[2]     ; query the buffer-full mode the session is using
ALoggerAbout[3]     ; query the session start time stamp
ALoggerAbout[4]     ; query the first logged parameter of the session
```

## See also

- [LoggerOn](LoggerOn.md) — start/stop the logger
- [LoggerParams](LoggerParams.md) — parameters the logger records
- [LoggerStatus](LoggerStatus.md) — logger run state
- [LoggerUpload](LoggerUpload.md) — retrieve logged data
