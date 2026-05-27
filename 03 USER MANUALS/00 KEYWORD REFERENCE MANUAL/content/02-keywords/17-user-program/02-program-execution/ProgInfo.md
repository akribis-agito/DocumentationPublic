---
keyword: ProgInfo
summary: Reports the information strings embedded in the loaded user program.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 297
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgInfo

Reports the information strings embedded in the loaded user program.

## Overview

`ProgInfo` returns the information strings stored with the loaded user program: the CRC value, the date, the CUP file name, and the free-text information supplied through the `#information` compiler directive. It is used to identify which program is currently resident on the controller (compare with [ProgErase](ProgErase.md) and [DownloadUPBin](DownloadUPBin.md), which remove and load programs). It is a non-axis status command and is not saved to flash.

## How it works

When a program is downloaded, a header is stored ahead of the program code holding its identifying details — the CRC, build date, source file name, the `#information` text, and the internal tables of tasks, functions, global variables and events. `ProgInfo` streams this header back to the requesting interface (the free-text print strings used by the program at run time are excluded from the report). It requires a stored program; if none is loaded the command is rejected. The reported CRC is the value the controller uses to verify program integrity, so it is a reliable way to confirm that the exact expected program is resident before running it.

## Examples

```text
AProgInfo           ; report CRC, date, CUP file name and #information text
```

## See also

- [DownloadUPBin](DownloadUPBin.md) — download a compiled user program
- [ProgErase](ProgErase.md) — erase the stored user program
- [ProgStatAll](ProgStatAll.md) — combined status of all tasks
