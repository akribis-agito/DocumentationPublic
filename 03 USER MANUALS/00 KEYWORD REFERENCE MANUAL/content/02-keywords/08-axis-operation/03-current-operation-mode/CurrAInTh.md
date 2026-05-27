---
keyword: CurrAInTh
summary: Analog force-feedback threshold (condition B) to enter current mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 338
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
  - -100000
  - 100000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# CurrAInTh

Analog force-feedback threshold (condition B) to enter current mode.

## Overview

`CurrAInTh` is the threshold analog force-feedback value used in the second condition check (condition B) to enter current operation mode. It is used only while the axis is in velocity or position operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 2 or 3). The analog force feedback is configured via [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md) and read from `AInPort`.

## How it works

| Value | Descriptions |
|----|----|
| \< 0 | Second condition is fulfilled if analog force feedback < `CurrAInTh`. |
| 0 | Second condition is not fulfilled. |
| \> 0 | Second condition is fulfilled if analog force feedback > `CurrAInTh`. |

This check is **only evaluated if an analog input is actually configured as force feedback**: the controller first verifies that an analog input is assigned the force-feedback function (via [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md)), and reads the filtered value of that input. If no input is assigned that function, `CurrAInTh` has no effect regardless of its value.

`CurrAInTh` is one of three interchangeable condition-B checks (the others being [CurrPosErrTh](CurrPosErrTh.md) and [CurrCurrTh](CurrCurrTh.md)); any one of them satisfying its comparison triggers the switch, provided condition A has already passed.

Entry into current operation mode still requires the first condition check ([CurrPosTh](CurrPosTh.md) / [CurrPosThDir](CurrPosThDir.md)). When both the first and second conditions are met, the axis enters current operation mode and the firmware clears `CurrAInTh` to 0 (and clears [CurrPosThDir](CurrPosThDir.md)) to avoid undesired future switching; the user must reconfigure its value for the next switch. See [Current operation mode](00-overview.md) for the full switching logic.

## Examples

```text
ACurrAInTh=5000      ; enter current mode when force feedback > 5000
ACurrAInTh=0         ; disable this condition
```

## See also

- [Current operation mode](00-overview.md) — full mode-switching conditions
- [CurrPosTh](CurrPosTh.md) — first condition (position reference threshold)
- [CurrPosErrTh](CurrPosErrTh.md) — alternative second condition (position error)
- [CurrCurrTh](CurrCurrTh.md) — alternative second condition (current reference)
