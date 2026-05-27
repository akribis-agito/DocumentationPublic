---
keyword: CurrCmdSlope
summary: Ramp rate (mA/s) toward each current-command table entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 568
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
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# CurrCmdSlope

Ramp rate (mA/s) toward each current-command table entry.

## Overview

`CurrCmdSlope` defines the slope for the transition from the starting `CurrRef` value to the active [CurrCmdVal](CurrCmdVal.md) entry, in milliamperes per second. It is applicable only when [CurrCmdSrc](CurrCmdSrc.md) = 1 or 2. The holding timer [CurrCmdCntr](CurrCmdCntr.md) only begins counting from 0 once the ramp completes.

## Examples

```text
ACurrCmdSlope[3]=700 ; ramp into entry 3 at 700 mA/s
```

Worked example — if `CurrCmdIndex` = 2, `CurrCmdCntr` = `CurrCmdHTime[2]` (end of the current entry), `CurrRef` = `CurrCmdVal[2]` = 340, `CurrCmdVal[3]` = -500, and `CurrCmdSlope[3]` = 700, then the ramp from 340 mA to -500 mA starts and completes in 1.2 seconds.

## See also

- [CurrCmdVal](CurrCmdVal.md) — target current values
- [CurrCmdHTime](CurrCmdHTime.md) — holding times per entry
- [CurrCmdCntr](CurrCmdCntr.md) — timer that starts after the ramp
