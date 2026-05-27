---
keyword: CurrPosTh
summary: Position-reference threshold (condition A) to enter current mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# CurrPosTh

Position-reference threshold (condition A) to enter current mode.

## Overview

`CurrPosTh` is the threshold position reference (`PosRef`) value used in the first condition check (condition A) to enter current operation mode. It is used only while the axis is in velocity or position operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 2 or 3). The comparison direction is set by [CurrPosThDir](CurrPosThDir.md), and the comparison is made against the *commanded* position reference `PosRef`, not the actual feedback position.

## How it works

Condition A is a **gate**: the firmware evaluates it first each cycle, and only if it passes does it go on to evaluate the condition-B thresholds. The direction keyword [CurrPosThDir](CurrPosThDir.md) decides the comparison (and `0` makes condition A always pass, i.e. it disables the position gate):

| CurrPosThDir | Descriptions                                         |
|--------------|------------------------------------------------------|
| \< 0         | First condition is fulfilled if `PosRef` < `CurrPosTh`. |
| 0            | First condition is fulfilled (unconditionally).       |
| \> 0         | First condition is fulfilled if `PosRef` > `CurrPosTh`. |

Entry into current operation mode still requires the second condition check (one of [CurrPosErrTh](CurrPosErrTh.md), [CurrAInTh](CurrAInTh.md) or [CurrCurrTh](CurrCurrTh.md)) to be satisfied in the same cycle. When both conditions are met, the axis enters current mode and the firmware clears [CurrPosThDir](CurrPosThDir.md) to 0 (which makes the position gate pass unconditionally) and clears the condition-B threshold that triggered the switch. `CurrPosTh` itself keeps its value; to fully re-arm the same position gate for a later switch, set `CurrPosThDir` and a condition-B threshold again. See [Current operation mode](00-overview.md) for the overview.

## Examples

```text
ACurrPosThDir=1      ; first condition triggers when PosRef > CurrPosTh
ACurrPosTh=100000    ; position-reference threshold (user units)
```

## See also

- [CurrPosThDir](CurrPosThDir.md) — selects the comparison direction
- [Current operation mode](00-overview.md) — full mode-switching conditions
