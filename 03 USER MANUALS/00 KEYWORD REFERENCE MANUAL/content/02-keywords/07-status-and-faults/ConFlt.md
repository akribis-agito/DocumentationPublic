---
keyword: ConFlt
summary: Holds the controller error code that disabled the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 31
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - -3000
    - 0
---
# ConFlt

Holds the controller error code that disabled the axis.

## Overview

`ConFlt` stores the error code that caused the axis to be disabled. A value of `0` means no fault is present; any positive value is a controller fault code. Fault codes are numbered from a base of `1000`, so the first real fault is `1001` (abort signal) and the codes run up contiguously from there — see [Controller error codes](../../04-error-codes/controller-error-codes.md) for the full list and their meanings.

`ConFlt` is an axis-scoped register that is not saved to flash, so it always reflects the live fault state of that axis. It works together with the diagnostic snapshot pair [ConFltSnapSrc](ConFltSnapSrc.md) / [ConFltSnapVal](ConFltSnapVal.md), which freeze selected parameter values at the moment a fault occurs, and with [MotorReason](MotorReason.md), which reports the broader category of why the axis was disabled.

## How it works

When the controller detects a disabling fault it performs four actions together, atomically, for the affected axis:

1. The axis is disabled ([MotorOn](../08-axis-operation/01-general-keywords/MotorOn.md) is forced off).
2. `ConFlt` is loaded with the fault code.
3. A diagnostic snapshot is captured into [ConFltSnapVal](ConFltSnapVal.md).
4. The fault is appended to the controller [ErrLog](ErrLog.md), tagged with the axis letter, together with the power-on time.

Separately, when the axis transitions to disabled while a fault is present, [MotorReason](MotorReason.md) is set to `1` (controller fault).

Clearing:

- `ConFlt` is automatically cleared to `0` when the axis is re-enabled (`MotorOn=1`).
- You may write `0` to `ConFlt` to clear the fault status manually. Clearing `ConFlt` does **not** clear [ErrLog](ErrLog.md) or [ConFltSnapVal](ConFltSnapVal.md) — those persist for diagnosis.
- The writable range is `0…0`: `0` is the only value you can write. You cannot write a positive value to simulate a fault, and writing a non-zero value is rejected.

### Some common fault codes

A few representative codes appear below; the [Controller error codes](../../04-error-codes/controller-error-codes.md) page has the complete table.

| Code | Meaning |
|------|---------|
| 0 | No fault |
| 1001 | Abort signal was detected |
| 1003 | Encoder error (disconnected or other) |
| 1008 | Bus voltage too high |
| 1009 | Bus voltage too low |
| 1020 | Position error exceeds limit |
| 1024 | STO1 activated |
| 1040 | Motor temperature too high |
| 1043 | Central-i communication was disconnected |
| 1081 | CPU background-loop watchdog timeout |

## Examples

```text
AConFlt             ; read the current fault code (0 = no fault)
AConFlt=0            ; clear the fault status
```

## Changes between versions

The v5 (Central-i) firmware defines additional fault codes that do not exist in v4:

| Code | Meaning (v5 only) |
|------|---------|
| 1067 | Anomaly/collision detected in the system |
| 1071 | Unstable current loop detected |
| 1072 | High noise/jitter detected |
| 1080 | No phasing is detected |

The mechanism (set on fault, cleared on re-enable, appended to `ErrLog`) is identical in both versions.

## See also

- [Controller error codes](../../04-error-codes/controller-error-codes.md) — meaning of each fault code
- [MotorReason](MotorReason.md) — why the axis was disabled (fault vs. command)
- [ConFltSnapSrc](ConFltSnapSrc.md) / [ConFltSnapVal](ConFltSnapVal.md) — parameter snapshot captured at fault
- [ErrLog](ErrLog.md) — log that positive ConFlt values are appended to
- [MotorOn](../08-axis-operation/01-general-keywords/MotorOn.md) — re-enabling the axis clears ConFlt
