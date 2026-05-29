---
keyword: CurrCmdCntr
summary: Time elapsed in current mode or in the active CurrCmdVal entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 334
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 2000000000
  default: 0
  scaling: 65.536
  implemented: final
overrides: {}
---
# CurrCmdCntr

Time elapsed in current mode or in the active CurrCmdVal entry.

## Overview

`CurrCmdCntr` is the time elapsed, in milliseconds, that drives the timing-table logic of current operation mode. Its meaning depends on [CurrCmdSrc](CurrCmdSrc.md):

1. If `CurrCmdSrc` = 0 or 3 (analog input or slave drive): time elapsed under current operation mode.
2. If `CurrCmdSrc` = 1 or 2 (user-defined table): time elapsed under the existing [CurrCmdVal](CurrCmdVal.md) array entry. This resets to 0 when switching to the next `CurrCmdVal` entry.

`CurrCmdCntr` resets to 0 upon receipt of the [GoToCurrMode](GoToCurrMode.md) command, upon automatic condition switching, or upon a digital input switching to current operation mode. This means that when [OperationMode](../01-general-keywords/OperationMode.md) is assigned directly, the user can preset it to any initial value and start the timer from there.

## How it works

The counter advances by one per control cycle. The exact value of one count in milliseconds therefore follows the control-loop sample time. Its behaviour depends on the source:

- **Sources 0 and 3 (analog / master axis):** the counter starts incrementing immediately on mode entry and is compared against [CurrCmdHTime](CurrCmdHTime.md)`[1]`.
- **Sources 1 and 2 (user table):** while `CurrRef` is ramping toward the active [CurrCmdVal](CurrCmdVal.md) entry the counter is held at 0; it only begins counting once `CurrRef` reaches the entry, and is reset to 0 when the index advances to the next entry. When the table is exhausted and the index is clamped to the last entry, the counter is **not** reset — so it keeps growing and reveals how long the axis has held the final value.

> **Note:** The user can overwrite `CurrCmdCntr` at any time while in current operation mode.

## Examples

```text
ACurrCmdCntr        ; read elapsed time (ms)
ACurrCmdCntr=0       ; restart the timer
```

### Edge cases

- **Wrong mode** ([OperationMode](../01-general-keywords/OperationMode.md) ≠ 1) — the counter is not advanced; the value reflects the last cycle in current mode.
- **Sources 1/2 during ramp** — held at `0` while [CurrCmdSlope](CurrCmdSlope.md) is ramping `CurrRef`; only starts counting once `CurrRef = CurrCmdVal[index]`.
- **Maximum value** — `2 000 000 000` is the largest value a user may *write* to `CurrCmdCntr`; it is not a runtime cap. While in current operation mode the counter simply increments once per control cycle, with no runtime saturation (consistent with the **Clamped index (20)** edge case, where the counter keeps growing at the final entry).
- **Clamped index (20)** — when [CurrCmdIndex](CurrCmdIndex.md) sits at `20`, the counter is **not** reset; it keeps growing.
- **Manual write** — writing `CurrCmdCntr` while in current mode is allowed; useful to restart a hold or to advance to the next entry early.
- **GoToCurrMode** — resets the counter to `0`; direct `OperationMode = 1` does not.
- **Save** — not flash-saveable.

## See also

- [CurrCmdHTime](CurrCmdHTime.md) — holding time compared against this counter
- [CurrCmdIndex](CurrCmdIndex.md) — active table entry
- [GoToCurrMode](GoToCurrMode.md) — resets this counter on entry
