---
summary: Denominator of the gear ratio applied to the master-variable delta.
keyword: MasterFactDen
availability:
  standalone: []
  central-i:
  - v5
can_code: 632
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
  - 1
  - 16777215
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
---
# MasterFactDen

Denominator of the gear ratio applied to the master-variable delta.

## Overview

`MasterFactDen` is the denominator of the scaling ratio applied to the delta of the master variable in gear motion. Together with the numerator [MasterFact](MasterFact.md) it forms the gear ratio that maps a change in the master variable to a change in the slave's profiler position reference (direct gear motion, [MotionMode](../02-motion-configuration/MotionMode.md) `= 5`) or target position [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) (indirect gear motion, `MotionMode = 6`). The scaled delta is accumulated into [MasterPos](MasterPos.md).

## How it works

$$
\mathrm{\Delta}_{ProfilerPosRef/AbsTrgt} = \mathrm{\Delta}_{MasterPos} = \frac{MasterFact}{MasterFactDen} \bullet \mathrm{\Delta}_{master\ variable}\ 
$$

## Examples

```text
AMasterFactDen      ; read the gear-ratio denominator
```

## See also

- [MasterFact](MasterFact.md) — numerator of the gear ratio
- [MasterPos](MasterPos.md) — accumulated, scaled master position
- [GearMaster](GearMaster.md) — selects the master variable
