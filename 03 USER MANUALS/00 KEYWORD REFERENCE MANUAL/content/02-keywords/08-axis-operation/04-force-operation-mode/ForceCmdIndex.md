---
keyword: ForceCmdIndex
summary: Index of the active ForceCmdVal / ForceCmdHTime table entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 573
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 20
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceCmdIndex

Index of the active ForceCmdVal / ForceCmdHTime table entry.

## Overview

`ForceCmdIndex` is the index of the [ForceCmdVal](ForceCmdVal.md) and [ForceCmdHTime](ForceCmdHTime.md) values currently in use. It is applicable only when [ForceCmdSrc](ForceCmdSrc.md) = 1 or 2 (user-defined table).

`ForceCmdIndex` resets to 1 upon receipt of the [GoToForceMode](GoToForceMode.md) command, upon automatic condition switching, or upon a digital input switching to force operation mode. This means that when [OperationMode](../01-general-keywords/OperationMode.md) is assigned directly, the user can preset it so the reference table starts from the desired `ForceCmdVal`/`ForceCmdHTime` pair.

> **Note:** The user can overwrite `ForceCmdIndex` at any time while in force operation mode. This causes an immediate switch of the `ForceCmdVal` in use, without resetting the [ForceCmdCntr](ForceCmdCntr.md) timer.

## How it works

The generator auto-increments `ForceCmdIndex` when the current entry's hold time elapses. It is clamped to the last usable entry (20): if it would advance past the end of the array it is held there, so the axis stays on the final [ForceCmdVal](ForceCmdVal.md) rather than wrapping. When advancing to a new entry the holding timer [ForceCmdCntr](ForceCmdCntr.md) is cleared so the next entry's [ForceCmdHTime](ForceCmdHTime.md) is timed from zero.

The reset to `1` on graceful entry is performed by [GoToForceMode](GoToForceMode.md) and by the automatic / digital-input switch paths.

## Examples

```text
AForceCmdIndex      ; read the active table entry
AForceCmdIndex=3     ; jump to the third entry
```

### Edge cases

- **Wrong mode** ([OperationMode](../01-general-keywords/OperationMode.md) ≠ 4 or [ForceCmdSrc](ForceCmdSrc.md) ∉ {1, 2}) — `ForceCmdIndex` is **not consulted**.
- **Out of range** — values outside `1`–`20` are rejected.
- **Mid-ramp write** — overwriting the index switches to the new target on the next cycle without resetting [ForceCmdCntr](ForceCmdCntr.md).
- **GoToForceMode** — always resets `ForceCmdIndex = 1`; direct `OperationMode = 4` does not.
- **End of table** — clamped at `20`; the firmware does not reset the counter when clamped.
- **Save** — not flash-saveable.

## See also

- [ForceCmdVal](ForceCmdVal.md) — table of force values
- [ForceCmdHTime](ForceCmdHTime.md) — holding times per entry
- [ForceCmdCntr](ForceCmdCntr.md) — timer for the active entry
