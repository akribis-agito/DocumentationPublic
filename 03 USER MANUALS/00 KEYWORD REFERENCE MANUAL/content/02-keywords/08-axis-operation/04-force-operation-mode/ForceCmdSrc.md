---
keyword: ForceCmdSrc
summary: Selects the source of the force reference in force mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 570
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceCmdSrc

Selects the source of the force reference in force mode.

## Overview

`ForceCmdSrc` sets the source of the force reference ([ForceRef](ForceRef.md)). It is read by the mode-switching logic to decide how the force reference is generated and when the axis exits force mode (see [Force operation mode](00-overview.md)).

## How it works

Each cycle the force-command generator branches on `ForceCmdSrc` to build the raw force reference and to decide when to exit force mode. The supported values are:

| Value | Source |
|----|----|
| 0 | Analog force-reference input (the channel assigned the force-command function via [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md)). The reference follows the analog signal; [ForceCmdHTime](ForceCmdHTime.md)`[1]` sets how long the axis stays in force mode. |
| 1 | User-defined sequence: step through the [ForceCmdVal](ForceCmdVal.md) table, each entry held for [ForceCmdHTime](ForceCmdHTime.md) and reached at rate [ForceCmdSlope](ForceCmdSlope.md). |
| 2 | Same as value 1 in the current firmware. |

> **Note:** In this firmware version, values 1 and 2 behave identically; the interpolated variant is reserved for a future enhancement. Document and configure with `ForceCmdSrc = 1` for the user-defined table.

When `ForceCmdSrc = 0`, the analog reference can be entered/exited automatically by the mode-switch conditions described in [Force operation mode](00-overview.md). When `ForceCmdSrc = 1` or `2`, the axis exits force mode according to the [ForceCmdHTime](ForceCmdHTime.md) table (a `0` entry forces a return to position mode).

## Examples

```text
AForceCmdSrc=0       ; follow the analog force reference input
AForceCmdSrc=1       ; use the user-defined ForceCmdVal table
```

### Edge cases

- **Wrong mode** ([OperationMode](../01-general-keywords/OperationMode.md) ≠ 4) — `ForceCmdSrc` is **not consulted**; writes take effect immediately but the new source only applies once the axis enters force mode.
- **Out of range** — values outside `0`–`2` are rejected by the parameter table.
- **Source 0 with no analog mapping** — if no analog input is mapped to function 4 (force command) via [AInMode](../../05-inputs-outputs/02-analog-inputs/AInMode.md), `ForceRef` reads as `0`.
- **No master-source equivalent** — unlike [CurrCmdSrc](../03-current-operation-mode/CurrCmdSrc.md), force mode does **not** have a master-axis source (no `ForceCmdSrc = 3`).
- **In-target detection** — [ForceInTStat](ForceInTStat.md) is only updated when `ForceCmdSrc = 1` or `2`; with `ForceCmdSrc = 0` there is no defined settling target so `ForceInTStat` stays at the motor-on state.
- **Save** — flash-saveable; reloaded at boot.
- **Motor off** — accepted at any time; the source flag does not require the motor.

## See also

- [ForceCmdVal](ForceCmdVal.md) — user-defined force values (sources 1/2)
- [ForceRef](ForceRef.md) — the resulting force reference
- [Force operation mode](00-overview.md) — overall mode behavior
