---
keyword: ProgBreaks
summary: Per-thread breakpoint settings for user program debugging.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 294
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 4
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgBreaks

Per-thread breakpoint settings for user program debugging.

## Overview

`ProgBreaks` is a read/write array parameter that holds breakpoint settings used when debugging a user program. The default value of `-1` indicates no breakpoint is set. It is typically managed by the PC Suite debugger together with [ProgSingle](ProgSingle.md) (single-step) and [ProgBreakThis](ProgBreakThis.md) (break the running task). It is a non-axis parameter and is not saved to flash.

> **Documentation pending:** The per-element meaning of `ProgBreaks` is not fully described in the source reference. Refer to the User Program Language Manual for complete details.

## See also

- [ProgBreakThis](ProgBreakThis.md) — set a breakpoint on the running task
- [ProgSingle](ProgSingle.md) — single-step execution of a thread
- [ProgPointer](ProgPointer.md) — current instruction pointer of each task
