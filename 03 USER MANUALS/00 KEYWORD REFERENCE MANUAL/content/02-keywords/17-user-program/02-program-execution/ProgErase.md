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

`ProgErase` erases the stored user program from controller memory. It is the inverse of downloading a program with [DownloadUPBin](DownloadUPBin.md). Because it removes the program the threads execute, it is blocked while the motor is on or the axis is in motion, and it cannot run while any thread is still active. It is a non-axis command and is not saved to flash.

## How it works

`ProgErase` first checks every thread; if even one thread is still running the command is rejected with an error and nothing is erased — stop all threads with [ProgHaltAll](ProgHaltAll.md) (or reset them) before erasing. When it does proceed, it:

- Marks the controller as having no stored program, so [ProgStat](ProgStat.md) reads `-1` for every thread and [ProgStatAll](ProgStatAll.md) reads `-1`.
- Sets every thread's [ProgPointer](ProgPointer.md) to `-1` (no program).
- Erases the program from the controller's non-volatile program memory.

After erasing, commands that need a program — such as [ProgRun](ProgRun.md), [ProgReset](ProgReset.md) and [ProgInfo](ProgInfo.md) — are rejected until a new program is downloaded with [DownloadUPBin](DownloadUPBin.md). Note that `ProgErase` also requires the motor to be off and the axis stopped, in addition to no thread running.

## Examples

```text
AProgErase           ; erase the stored user program (motor off, not in motion)
```

## See also

- [DownloadUPBin](DownloadUPBin.md) — download a compiled user program to the controller
- [ProgHaltAll](ProgHaltAll.md) — stop all threads before erasing
- [ProgResetAll](ProgResetAll.md) — stop all threads and reset pointers and stacks
- [ProgInfo](ProgInfo.md) — identify the program currently stored
