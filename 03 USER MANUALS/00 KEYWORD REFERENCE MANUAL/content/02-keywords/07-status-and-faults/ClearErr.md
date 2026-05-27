---
keyword: ClearErr
summary: Command that clears the controller error log (ErrLog).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 236
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ClearErr

Command that clears the controller error log (ErrLog).

## Overview

`ClearErr` empties the [ErrLog](ErrLog.md) array, discarding all recorded error entries and their timestamps. Use it after you have reviewed or exported the log so that newly logged errors start from a clean slate.

`ClearErr` is a non-axis command (it acts on the unit-wide log) and takes no value — issuing the keyword runs the command. It is not saved to flash and may be issued at any time, including while a motor is enabled or in motion.

## Examples

```text
ClearErr            ; clear all entries from the error log
```

## See also

- [ErrLog](ErrLog.md) — the error log this command clears
- [ConFlt](ConFlt.md) — the per-axis fault code; positive values are appended to ErrLog
