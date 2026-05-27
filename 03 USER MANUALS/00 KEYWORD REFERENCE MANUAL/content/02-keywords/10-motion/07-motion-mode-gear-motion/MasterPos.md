---
keyword: MasterPos
summary: Accumulated, scaled position of the gear-motion master variable.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 44
attributes:
  access: ro
  scope: axis
  flash: false
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
# MasterPos

Accumulated, scaled position of the gear-motion master variable.

## Overview

`MasterPos` tracks the change of the master variable (selected by [GearMaster](GearMaster.md)) after scaling, by accumulating the scaled delta each controller cycle. The accumulation runs regardless of the motion state or motion mode. The scaling uses the gear ratio [MasterFact](MasterFact.md) / [MasterFactDen](MasterFactDen.md), and modulo wrap-around of the master variable is handled via [MasterModRev](MasterModRev.md).

## How it works

$$
\mathrm{\Delta}_{MasterPos} = \frac{MasterFact}{MasterFactDen} \bullet \mathrm{\Delta}_{master\ variable}
$$

## Examples

```text
AMasterPos          ; read the accumulated scaled master position
```

## See also

- [GearMaster](GearMaster.md) — selects the master variable
- [MasterFact](MasterFact.md) / [MasterFactDen](MasterFactDen.md) — gear ratio numerator / denominator
- [MasterModRev](MasterModRev.md) — modulo divisor for correct accumulation
