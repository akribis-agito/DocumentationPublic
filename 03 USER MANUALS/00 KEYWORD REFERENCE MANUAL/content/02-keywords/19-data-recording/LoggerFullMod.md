---
keyword: LoggerFullMod
summary: Selects logger behavior when its buffer fills (overwrite or stop).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 533
attributes:
  access: rw
  scope: non-axis
  flash: true
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
# LoggerFullMod

Selects logger behavior when its buffer fills (overwrite or stop).

## Overview

`LoggerFullMod` sets the behavior of the continuous data logger when its internal buffer becomes full, selecting between a stop mode and an overwrite (circular) mode. This determines whether long-running logging freezes at the first full buffer or keeps the most recent samples. It is a non-axis parameter saved to flash and can be changed at any time. It works together with [LoggerOn](LoggerOn.md) and [LoggerGap](LoggerGap.md), and is observed through [LoggerStatus](LoggerStatus.md).

## How it works

The value selects what happens when a new sample is due but the buffer has no room for a full packet:

| Value | Mode | Behavior when the buffer is full |
|---|---|---|
| 0 | Stop (pause) | The new sample is dropped and the logger reports a paused state ([LoggerStatus](LoggerStatus.md) index 3 = 2). Logging resumes automatically once the host frees space by calling [LoggerUpload](LoggerUpload.md). Earlier samples are preserved. |
| 1 | Overwrite (circular) | The oldest stored sample is discarded to make room for the new one, so the buffer always holds the most recent samples. (If the oldest sample is being uploaded at that instant, that one sample is dropped instead.) |

In both modes, every dropped or overwritten sample increments the lost-packets counter reported by [LoggerStatus](LoggerStatus.md) (index 5). The mode in force is captured into the session metadata when the logger is enabled and reported by [LoggerAbout](LoggerAbout.md) (index 2). A running session keeps the mode it started with; change `LoggerFullMod` before enabling the logger (or stop and restart it) for the new setting to take effect.

## Examples

```text
ALoggerFullMod=0    ; stop (pause) logging when the buffer fills
ALoggerFullMod=1    ; overwrite oldest samples (circular buffer)
ALoggerFullMod      ; query the current buffer-full mode
```

## See also

- [LoggerOn](LoggerOn.md) — start/stop the logger
- [LoggerStatus](LoggerStatus.md) — logger run state and buffer fill
- [LoggerGap](LoggerGap.md) — logger sampling interval
