---
keyword: CurrCurrTh
summary: Current-reference threshold (condition B) to enter current mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 339
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
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
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

## See also

- [CurrCurrThDir](CurrCurrThDir.md) — selects the comparison direction
- [Current operation mode](00-overview.md) — full mode-switching conditions
- [CurrPosTh](CurrPosTh.md) — first condition (position reference threshold)
