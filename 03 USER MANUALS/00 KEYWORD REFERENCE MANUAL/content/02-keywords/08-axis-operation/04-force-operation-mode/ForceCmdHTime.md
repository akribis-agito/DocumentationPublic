---
keyword: ForceCmdHTime
summary: Holding time for each force-command table entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 572
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - -2000000000
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceCmdHTime

Holding time for each force-command table entry.

## Overview

`ForceCmdHTime` defines the holding time, in milliseconds, of the force reference in force operation mode. Its use depends on [ForceCmdSrc](ForceCmdSrc.md):

- If `ForceCmdSrc` = 0 (analog input): only `ForceCmdHTime[1]` is used, defining the time to stay within force operation mode.
- If `ForceCmdSrc` = 1 or 2 (user-defined table): each array element defines the holding time for the corresponding [ForceCmdVal](ForceCmdVal.md) entry.

## How it works

| Value | Descriptions |
|---|---|
| < 0 | Source value is held indefinitely. |
| 0 | Axis exits force operation mode and enters position operation mode. |
| > 0 | Source value is held for `ForceCmdHTime`, before exiting force operation mode (`ForceCmdSrc` = 0) or proceeding to the next pair (`ForceCmdSrc` = 1 or 2). For `ForceCmdSrc` = 1 or 2, if [ForceCmdIndex](ForceCmdIndex.md) reaches the last index value and the last `ForceCmdHTime` entry is greater than 0, the axis holds the last `ForceCmdVal` value indefinitely. |

## Examples

```text
ForceCmdHTime[1]=400 ; hold first entry for 400 ms
ForceCmdHTime[2]=0   ; exit force mode after the second entry
```

## See also

- [ForceCmdVal](ForceCmdVal.md) — force values paired with these holding times
- [ForceCmdIndex](ForceCmdIndex.md) — active table entry
- [ForceCmdCntr](ForceCmdCntr.md) — elapsed time compared against this value
