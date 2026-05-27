---
keyword: DontDownload
summary: Read-only safety interlock that, when set, blocks firmware download.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 670
attributes:
  access: ro
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
# DontDownload

Read-only safety interlock that, when set, blocks firmware download.

## Overview

`DontDownload` is a read-only flag that acts as a safety interlock against accidental firmware updates. When it is non-zero, the host is prevented from downloading a new firmware image to the controller — useful for protecting a unit during critical operation. A value of `0` allows downloads; `1` blocks them. It is non-axis and not saved to flash, so it reflects the controller's live state.

## Examples

```text
ADontDownload       ; check whether firmware download is currently blocked
```

## See also

- [DownloadFW](../02-operation/DownloadFW.md) / [DownloadFPGA](../02-operation/DownloadFPGA.md) — the firmware/FPGA download commands this flag gates
- [UnitStat](UnitStat.md) — unit hardware/firmware health
