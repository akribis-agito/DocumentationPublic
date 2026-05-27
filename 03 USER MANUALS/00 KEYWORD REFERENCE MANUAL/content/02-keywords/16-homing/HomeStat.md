---
keyword: HomeStat
summary: Read-only bit-field reporting the homing status of the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 111
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HomeStat

Read-only bit-field reporting the homing status of the axis.

## Overview

`HomeStat` is a read-only, axis-scoped status variable (not saved to flash) that reports the current status of the homing procedure as a bit-field, indicating whether the axis has been homed, whether a homing sequence is in progress, and any homing error conditions. It is read alongside [HomingStat](HomingStat.md) (homing-process status and error codes) and [HomingStep](HomingStep.md) (last completed step) when monitoring or diagnosing the homing run started by [HomingOn](HomingOn.md).

> **Documentation pending:** the individual bit assignments of `HomeStat` are not documented in the source material. Use [HomingStat](HomingStat.md) for the documented per-step status and error codes.

## Examples

```text
HomeStat?           ; read the homing status bit-field
```

## See also

- [HomingStat](HomingStat.md) — homing-process status and documented error codes
- [HomingStep](HomingStep.md) — index of the last completed homing step
- [HomingOn](HomingOn.md) — starts the homing process
