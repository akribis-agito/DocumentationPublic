---
summary: Denominator of the gear ratio applied to the master-variable delta.
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
MasterFactDen?      ; read the gear-ratio denominator
```

## See also

- [MasterFact](MasterFact.md) — numerator of the gear ratio
- [MasterPos](MasterPos.md) — accumulated, scaled master position
- [GearMaster](GearMaster.md) — selects the master variable
