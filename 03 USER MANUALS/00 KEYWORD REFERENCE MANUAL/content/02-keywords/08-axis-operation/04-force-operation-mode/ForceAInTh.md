---
keyword: ForceAInTh
summary: Analog force-feedback threshold (condition B) to enter force mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 584
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
overrides: {}
---
# ForceAInTh

Analog force-feedback threshold (condition B) to enter force mode.

## Overview

`ForceAInTh` is the threshold analog force-feedback value used in the second condition check (condition B) to enter force operation mode. It is used only while the axis is in velocity or position operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 2 or 3).

## How it works

| Value | Descriptions |
|----|----|
| \< 0 | Second condition is fulfilled if analog force feedback < `ForceAInTh`. |
| 0 | Second condition is not fulfilled. |
| \> 0 | Second condition is fulfilled if analog force feedback > `ForceAInTh`. |

Entry into force operation mode still requires the first condition check ([CurrPosTh](../03-current-operation-mode/CurrPosTh.md) / [CurrPosThDir](../03-current-operation-mode/CurrPosThDir.md)). When both conditions are met, the axis enters force mode and `ForceAInTh` is cleared to 0 to avoid undesired future switching; the user must reconfigure its value for the next switch. See [Force operation mode](00-overview.md) for the overview.

## Examples

```text
ForceAInTh=5000     ; enter force mode when force feedback > 5000
ForceAInTh=0        ; disable this condition
```

## See also

- [Force operation mode](00-overview.md) — full mode-switching conditions
- [ForcePosErrTh](ForcePosErrTh.md) — alternative second condition (position error)
- [Force](Force.md) — the force feedback being compared
