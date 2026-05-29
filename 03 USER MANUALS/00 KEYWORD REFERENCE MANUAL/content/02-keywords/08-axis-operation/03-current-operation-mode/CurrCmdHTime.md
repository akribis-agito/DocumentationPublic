---
keyword: CurrCmdHTime
summary: Holding time for each current-command table entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
  scaling: 65.536
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
| > 0 | Source value is held for `CurrCmdHTime`, before exiting current operation mode (`CurrCmdSrc` = 0 or 3) or proceeding to the next pair (`CurrCmdSrc` = 1 or 2). For `CurrCmdSrc` = 1 or 2, if [CurrCmdIndex](CurrCmdIndex.md) reaches the last usable entry (20) and that entry's `CurrCmdHTime` is greater than 0, the axis holds the last `CurrCmdVal` value indefinitely. |

The holding time is accumulated by the [CurrCmdCntr](CurrCmdCntr.md) counter, which advances once per control cycle. For sources 1 and 2 the counter only starts after `CurrRef` has finished ramping to the entry's [CurrCmdVal](CurrCmdVal.md) (see [CurrCmdSlope](CurrCmdSlope.md)); for sources 0 and 3 it starts immediately on mode entry. When the counter reaches `CurrCmdHTime[1]` (sources 0/3) the axis switches to position mode; when it reaches `CurrCmdHTime[index]` (sources 1/2) the axis advances to the next table entry.

## Examples

```text
ACurrCmdHTime[1]=500 ; hold first entry for 500 ms
ACurrCmdHTime[2]=0   ; exit current mode after the second entry
```

### Edge cases

- **Index 0** — invalid; valid indices are `CurrCmdHTime[1]`–`CurrCmdHTime[20]`. `CurrCmdHTime[0]` does not exist.
- **Wrong mode** ([OperationMode](../01-general-keywords/OperationMode.md) ≠ 1) — the table is **not consulted**; values are stored but not timed.
- **Zero value** — exits current mode to position mode at the end of the corresponding `CurrCmdVal` entry. **`CurrCmdHTime[1] = 0` with `CurrCmdSrc` = 0 / 3 returns to position mode immediately** on entering current mode.
- **Negative value** — holds the value indefinitely; only an explicit mode change ([GoToPosMode](../02-position-operation-mode/GoToPosMode.md), `OperationMode` direct write, or DInMode) leaves the entry.
- **End of table** — when `CurrCmdIndex` reaches `20` and that entry's `CurrCmdHTime > 0`, the firmware holds the last value indefinitely rather than advancing past 20.
- **Counter saturation** — [CurrCmdCntr](CurrCmdCntr.md) is clamped at 2 000 000 000 to avoid roll-over; very long holds remain comparable to `CurrCmdHTime`.
- **HTime > CurrCmdHTime max** — values outside ±2 000 000 000 are rejected.
- **Save** — flash-saveable.

## See also

- [CurrCmdVal](CurrCmdVal.md) — current values paired with these holding times
- [CurrCmdIndex](CurrCmdIndex.md) — active table entry
- [CurrCmdCntr](CurrCmdCntr.md) — elapsed time compared against this value
