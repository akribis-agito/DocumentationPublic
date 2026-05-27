---
keyword: ProgInfo
summary: Reports the information strings embedded in the loaded user program.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`ProgInfo` inquires the list of information strings included with the loaded user program: the CRC value, the date, the CUP file name, and the free-text information supplied through the `#information` compiler directive. It is used to identify which program is currently resident on the controller (compare with [ProgErase](ProgErase.md) and [DownloadUPBin](DownloadUPBin.md), which remove and load programs). It is a non-axis status command and is not saved to flash.

## Examples

```text
ProgInfo?           ; report CRC, date, CUP file name and #information text
```

## See also

- [DownloadUPBin](DownloadUPBin.md) — download a compiled user program
- [ProgErase](ProgErase.md) — erase the stored user program
- [ProgStatAll](ProgStatAll.md) — combined status of all tasks
