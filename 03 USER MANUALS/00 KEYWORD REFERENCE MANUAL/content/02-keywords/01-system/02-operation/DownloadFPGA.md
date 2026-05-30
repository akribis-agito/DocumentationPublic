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

`DownloadFPGA` switches the controller into FPGA-download mode, after which a new FPGA image can be transferred. It is a **command** (no value) and cannot be issued while the motor is on or in motion.

> **Use through Agito PCSuite only.** To avoid leaving a controller in an unexpected state, issue `DownloadFPGA` only via PCSuite's FPGA-download tab. Contact Agito if you need to drive the download from your own host software.

A firmware/FPGA version mismatch is reported by [UnitStat](../01-status/UnitStat.md).

## How it works

`DownloadFPGA` behaves differently by controller type:

- **Central-i controllers do not accept a separate FPGA download.** In the normal operating image `DownloadFPGA` returns instruction error 242 ("This function is not supported in this controller type") and the controller stays in normal operation. On central-i the FPGA configuration is carried inside the single combined firmware image and is updated as part of [DownloadFW](DownloadFW.md); there is no standalone FPGA transfer step.
- **Standalone controllers** perform a dedicated FPGA transfer that follows the same path as [DownloadFW](DownloadFW.md), just targeting the FPGA configuration image instead of the processor firmware:

  1. **Password handshake.** The controller requests a password and waits for the host to reply over the link the command arrived on (USB/serial or CAN). PCSuite supplies this automatically; a wrong reply, or no reply within about 10 seconds, leaves the unit in normal operation.
  2. **Quiesce hardware.** On success the serial bus is closed and the FPGA is reset so the drive outputs are safe, and the I/O pins are set to the mode the boot program expects.
  3. **Jump to boot.** The firmware records the originating interface and hands over to the boot program, which receives and writes the new FPGA image, then restarts the unit.

Firmware and FPGA images are versioned together; after updating one you may need to update the other so they match. The controller flags a mismatch in [UnitStat](../01-status/UnitStat.md) and will refuse to enable the motor while a relevant mismatch is present.

## See also

- [DownloadFW](DownloadFW.md) — equivalent command for the firmware image
- [DontDownload](../01-status/DontDownload.md) — interlock that blocks download
- [Reset](Reset.md) — graceful software restart used after a download
- [UnitStat](../01-status/UnitStat.md) — flags FW/FPGA image mismatches
