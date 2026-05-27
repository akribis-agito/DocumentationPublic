---
keyword: ForceCmdSrc
summary: Selects the source of the force reference in force mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 570
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
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceCmdSrc

Selects the source of the force reference in force mode.

## Overview

`ForceCmdSrc` sets the source of the force reference ([ForceRef](ForceRef.md)). It is read by the mode-switching logic to decide how the force reference is generated and when the axis exits force mode (see [Force operation mode](00-overview.md)).

## How it works

| Value | Source |
|----|----|
| 0 | Analog force reference input (defined by [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md)) |
| 1 or 2 | User-defined values ([ForceCmdVal](ForceCmdVal.md)), each with specific timing ([ForceCmdHTime](ForceCmdHTime.md)) |

## Examples

```text
AForceCmdSrc=0       ; follow the analog force reference input
AForceCmdSrc=1       ; use the user-defined ForceCmdVal table
```

## See also

- [ForceCmdVal](ForceCmdVal.md) — user-defined force values (sources 1/2)
- [ForceRef](ForceRef.md) — the resulting force reference
- [Force operation mode](00-overview.md) — overall mode behavior
