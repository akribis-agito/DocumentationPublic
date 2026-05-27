---
keyword: DownloadFPGA
summary: Command that puts the controller into FPGA-download mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 231
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
# DownloadFPGA

Command that puts the controller into FPGA-download mode.

## Overview

`DownloadFPGA` switches the controller into FPGA-download mode, after which a new FPGA image can be transferred. It cannot be issued while the motor is on or in motion.

> **Use through Agito PCSuite only.** To avoid leaving a controller in an unexpected state, issue `DownloadFPGA` only via PCSuite's FPGA-download tab. Contact Agito if you need to drive the download from your own host software.

A firmware/FPGA version mismatch is reported by [UnitStat](../01-status/UnitStat.md).

## See also

- [DownloadFW](DownloadFW.md) — equivalent command for the firmware image
- [DontDownload](../01-status/DontDownload.md) — interlock that blocks download
- [UnitStat](../01-status/UnitStat.md) — flags FW/FPGA image mismatches
