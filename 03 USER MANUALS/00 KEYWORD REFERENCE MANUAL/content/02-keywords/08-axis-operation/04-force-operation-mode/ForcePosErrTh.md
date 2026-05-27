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
---
# ForcePosErrTh

Position-error threshold (condition B) to enter force mode.

## Overview

`ForcePosErrTh` is the threshold position error (`PosErr`) value used in the second condition check (condition B) to enter force operation mode. It is used only while the axis is in position operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 3).

## How it works

| Value | Descriptions                                              |
|-------|-----------------------------------------------------------|
| \< 0  | Second condition is fulfilled if `PosErr` < `ForcePosErrTh`. |
| 0     | Second condition is not fulfilled.                        |
| \> 0  | Second condition is fulfilled if `PosErr` > `ForcePosErrTh`. |

Entry into force operation mode still requires the first condition check ([CurrPosTh](../03-current-operation-mode/CurrPosTh.md) / [CurrPosThDir](../03-current-operation-mode/CurrPosThDir.md)). When both conditions are met, the axis enters force mode and `ForcePosErrTh` is cleared to 0 to avoid undesired future switching; the user must reconfigure its value for the next switch. See [Force operation mode](00-overview.md) for the overview.

## Examples

```text
AForcePosErrTh=5000  ; enter force mode when PosErr > 5000
AForcePosErrTh=0     ; disable this condition
```

## See also

- [Force operation mode](00-overview.md) — full mode-switching conditions
- [ForceAInTh](ForceAInTh.md) — alternative second condition (analog force feedback)
