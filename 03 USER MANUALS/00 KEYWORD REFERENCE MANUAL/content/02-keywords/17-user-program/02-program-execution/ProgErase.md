---
keyword: ProgErase
summary: Erases the stored user program from controller memory.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 299
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
# ProgErase

Erases the stored user program from controller memory.

## Overview

`ProgErase` is a command that erases the stored user program from controller memory. It is the inverse of downloading a program with [DownloadUPBin](DownloadUPBin.md). Because it removes the running program, it cannot be executed while the axis is in motion or with the motor on; stop and reset tasks first (see [ProgResetAll](ProgResetAll.md)). It is a non-axis command and is not saved to flash.

## Examples

```text
AProgErase           ; erase the stored user program (motor off, not in motion)
```

## See also

- [DownloadUPBin](DownloadUPBin.md) — download a compiled user program to the controller
- [ProgReset](ProgReset.md) — reset a task to its initial state
- [ProgResetAll](ProgResetAll.md) — stop all threads and reset pointers and stacks
