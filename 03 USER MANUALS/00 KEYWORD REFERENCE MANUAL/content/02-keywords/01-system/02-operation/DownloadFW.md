---
keyword: DownloadFW
summary: Command that puts the controller into firmware-download mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`DownloadFW` switches the controller into firmware-download mode, after which a new firmware image can be transferred. It is a **command** (no value) and cannot be issued while the motor is on or in motion.

> **Use through Agito PCSuite only.** To avoid leaving a controller in an unexpected state, issue `DownloadFW` only via PCSuite's firmware-download tab. Contact Agito if you need to drive the download from your own host software.

The [DontDownload](../01-status/DontDownload.md) flag, when set, blocks firmware download as a safety interlock.

## How it works

`DownloadFW` hands control from the running firmware to the on-board boot program, which performs the actual image transfer. The sequence is:

1. **Password handshake.** The controller requests a password and waits for the host to send the expected reply over the same link the command arrived on (USB/serial, CAN, or Ethernet). PCSuite supplies this automatically. A wrong reply returns a password error; no reply within about 10 seconds returns a timeout error — in either case the controller stays in normal operation.
2. **Quiesce hardware.** On success the serial bus is closed and the FPGA is reset so the drive outputs are taken to a safe state, and the I/O pins are returned to the mode the boot program expects.
3. **Jump to boot.** The firmware records which interface initiated the download and jumps to the boot program, which receives and writes the new image. The download tool then restarts the unit; on the next start-up the controller runs the new firmware.

Because the password and timeout handshake differ per interface and must be matched exactly, this command is intended to be driven by PCSuite rather than by hand.

## See also

- [DownloadFPGA](DownloadFPGA.md) — equivalent command for the FPGA image
- [DontDownload](../01-status/DontDownload.md) — interlock that blocks firmware download
- [Reset](Reset.md) — graceful software restart (used to re-enter normal mode after download)
- [FWInfo](../01-status/FWInfo.md) — current firmware version
