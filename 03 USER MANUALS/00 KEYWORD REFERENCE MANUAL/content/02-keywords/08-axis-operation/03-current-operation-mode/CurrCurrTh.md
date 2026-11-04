---
keyword: CurrCurrTh
summary: Current-reference threshold (condition B) to enter current mode.
availability:
- controller
- ci-master
can_code: 339
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -16000
  - 16000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - -64000
    - 64000
  agc300-et:
    range:
    - -4000
    - 4000
  agc301-et:
    range:
    - -4000
    - 4000
  agc301-et-bioxtreme:
    range:
    - -4000
    - 4000
  agd200-et-2d01:
    range:
    - -4000
    - 4000
  agd200-et-2d02:
    range:
    - -8000
    - 8000
  agd301-et-2d01:
    range:
    - -4000
    - 4000
  agd301-et-2d02:
    range:
    - -8000
    - 8000
  agd301-et-2d09:
    range:
    - -25500
    - 25500
  agd155-af-2a06:
    range:
    - -25500
    - 25500
  agd155-af-2a10:
    range:
    - -28500
    - 28500
  agd155-ec:
    range:
    - -25500
    - 25500
  agd155-ec-var34:
    range:
    - -28500
    - 28500
  agd155-ec-var34-3:
    range:
    - -42500
    - 42500
  agd156-ec:
    range:
    - -12726
    - 12726
  agd101-ec-34a:
    range:
    - -28280
    - 28280
  agd101-ec-17a:
    range:
    - -14140
    - 14140
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# CurrCurrTh

Current-reference threshold (condition B) to enter current mode.

## Overview

`CurrCurrTh` is the threshold value compared against the current *reference* `CurrRef` (the commanded current, not the measured current) in the second condition check (condition B) to enter current operation mode. It is used only while the axis is in velocity or position operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 2 or 3). If the value is 0 the check is disarmed and the axis does not switch on it; otherwise the comparison direction is set by [CurrCurrThDir](CurrCurrThDir.md).

## How it works

| CurrCurrThDir | Descriptions                                            |
|---------------|---------------------------------------------------------|
| 0             | Second condition is fulfilled if `CurrRef` > `CurrCurrTh`. |
| 1             | Second condition is fulfilled if `CurrRef` < `CurrCurrTh`. |

`CurrCurrTh` is one of three interchangeable condition-B checks (with [CurrPosErrTh](CurrPosErrTh.md) and [CurrAInTh](CurrAInTh.md)); the firmware switches if any armed check is satisfied, provided condition A has already passed.

Entry into current operation mode still requires the first condition check ([CurrPosTh](CurrPosTh.md) / [CurrPosThDir](CurrPosThDir.md)). When both conditions are met, the axis enters current mode and the firmware clears `CurrCurrTh` to 0 (and clears [CurrPosThDir](CurrPosThDir.md)) to avoid undesired future switching; the user must reconfigure its value for the next switch. See [Current operation mode](00-overview.md) for the overview.

## Examples

```text
ACurrCurrThDir=0     ; trigger when CurrRef rises above threshold
ACurrCurrTh=2000     ; enter current mode when CurrRef > 2000 mA
```

### Edge cases

- **Wrong mode** ([OperationMode](../01-general-keywords/OperationMode.md) ∉ {2, 3}) — not evaluated.
- **Zero value** — disables this condition.
- **After trigger** — both `CurrCurrTh` and [CurrPosThDir](CurrPosThDir.md) are cleared to `0`; the user must re-arm both for the next switch.
- **Direction** — comparison sense set by [CurrCurrThDir](CurrCurrThDir.md); `0` defaults to a rising-edge crossing.
- **Motor off** — the threshold engine does not run.
- **Save** — not flash-saveable; the value is lost on power cycle and must be re-armed.

## See also

- [CurrCurrThDir](CurrCurrThDir.md) — selects the comparison direction
- [Current operation mode](00-overview.md) — full mode-switching conditions
- [CurrPosTh](CurrPosTh.md) — first condition (position reference threshold)
