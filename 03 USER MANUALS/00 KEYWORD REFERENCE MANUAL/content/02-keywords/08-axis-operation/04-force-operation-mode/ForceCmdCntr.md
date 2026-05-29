---
keyword: ForceCmdCntr
summary: Time elapsed in force mode or in the active ForceCmdVal entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 574
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
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceCmdCntr

Time elapsed in force mode or in the active ForceCmdVal entry.

## Overview

`ForceCmdCntr` is the time elapsed, in milliseconds, that drives the timing-table logic of force operation mode. Its meaning depends on [ForceCmdSrc](ForceCmdSrc.md):

1. If `ForceCmdSrc` = 0 (analog input): time elapsed under force operation mode.
2. If `ForceCmdSrc` = 1 or 2 (user-defined table): time elapsed under the existing [ForceCmdVal](ForceCmdVal.md) array entry. This resets to 0 when switching to the next `ForceCmdVal` entry.

`ForceCmdCntr` resets to 0 upon receipt of the [GoToForceMode](GoToForceMode.md) command, upon automatic condition switching, or upon a digital input switching to force operation mode. This means that when [OperationMode](../01-general-keywords/OperationMode.md) is assigned directly, the user can preset it to any initial value and start the timer from there.

> **Note:** The user can overwrite `ForceCmdCntr` at any time while in force operation mode.

## How it works

`ForceCmdCntr` is incremented once per control cycle while the raw force reference is holding at its target (for both the table source and the analog source) and is compared against [ForceCmdHTime](ForceCmdHTime.md) to decide when to advance the table entry or exit force mode. It is **held at 0 while the reference is still ramping** to the target, so it measures hold time only, not ramp time. The internal counter is clamped at 2,000,000,000 to prevent roll-over.

When the table index advances to a new entry the counter is cleared to 0; on the **last** entry it is left running so the user can read how long the axis has been holding the final value.

## Examples

```text
AForceCmdCntr       ; read elapsed time (ms)
AForceCmdCntr=0      ; restart the timer
```

### Edge cases

- **Wrong mode** ([OperationMode](../01-general-keywords/OperationMode.md) ≠ 4) — not advanced.
- **Sources 1/2 during ramp** — held at `0` while [ForceCmdSlope](ForceCmdSlope.md) is ramping; only starts counting once `ForceRef = ForceCmdVal[index]`.
- **Saturation** — clamped at `2 000 000 000` to avoid roll-over.
- **Clamped index (20)** — counter is left running, not reset.
- **Manual write** — allowed while in force mode; can restart a hold or short-circuit a long hold.
- **GoToForceMode** — resets the counter to `0`; direct `OperationMode = 4` does not.
- **Save** — not flash-saveable.

## See also

- [ForceCmdHTime](ForceCmdHTime.md) — holding time compared against this counter
- [ForceCmdIndex](ForceCmdIndex.md) — active table entry
- [GoToForceMode](GoToForceMode.md) — resets this counter on entry
