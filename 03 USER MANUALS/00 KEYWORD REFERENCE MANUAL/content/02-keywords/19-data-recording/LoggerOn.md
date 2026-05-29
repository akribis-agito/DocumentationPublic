---
keyword: LoggerOn
summary: Enables or disables the continuous data logger.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`LoggerOn` starts or stops the continuous data logger. When set to `1`, the logger begins sampling the parameters configured in [LoggerParams](LoggerParams.md) at the rate defined by [LoggerGap](LoggerGap.md); setting it to `0` stops logging. It is a non-axis parameter and is not saved to flash, so the logger always starts disabled after power-up.

## How it works

Setting `LoggerOn` from `0` to `1` prepares a fresh session in one step:

1. The parameter list in [LoggerParams](LoggerParams.md) is analyzed and the packet size (a time stamp plus one buffer slot per configured parameter) is computed and published in [LoggerStatus](LoggerStatus.md) (index 1).
2. The buffer is reset (free space set to full, packet identifier and lost-packets counter cleared), and the first sample is time-stamped at zero.
3. The current [LoggerFullMod](LoggerFullMod.md), start time, and parameter list are snapshotted into [LoggerAbout](LoggerAbout.md).

From then on, the logger evaluates one sample every [LoggerGap](LoggerGap.md) tick in the background, appending it to a circular buffer. When the buffer fills, the behavior selected by [LoggerFullMod](LoggerFullMod.md) applies. Setting `LoggerOn` back to `0` stops sampling immediately; data already in the buffer remains available for upload.

Unlike the recording scope (`Rec*` keywords), which captures a fixed-length, trigger-aligned window and is read back in one pass, the continuous logger runs indefinitely in the background and is drained incrementally: use [LoggerStatus](LoggerStatus.md) to monitor its state and [LoggerUpload](LoggerUpload.md) to retrieve completed packets as they accumulate. The logger has no trigger configuration.

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
