---
keyword: DontDownload
summary: Read-only safety interlock that, when set, blocks firmware download.
availability:
  standalone:
  - v4
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

`DontDownload` is a read-only flag that reflects whether the running image will reject a firmware download. A value of `0` allows downloads; `1` blocks them. It is non-axis and not saved to flash, so it reflects the controller's live state.

## How it works

The flag is set during start-up. On the relevant platform, if the unit powers up with its **"force download firmware" configuration DIP switch** asserted, the running application sets `DontDownload = 1` and, in the application (non-boot) image, erases the header of the firmware image currently in flash. With the header erased, the next power cycle boots the **golden image** instead of the application, and a normal [DownloadFW](../02-operation/DownloadFW.md) can then proceed.

In effect, `DontDownload = 1` indicates the unit is mid–recovery: the current application has invalidated itself so that a clean download can be performed from the golden boot image after a power cycle. In normal operation the flag reads `0`. A host should read it before attempting a download and, if it is set, power-cycle the unit first.

## Examples

```text
ADontDownload       ; check whether firmware download is currently blocked
```

## See also

- [DownloadFW](../02-operation/DownloadFW.md) / [DownloadFPGA](../02-operation/DownloadFPGA.md) — the firmware/FPGA download commands this flag gates
- [UnitStat](UnitStat.md) — unit hardware/firmware health
