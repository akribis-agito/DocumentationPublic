---
keyword: LoggerParams
summary: Lists the parameters captured by the continuous data logger.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`LoggerParams` is an array that specifies which controller parameters the continuous data logger records. Each array element identifies one parameter to be sampled during a logging session, so the logger configured by [LoggerOn](LoggerOn.md) knows what to capture. It is a non-axis parameter saved to flash, so the parameter selection persists across power cycles.

The array is 1-indexed: `LoggerParams[1]` is the first logged parameter. Metadata describing the captured set is reported by [LoggerAbout](LoggerAbout.md), and the recording rate is set by [LoggerGap](LoggerGap.md).

## Examples

```text
LoggerParams[1]=2     ; first logged parameter
LoggerParams[2]=1026  ; second logged parameter
LoggerParams[1]?      ; query the first logged parameter
```

## See also

- [LoggerOn](LoggerOn.md) — start/stop the logger
- [LoggerGap](LoggerGap.md) — logger sampling interval
- [LoggerAbout](LoggerAbout.md) — metadata of the logged set
- [LoggerUpload](LoggerUpload.md) — retrieve logged data
