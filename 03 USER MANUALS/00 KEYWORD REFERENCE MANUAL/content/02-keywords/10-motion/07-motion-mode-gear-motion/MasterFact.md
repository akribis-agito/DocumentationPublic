---
keyword: MasterFact
summary: Numerator of the gear ratio applied to the master-variable delta.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 120
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
  - -16777215
  - 16777215
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
---
# MasterFact

Numerator of the gear ratio applied to the master-variable delta.

## Overview

`MasterFact` is the numerator of the scaling ratio applied to the delta of the master variable in gear motion. Together with the denominator [MasterFactDen](MasterFactDen.md) it forms the gear ratio that maps a change in the master variable to a change in the slave's profiler position reference (direct gear motion, [MotionMode](../02-motion-configuration/MotionMode.md) `= 5`) or target position [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) (indirect gear motion, `MotionMode = 6`). The scaled delta is accumulated into [MasterPos](MasterPos.md).

## How it works

$$
\mathrm{\Delta}_{ProfilerPosRef/AbsTrgt} = \mathrm{\Delta}_{MasterPos} = \frac{MasterFact}{MasterFactDen} \bullet \mathrm{\Delta}_{master\ variable}\ 
$$

## Examples

```text
MasterFact=65536    ; default numerator (1:1 ratio with default denominator)
MasterFact?         ; read current value
```

## See also

- [MasterFactDen](MasterFactDen.md) — denominator of the gear ratio
- [MasterPos](MasterPos.md) — accumulated, scaled master position
- [GearMaster](GearMaster.md) — selects the master variable
- [MotionMode](../02-motion-configuration/MotionMode.md) — selects direct (`= 5`) or indirect (`= 6`) gear motion
