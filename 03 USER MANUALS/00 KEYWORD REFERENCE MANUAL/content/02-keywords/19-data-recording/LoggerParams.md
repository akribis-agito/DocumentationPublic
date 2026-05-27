---
keyword: LoggerParams
summary: Lists the parameters captured by the continuous data logger.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

Lists the parameters captured by the continuous data logger.

## Overview

`LoggerParams` is an array that specifies which controller parameters the continuous data logger records. Each element holds the [complex CAN code](../../01-keyword-usage-and-syntax/complex-can-code.md) of one parameter to be sampled during a logging session, so the logger configured by [LoggerOn](LoggerOn.md) knows what to capture. It is a non-axis parameter saved to flash, so the parameter selection persists across power cycles.

## How it works

The array is 1-indexed: `LoggerParams[1]` is the first logged parameter, up to 40 parameters in total. An element of `0` is treated as empty and selects no parameter. The complex CAN code encodes both the parameter and, for axis parameters, the axis it applies to, so the same parameter on different axes can be logged in the same session.

Each logged sample written to the buffer consists of a time stamp followed by one value per configured parameter; this determines the packet size reported by [LoggerStatus](LoggerStatus.md) (index 1). Adding more parameters makes each sample larger and therefore reduces the number of samples the fixed buffer can hold.

The parameter list is captured into the session metadata when logging starts and mirrored from index 4 onward of [LoggerAbout](LoggerAbout.md), so a host can interpret an upload even if the list is later changed. The sampling rate is set by [LoggerGap](LoggerGap.md).

## Examples

```text
ALoggerParams[1]=2     ; first logged parameter (complex CAN code)
ALoggerParams[2]=1026  ; second logged parameter
ALoggerParams[3]=0     ; clear the third slot (no parameter)
ALoggerParams[1]      ; query the first logged parameter
```

## See also

- [LoggerOn](LoggerOn.md) — start/stop the logger
- [LoggerGap](LoggerGap.md) — logger sampling interval
- [LoggerAbout](LoggerAbout.md) — metadata of the logged set
- [LoggerUpload](LoggerUpload.md) — retrieve logged data
