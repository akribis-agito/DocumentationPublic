---
keyword: ForceCmdSlope
summary: Ramp rate (unit/s) toward each force-command table entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 569
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2147483647
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceCmdSlope

Ramp rate (unit/s) toward each force-command table entry.

## Overview

`ForceCmdSlope` defines the slope for the transition from the starting [ForceRef](ForceRef.md) value to the active [ForceCmdVal](ForceCmdVal.md) entry, in units per second. It is applicable only when [ForceCmdSrc](ForceCmdSrc.md) = 1 or 2. The holding timer [ForceCmdCntr](ForceCmdCntr.md) only begins counting from 0 once the ramp completes.

## Examples

```text
ForceCmdSlope[3]=700 ; ramp into entry 3 at 700 units/s
```

## See also

- [ForceCmdVal](ForceCmdVal.md) — target force values
- [ForceCmdHTime](ForceCmdHTime.md) — holding times per entry
- [ForceCmdCntr](ForceCmdCntr.md) — timer that starts after the ramp
