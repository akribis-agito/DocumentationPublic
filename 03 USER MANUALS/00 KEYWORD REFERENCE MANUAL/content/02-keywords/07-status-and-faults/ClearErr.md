---
keyword: ClearErr
summary: Command that clears the controller error log (ErrLog).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`ClearErr` empties the [ErrLog](ErrLog.md) array, discarding all recorded error entries and their timestamps and rewinding the log's write position back to `ErrLog[1]`, so newly logged errors start from a clean slate. Use it after you have reviewed or exported the log.

`ClearErr` is a non-axis command (it acts on the unit-wide log) and takes no value — issuing the keyword runs the command. It is not saved to flash and may be issued at any time, including while a motor is enabled or in motion.

## How it works

`ClearErr` clears **only** the error log:

1. The internal ring-buffer write index is reset to the start, so any error that occurs during the clear is written to the front of the array (and then cleared too).
2. Every element of `ErrLog` is set to `0`.
3. Interrupts are briefly disabled to clear any entries that the control interrupt may have pushed while the bulk clear was running, then the write index is reset again.

It does **not** clear [ConFlt](ConFlt.md), [ConFltSnapVal](ConFltSnapVal.md), or [MotorReason](MotorReason.md) — those reflect the current fault state and are cleared separately (by re-enabling the axis, or by writing `0` to `ConFlt`).

## Examples

```text
AClearErr            ; clear all entries from the error log
```

## See also

- [ErrLog](ErrLog.md) — the error log this command clears
- [ConFlt](ConFlt.md) — the per-axis fault code; positive values are appended to ErrLog
- [ConFltSnapVal](ConFltSnapVal.md) — fault snapshot, not affected by ClearErr
