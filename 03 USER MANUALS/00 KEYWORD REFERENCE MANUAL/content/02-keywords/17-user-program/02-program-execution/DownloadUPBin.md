---
keyword: DownloadUPBin
summary: Command that transfers a compiled user-program binary image into controller program memory.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`DownloadUPBin` transfers a compiled user-program binary image into the controller's program memory, loading the program that the controller will subsequently execute. It is a non-axis command and is not saved to flash. Because it rewrites program memory, it cannot run while the axis is in motion or while the motor is on (`ok_in_motion: false`, `ok_motor_on: false`); stop motion and disable the motor first.

A typical workflow is to erase any existing program with [ProgErase](ProgErase.md), download the new image with `DownloadUPBin`, then reset the program state with [ProgReset](ProgReset.md) before running it.

## Examples

```text
; Issue with the motor off and no motion in progress
ADownloadUPBin       ; transfer the compiled user-program binary into program memory
```

## See also

- [ProgErase](ProgErase.md) — erase the current user program
- [ProgReset](ProgReset.md) — reset user-program state
- [ProgStatAll](ProgStatAll.md) — status of all user-program threads
