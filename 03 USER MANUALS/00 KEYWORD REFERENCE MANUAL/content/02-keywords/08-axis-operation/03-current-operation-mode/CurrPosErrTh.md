---
keyword: CurrPosErrTh
summary: Position-error threshold (condition B) to enter current mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 337
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
---
# CurrPosErrTh

Position-error threshold (condition B) to enter current mode.

## Overview

`CurrPosErrTh` is the threshold position error (`PosErr`) value used in the second condition check (condition B) to enter current operation mode. It is used only while the axis is in position operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 3).

## How it works

| Value | Descriptions                                             |
|-------|----------------------------------------------------------|
| \< 0  | Second condition is fulfilled if `PosErr` < `CurrPosErrTh`. |
| 0     | Second condition is not fulfilled.                       |
| \> 0  | Second condition is fulfilled if `PosErr` > `CurrPosErrTh`. |

Entry into current operation mode still requires the first condition check ([CurrPosTh](CurrPosTh.md) / [CurrPosThDir](CurrPosThDir.md)). When both conditions are met, the axis enters current mode and `CurrPosErrTh` is cleared to 0 to avoid undesired future switching; the user must reconfigure its value for the next switch. See [Current operation mode](00-overview.md) for the overview.

## Examples

```text
ACurrPosErrTh=5000   ; enter current mode when PosErr > 5000
ACurrPosErrTh=0      ; disable this condition
```

## See also

- [Current operation mode](00-overview.md) — full mode-switching conditions
- [CurrAInTh](CurrAInTh.md) — alternative second condition (analog force feedback)
- [CurrCurrTh](CurrCurrTh.md) — alternative second condition (current reference)
