---
keyword: ErrLog
summary: Read-only circular log of recent errors with their timestamps.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 235
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 65
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ErrLog

Read-only circular log of recent errors with their timestamps.

## Overview

`ErrLog` holds the controller's error log. It is a unit-wide (non-axis), read-only array of 65 elements that records errors as they occur, together with the time each one happened, so you can reconstruct the sequence of faults after a problem. It is not saved to flash. Each positive [ConFlt](ConFlt.md) value is appended here automatically, and the entire log can be wiped with [ClearErr](ClearErr.md).

The easiest way to read `ErrLog` is with the Agito PCSuite software, which translates each error code to text and converts the power-on time to a clock reading using the PC clock.

## How it works

When an error occurs, two values are saved in `ErrLog`:

- Axis and error code
- Error time (in seconds, counting from when the unit was powered on)

The axis and error code of the first error are logged in `ErrLog[1]`, and the error time of the first error is in `ErrLog[2]`. Subsequent errors are saved in higher array locations, `ErrLog[3]` and `ErrLog[4]`, and so on. When the end of the array is reached, the log circles back to the first entry and overwrites it.

The axis and error code are stored together: the axis information (see table below) occupies the upper 8 bits, and the error code (see [Controller error codes](../../04-error-codes/controller-error-codes.md)) occupies the lower 24 bits.

| Axis | A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Value (upper 8 bit) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |

The time of the error in `ErrLog` is in seconds since power on.

## Examples

```text
AErrLog[1]          ; axis + error code of the first logged error
AErrLog[2]          ; time (s since power-on) of the first logged error
AErrLog             ; read the full log
```

## See also

- [ClearErr](ClearErr.md) — clear all entries from this log
- [ConFlt](ConFlt.md) — per-axis fault code appended to this log
- [Controller error codes](../../04-error-codes/controller-error-codes.md) — meaning of each error code
