---
keyword: ForceInTTol
summary: Settling window around the target force used for in-target status.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 734
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
  - 0
  - 2147483647
  default: 10
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceInTTol

Settling window around the target force used for in-target status.

## Overview

`ForceInTTol` is the settling window around the target value ([ForceCmdVal](ForceCmdVal.md)), in units, used to determine the in-target status of force control. It is applicable only when [ForceCmdSrc](ForceCmdSrc.md) = 1 or 2. Together with the dwell time [ForceInTTime](ForceInTTime.md), it determines when [ForceInTStat](ForceInTStat.md) reports settled.

## Examples

```text
AForceInTTol=10      ; settled when force error stays within ±10 units
```

## See also

- [ForceInTTime](ForceInTTime.md) — required dwell time within this window
- [ForceInTStat](ForceInTStat.md) — in-target status using this window
- [ForceErr](ForceErr.md) — error compared against this window
