---
keyword: CurrCurrThDir
summary: Trigger direction for the CurrCurrTh current-reference check.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 343
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrCurrThDir

Trigger direction for the CurrCurrTh current-reference check.

## Overview

`CurrCurrThDir` defines the trigger direction for the second condition check (current reference, `CurrRef`) used to enter current operation mode, together with the threshold [CurrCurrTh](CurrCurrTh.md). It is used only while the axis is in velocity or position operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 2 or 3).

## How it works

| CurrCurrThDir | Descriptions                                            |
|---------------|---------------------------------------------------------|
| 0             | Second condition is fulfilled if `CurrRef` > `CurrCurrTh`. |
| 1             | Second condition is fulfilled if `CurrRef` < `CurrCurrTh`. |

The direction only has an effect when [CurrCurrTh](CurrCurrTh.md) is non-zero (a `CurrCurrTh` of 0 disarms the check entirely). Unlike [CurrPosThDir](CurrPosThDir.md), this keyword is **not** cleared by the firmware when the switch triggers — only `CurrCurrTh` and `CurrPosThDir` are zeroed — so the chosen direction persists for the next time you re-arm the threshold.

## Examples

```text
ACurrCurrThDir=1     ; trigger when CurrRef falls below CurrCurrTh
ACurrCurrTh=-2000    ; threshold (mA)
```

### Edge cases

- **Wrong mode** — not evaluated outside [OperationMode](../01-general-keywords/OperationMode.md) 2 / 3.
- **Out of range** — values outside `0`–`1` are rejected.
- **Save** — flash-saveable.

## See also

- [CurrCurrTh](CurrCurrTh.md) — the current-reference threshold
- [Current operation mode](00-overview.md) — full mode-switching conditions
