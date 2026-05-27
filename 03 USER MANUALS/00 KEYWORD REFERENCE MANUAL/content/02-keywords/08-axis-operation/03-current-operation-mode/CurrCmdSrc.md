---
keyword: CurrCmdSrc
summary: Selects the source of the current reference in current mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 330
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
overrides:
  central-i.v5:
    range:
    - 0
    - 3
---
# CurrCmdSrc

Selects the source of the current reference in current mode.

## Overview

Under current operation mode, `CurrCmdSrc` sets the source of the current command (`CurrRef`). Each control-loop cycle the firmware reads `CurrCmdSrc` in a `switch` statement and generates the current reference accordingly; the same value also governs how and when the axis automatically exits current mode back to position mode (see [Current operation mode](00-overview.md)). `CurrCmdSrc` is only consulted while the axis is actually in current mode ([OperationMode](../01-general-keywords/OperationMode.md) = 1).

## How it works

The controller generates the current reference according to the value as follows:

| Value | Source | Generation mechanism |
|----|----|----|
| 0 | Analog current command input | `CurrRef` is set directly from the filtered analog input configured as the current command (see [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md)). The axis stays in current mode for [CurrCmdHTime](CurrCmdHTime.md)`[1]` (or indefinitely if it is negative). |
| 1 | User-defined table | `CurrRef` steps through the [CurrCmdVal](CurrCmdVal.md) table, ramping toward each entry at [CurrCmdSlope](CurrCmdSlope.md) and holding it for [CurrCmdHTime](CurrCmdHTime.md), advancing via [CurrCmdIndex](CurrCmdIndex.md). |
| 2 | User-defined table (interpolated) | Same handling as value 1 in current firmware — interpolated handling is reserved for a future release. |
| 3 | Master axis current command | `CurrRef` is copied from the master axis' `CurrRef` (master selected by [CurrRefMaster](CurrRefMaster.md)). Timed by [CurrCmdHTime](CurrCmdHTime.md)`[1]` exactly like the analog source. **central-i v5 only.** |

Any unexpected value forces `CurrRef` to 0.

> **Note:** Values 1 and 2 currently behave identically. Value 3 (master-axis slave drive) exists only in the central-i v5 firmware; the standalone/v4 firmware accepts `CurrCmdSrc` of 0–2 only.

## Examples

```text
ACurrCmdSrc=1        ; use the user-defined CurrCmdVal table
ACurrCmdSrc=3        ; follow a master axis (slave drive, central-i v5)
```

## Changes between versions

central-i v5 adds source value 3 (master-axis current command), extending the valid range to 0–3 (standalone/v4: 0–2). Source 3 makes the axis a slave drive that copies the master axis' current reference; see [CurrRefMaster](CurrRefMaster.md).

## See also

- [CurrCmdVal](CurrCmdVal.md) — user-defined current values (sources 1/2)
- [CurrRefMaster](CurrRefMaster.md) — master axis index (source 3)
- [CurrCmdHTime](CurrCmdHTime.md) — timing that determines when the axis exits current mode
- [Current operation mode](00-overview.md) — overall mode behavior
