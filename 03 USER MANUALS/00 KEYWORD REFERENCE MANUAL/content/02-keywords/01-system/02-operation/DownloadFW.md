---
keyword: DownloadFW
summary: Command that puts the controller into firmware-download mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 230
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DownloadFW

Command that puts the controller into firmware-download mode.

## Overview

`DownloadFW` switches the controller into firmware-download mode, after which a new firmware image can be transferred. It cannot be issued while the motor is on or in motion.

> **Use through Agito PCSuite only.** To avoid leaving a controller in an unexpected state, issue `DownloadFW` only via PCSuite's firmware-download tab. Contact Agito if you need to drive the download from your own host software.

The [DontDownload](../01-status/DontDownload.md) flag, when set, blocks firmware download as a safety interlock.

## See also

- [DownloadFPGA](DownloadFPGA.md) — equivalent command for the FPGA image
- [DontDownload](../01-status/DontDownload.md) — interlock that blocks firmware download
- [FWInfo](../01-status/FWInfo.md) — current firmware version
