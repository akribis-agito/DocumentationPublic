---
keyword: AOutMode
summary: Selects direct command mode or parameter-monitoring mode for each analog output.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 220
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
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
# AOutMode

Selects direct command mode or parameter-monitoring mode for each analog output.

## Overview

`AOutMode` sets whether an analog output is in **direct command mode** or **monitoring mode**. The array index is the analog-output number (e.g. `AOutMode[2]` is analog output 2).

| Value | Mode |
|-------|------|
| 0 | Direct command mode — the output follows [AOutPort](AOutPort.md) |
| CCC | Monitoring mode — the output emulates the parameter whose Complex CAN code (CCC) is given |

In monitoring mode the emulated parameter is treated as millivolts, scaled by [AOutShifts](AOutShifts.md) and offset by [AOutOffset](AOutOffset.md). See the [analog-output overview](00-overview.md).

## Examples

```text
AAOutMode[1]=0       ; direct command mode
AAOutMode[1]=<CCC>   ; monitor a parameter (use its Complex CAN code)
```

## See also

- [AOutPort](AOutPort.md) — commanded value (direct mode)
- [AOutShifts](AOutShifts.md) — scaling (monitoring mode)
- [AOutOffset](AOutOffset.md) — output offset
