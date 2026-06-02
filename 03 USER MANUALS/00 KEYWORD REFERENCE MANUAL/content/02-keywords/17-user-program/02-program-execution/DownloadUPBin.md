---
keyword: DownloadUPBin
summary: Command that transfers a compiled user-program binary image into controller program memory.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 207
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# DownloadUPBin

Command that transfers a compiled user-program binary image into controller program memory.

## Overview

`DownloadUPBin` transfers a compiled user-program binary image into the controller's non-volatile program storage, loading the program that the controller will subsequently execute. The downloaded program is retained across power cycles. It is a non-axis command. Because it erases and reprograms the program storage area, it cannot run while the axis is in motion or while the motor is on; stop motion and disable the motor first.

A typical workflow is to erase any existing program with [ProgErase](ProgErase.md), download the new image with `DownloadUPBin`, then reset the program state with [ProgReset](ProgReset.md) before running it.

## How it works

`DownloadUPBin` first halts any running user-program threads, then erases the program storage area. If the erase fails the command returns error 27 and no transfer begins. Otherwise the controller acknowledges with `OK` and the host streams the compiled binary as a sequence of 8-byte data blocks on whichever communication channel issued the command (serial, CAN, or Ethernet); each block is written to storage as it arrives. The transfer ends when the host sends a block of eight carriage-return bytes as the end-of-file marker. A block of an unexpected length during the transfer aborts it with error 15.

The transfer is guarded by a 10-second timeout: if blocks stop arriving before the end-of-file marker is seen, the download aborts. On a timeout the controller sends no reply at all, because the link is assumed to be out of sync, and no valid program is left in storage. When the end-of-file marker is received normally, the controller writes a completion signature and verifies the program's checksum; if the checksum does not match, the signature is erased (so no program is present) and the command returns error 171. A failed or interrupted download therefore leaves the controller with no usable program, and the image must be downloaded again.

Because the program file is compiled for a specific layout, the binary must be produced by the PC Suite for the target controller; the offsets that keywords such as [Jump](Jump.md) rely on are fixed when the file is built.

## Examples

```text
; Issue with the motor off and no motion in progress
ADownloadUPBin       ; transfer the compiled user-program binary into program memory
```

## See also

- [ProgErase](ProgErase.md) — erase the current user program
- [ProgReset](ProgReset.md) — reset user-program state
- [ProgStatAll](ProgStatAll.md) — status of all user-program threads
