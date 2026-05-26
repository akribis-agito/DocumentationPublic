---
keyword: CurrLimMode
summary: Selects how the current command (CurrRef) is saturated.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 392
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
  - 3
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrLimMode

Selects how the current command (CurrRef) is saturated.

## Overview

`CurrLimMode` chooses the source of the current-command (`CurrRef`) saturation limits:

| Value | Limited by | Allowable CurrRef range [mA] |
|-------|------------|------------------------------|
| 0 | [PeakCL](PeakCL.md) (absolute value) | [−PeakCL, PeakCL] |
| 1 | Two analog inputs | [−AInPort[q], AInPort[p]] |
| 2 | One analog input | [−AInPort[p], AInPort[p]] |
| 3 | [CurrLimFwd](CurrLimFwd.md), [CurrLimRev](CurrLimRev.md) | [−CurrLimRev, CurrLimFwd] |

- **Mode 1:** the positive limit comes from the analog input `p` where [AInMode](../../05-inputs-outputs/02-analog-inputs/AInMode.md)`[p] = 8` (positive current limit); the negative limit from input `q` where `AInMode[q] = 7` (negative current limit).
- **Mode 2:** both limits come from the single analog input `p` where `AInMode[p] = 8`.

## Examples

```text
CurrLimMode=3       ; use CurrLimFwd / CurrLimRev as the limits
```

## See also

- [CurrLimFwd](CurrLimFwd.md) / [CurrLimRev](CurrLimRev.md) — limits used in mode 3
- [PeakCL](PeakCL.md) — limit used in mode 0
