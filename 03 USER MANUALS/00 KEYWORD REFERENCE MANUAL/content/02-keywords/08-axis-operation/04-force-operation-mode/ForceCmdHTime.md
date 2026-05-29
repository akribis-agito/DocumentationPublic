---
keyword: ForceCmdHTime
summary: Holding time for each force-command table entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
  scaling: 65.536
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

Each cycle the generator reads the hold time for the active entry and branches on its sign:

| Value | Descriptions |
|---|---|
| < 0 | Source value is held indefinitely. The axis stays in force mode on this entry; for the table source the in-target detection still runs. |
| 0 | Axis exits force operation mode and enters position operation mode. When [ForcePIVOn](../../11-control-tuning/07-force-control/ForcePIVOn.md) is active, the velocity integrator is seeded on the way out to avoid a current-reference jump. |
| > 0 | Source value is held for `ForceCmdHTime`, before exiting force operation mode (`ForceCmdSrc` = 0) or proceeding to the next pair (`ForceCmdSrc` = 1 or 2). For `ForceCmdSrc` = 1 or 2, if [ForceCmdIndex](ForceCmdIndex.md) reaches the last index value and the last `ForceCmdHTime` entry is greater than 0, the axis holds the last `ForceCmdVal` value indefinitely. |

The hold time is timed by [ForceCmdCntr](ForceCmdCntr.md), which counts only while the reference is at the target value (ramp time is excluded). For the analog source only `ForceCmdHTime[1]` is consulted.

## Examples

```text
AForceCmdHTime[1]=400 ; hold first entry for 400 ms
AForceCmdHTime[2]=0   ; exit force mode after the second entry
```

### Edge cases

- **Index 0** — invalid; valid indices are `ForceCmdHTime[1]`–`ForceCmdHTime[20]`.
- **Wrong mode** ([OperationMode](../01-general-keywords/OperationMode.md) ≠ 4) — the table is **not consulted**.
- **Zero value** — exits force mode at that entry; with `ForcePIVOn = 1` the velocity integrator is seeded on exit to avoid a current-ref jump.
- **Negative value** — holds indefinitely; only an explicit mode change leaves the entry.
- **End of table (index 20 with positive HTime)** — the firmware holds the last value indefinitely.
- **Counter saturation** — [ForceCmdCntr](ForceCmdCntr.md) is clamped at 2 000 000 000 to avoid roll-over.
- **Analog source** ([ForceCmdSrc](ForceCmdSrc.md) = 0) — only `ForceCmdHTime[1]` is consulted; the rest of the array is unused.
- **Save** — flash-saveable.

## See also

- [ForceCmdVal](ForceCmdVal.md) — force values paired with these holding times
- [ForceCmdIndex](ForceCmdIndex.md) — active table entry
- [ForceCmdCntr](ForceCmdCntr.md) — elapsed time compared against this value
