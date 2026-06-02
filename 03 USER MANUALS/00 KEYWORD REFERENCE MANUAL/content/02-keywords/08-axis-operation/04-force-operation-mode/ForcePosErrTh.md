---
keyword: ForcePosErrTh
summary: Position-error threshold (condition B) to enter force mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 576
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -327680
  - 327680
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# ForcePosErrTh

Position-error threshold (condition B) to enter force mode.

## Overview

`ForcePosErrTh` is the threshold position error (`PosErr`) value used in the second condition check (condition B) to enter force operation mode. It is evaluated whenever the axis is neither in current operation mode nor already in force operation mode — that is, while in position operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 3) **or** velocity operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 2).

## How it works

Each cycle, while the axis is neither in current mode nor in force mode, the controller compares the position error against this threshold:

| Value | Descriptions                                              |
|-------|-----------------------------------------------------------|
| \< 0  | Second condition is fulfilled if `PosErr` < `ForcePosErrTh`. |
| 0     | Second condition is not fulfilled.                        |
| \> 0  | Second condition is fulfilled if `PosErr` > `ForcePosErrTh`. |

Entry into force operation mode still requires the first condition check ([CurrPosTh](../03-current-operation-mode/CurrPosTh.md) / [CurrPosThDir](../03-current-operation-mode/CurrPosThDir.md), evaluated against the position reference). When both conditions are met, the axis enters force mode via the same graceful hand-off as [GoToForceMode](GoToForceMode.md), and `ForcePosErrTh` is cleared to 0 to avoid undesired future switching; the user must reconfigure its value for the next switch. `ForcePosErrTh` and [ForceAInTh](ForceAInTh.md) act as parallel B-conditions — either one triggering is sufficient. See [Force operation mode](00-overview.md) for the overview.

## Examples

```text
AForcePosErrTh=5000  ; enter force mode when PosErr > 5000
AForcePosErrTh=0     ; disable this condition
```

### Edge cases

- **Current or force mode** — not evaluated while the axis is already in current operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 1) or force operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 4). It is evaluated in both position mode (= 3) and velocity mode (= 2).
- **Zero value** — disables this condition.
- **After trigger** — cleared to `0` on entry to force mode to avoid repeat triggers.
- **Out of range** — values outside ±327680 are rejected.
- **Motor off** — the threshold engine does not run.
- **Save** — not flash-saveable.

## See also

- [Force operation mode](00-overview.md) — full mode-switching conditions
- [ForceAInTh](ForceAInTh.md) — alternative second condition (analog force feedback)
