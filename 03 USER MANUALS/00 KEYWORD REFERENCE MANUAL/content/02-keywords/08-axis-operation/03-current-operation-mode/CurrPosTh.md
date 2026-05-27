---
keyword: CurrPosTh
summary: Position-reference threshold (condition A) to enter current mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 426
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrPosTh

Position-reference threshold (condition A) to enter current mode.

## Overview

`CurrPosTh` is the threshold position reference (`PosRef`) value used in the first condition check (condition A) to enter current operation mode. It is used only while the axis is in velocity or position operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 2 or 3). The comparison direction is set by [CurrPosThDir](CurrPosThDir.md).

## How it works

| CurrPosThDir | Descriptions                                         |
|--------------|------------------------------------------------------|
| \< 0         | First condition is fulfilled if `PosRef` < `CurrPosTh`. |
| 0            | First condition is fulfilled (unconditionally).       |
| \> 0         | First condition is fulfilled if `PosRef` > `CurrPosTh`. |

Entry into current operation mode still requires the second condition check (one of [CurrPosErrTh](CurrPosErrTh.md), [CurrAInTh](CurrAInTh.md) or [CurrCurrTh](CurrCurrTh.md)). When both conditions are met, the axis enters current mode and `CurrPosTh` is cleared to 0 to avoid undesired future switching; the user must reconfigure its value for the next switch. See [Current operation mode](00-overview.md) for the overview.

## Examples

```text
ACurrPosThDir=1      ; first condition triggers when PosRef > CurrPosTh
ACurrPosTh=100000    ; position-reference threshold (user units)
```

## See also

- [CurrPosThDir](CurrPosThDir.md) — selects the comparison direction
- [Current operation mode](00-overview.md) — full mode-switching conditions
