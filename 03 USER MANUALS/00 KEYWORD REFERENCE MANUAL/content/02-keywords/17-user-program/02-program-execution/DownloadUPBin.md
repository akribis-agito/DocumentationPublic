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
---
# DownloadUPBin

Command that transfers a compiled user-program binary image into controller program memory.

## Overview

`DownloadUPBin` transfers a compiled user-program binary image into the controller's program memory, loading the program that the controller will subsequently execute. It is a non-axis command and is not saved to flash. Because it rewrites program memory, it cannot run while the axis is in motion or while the motor is on; stop motion and disable the motor first.

A typical workflow is to erase any existing program with [ProgErase](ProgErase.md), download the new image with `DownloadUPBin`, then reset the program state with [ProgReset](ProgReset.md) before running it.

## How it works

`DownloadUPBin` starts a transfer on whichever communication channel issued the command (serial, CAN, or Ethernet). After the command is accepted, the host streams the compiled binary as a sequence of fixed-length data blocks. The controller appends each block to program memory in order until it receives the end-of-file marker that terminates the image. The transfer is guarded by a timeout: if blocks stop arriving before the end-of-file marker is seen, the download aborts with an error and the program memory is left incomplete, so the image must be downloaded again.

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
