---
keyword: ForceInTStat
summary: In-target status of force control for the user-defined reference table.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 735
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 4
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceInTStat

In-target status of force control for the user-defined reference table.

## Overview

`ForceInTStat` reports the in-target status of force control when a user-defined force reference array is used. It is applicable only when [ForceCmdSrc](ForceCmdSrc.md) = 1 or 2, and it tracks progress from motor enable through ramping to settling within [ForceInTTol](ForceInTTol.md) for at least [ForceInTTime](ForceInTTime.md).

## How it works

| ForceInTStat | Descriptions |
|----|----|
| 0 | Motor is disabled. |
| 1 | Motor is enabled. |
| 2 | Force reference is changing/ramping to the target value ([ForceCmdVal](ForceCmdVal.md)). |
| 3 | Force reference has reached the target value while force feedback is settling to within the [ForceInTTol](ForceInTTol.md) window around the target value for at least [ForceInTTime](ForceInTTime.md). |
| 4 | Force feedback has settled to within `ForceInTTol` of the target value for at least `ForceInTTime`. |

## Examples

```text
ForceInTStat?       ; 4 = settled in target, 2 = still ramping
```

## See also

- [ForceInTTol](ForceInTTol.md) — settling window
- [ForceInTTime](ForceInTTime.md) — required dwell time within the window
- [ForceSamples](ForceSamples.md) — measured move/settle timings
