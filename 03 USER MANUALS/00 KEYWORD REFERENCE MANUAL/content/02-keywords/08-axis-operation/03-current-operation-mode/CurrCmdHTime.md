---
keyword: CurrCmdHTime
summary: Holding time for each current-command table entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 332
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
# CurrCmdHTime

Holding time for each current-command table entry.

## Overview

`CurrCmdHTime` defines the holding time, in milliseconds, of the current reference in current operation mode. Its use depends on [CurrCmdSrc](CurrCmdSrc.md):

- If `CurrCmdSrc` = 0 or 3 (analog input or slave drive): only `CurrCmdHTime[1]` is used, defining the time to stay within current operation mode.
- If `CurrCmdSrc` = 1 or 2 (user-defined table): each array element defines the holding time for the corresponding [CurrCmdVal](CurrCmdVal.md) entry.

## How it works

| Value | Descriptions |
|---|---|
| < 0 | Source value is held indefinitely. |
| 0 | Axis exits current operation mode and enters position operation mode. |
| > 0 | Source value is held for `CurrCmdHTime`, before exiting current operation mode (`CurrCmdSrc` = 0 or 3) or proceeding to the next pair (`CurrCmdSrc` = 1 or 2). For `CurrCmdSrc` = 1 or 2, if [CurrCmdIndex](CurrCmdIndex.md) reaches the last index value and the last `CurrCmdHTime` entry is greater than 0, the axis holds the last `CurrCmdVal` value indefinitely. |

## Examples

```text
CurrCmdHTime[1]=500 ; hold first entry for 500 ms
CurrCmdHTime[2]=0   ; exit current mode after the second entry
```

## See also

- [CurrCmdVal](CurrCmdVal.md) — current values paired with these holding times
- [CurrCmdIndex](CurrCmdIndex.md) — active table entry
- [CurrCmdCntr](CurrCmdCntr.md) — elapsed time compared against this value
