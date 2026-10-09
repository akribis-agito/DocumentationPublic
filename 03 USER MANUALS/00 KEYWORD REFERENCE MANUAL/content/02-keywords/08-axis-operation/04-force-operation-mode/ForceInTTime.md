---
keyword: ForceInTTime
summary: Minimum dwell time within the settling window before force control is settled.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 733
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 163840
  default: null
  scaling: 65.536
  implemented: final
overrides: {}
last_updated: '2026-10-10'
doc_revision: '2026.06'
---
# ForceInTTime

> **AGM800-EC** — This keyword remains in milliseconds. AGM800-EC converts at **16 samples/ms** (62.5 µs per sample), with integer rounding where required. The 16.384 samples/ms calculations below apply to the legacy 16,384 Hz configuration. Product-dependent raw sample limits and defaults must be read from the controller metadata. See [AGM800-EC timing and units](../../01-system/03-timing/AGM800-EC-units.md).

Minimum dwell time within the settling window before force control is settled.

## Overview

`ForceInTTime` defines the minimum time, in milliseconds, that the force error ([ForceErr](ForceErr.md)) must continuously stay within the settling window ([ForceInTTol](ForceInTTol.md)) before the axis is considered settled in [ForceInTStat](ForceInTStat.md). It is applicable in Force Operation Mode when [ForceCmdSrc](ForceCmdSrc.md) = 1 or 2, and in Current Operation Mode ([OperationMode](../01-general-keywords/OperationMode.md) = 1) when [CurrCmdSrc](../03-current-operation-mode/CurrCmdSrc.md) = 1 or 2, where the error is `CurrRef − MotorCurr`.

## How it works

The internal dwell counter is active only while [ForceInTStat](ForceInTStat.md) = 3. Each cycle the controller tests `|ForceErr| <= ForceInTTol`; if true it increments the counter, otherwise it re-zeroes it. Once the counter reaches `ForceInTTime` the axis is considered settled (`ForceInTStat` = 4) and the settling condition is no longer checked for that command entry.

A value of `0` means the axis is declared settled as soon as `ForceErr` first enters the window (no dwell required).

## Examples

```text
AForceInTTime=50     ; require 50 ms within the settling window
```

### Edge cases

- **Wrong mode / source** — only used when [OperationMode](../01-general-keywords/OperationMode.md) = 4 and [ForceCmdSrc](ForceCmdSrc.md) ∈ {1, 2}, or OperationMode = 1 and [CurrCmdSrc](../03-current-operation-mode/CurrCmdSrc.md) ∈ {1, 2}; ignored otherwise.
- **Zero value** — settling latches as soon as the error enters [ForceInTTol](ForceInTTol.md) for one cycle (dwell of zero).
- **Tolerance excursion** — leaving the window during the dwell re-zeros the dwell counter; the dwell must accumulate consecutively.
- **Out of range** — values outside `0`–`163840` are rejected.
- **Save** — flash-saveable.

## See also

- [ForceInTTol](ForceInTTol.md) — the settling window
- [ForceInTStat](ForceInTStat.md) — in-target status driven by this timer
- [ForceErr](ForceErr.md) — error checked against the window
