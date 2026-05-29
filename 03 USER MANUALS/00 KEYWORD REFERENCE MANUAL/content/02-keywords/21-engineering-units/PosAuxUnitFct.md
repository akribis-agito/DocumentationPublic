---
keyword: PosAuxUnitFct
summary: Scale factor applied to auxiliary-encoder position values when Global User Units is enabled.
availability:
  standalone: []
  central-i:
  - v5
can_code: 815
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# PosAuxUnitFct

Scale factor applied to auxiliary-encoder position values when Global User Units is enabled.

## Overview

`PosAuxUnitFct` is the per-axis scale factor for the auxiliary-encoder position quantity under the Global User Units feature ([UserUnitsEn](UserUnitsEn.md) = 1). It is the auxiliary-encoder counterpart of the main-feedback [PosUnitFct](PosUnitFct.md): it scales the auxiliary position [AuxPos](../10-motion/01-kinematics-status/AuxPos.md) and the other members of the auxiliary position unit group ([PosAuxUnitGrp](PosAuxUnitGrp.md)) into the engineering unit you want the host to show.

The factor affects only how values are presented to and accepted from the host; the internal control computation is unaffected. The matching textual label is set with [PosAuxUnitUnt](PosAuxUnitUnt.md).

## How it works

`PosAuxUnitFct` is a floating-point factor that relates internal auxiliary position units to the displayed user unit, applied to every keyword listed in [PosAuxUnitGrp](PosAuxUnitGrp.md). The default is `1` (values presented unchanged).

The factor is stored in flash, so it persists across power cycles.

Global User Units and the embedded auxiliary scaling [AuxUsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) are mutually exclusive on the same axis. Use one or the other for the auxiliary feedback; enabling both raises a conflict when an affected keyword is accessed.

This keyword is available from v5 (central-i) only.

## Examples

```text
APosAuxUnitFct=1       ; default — present auxiliary position unchanged
APosAuxUnitFct=0.001   ; present the auxiliary position scaled by 0.001
APosAuxUnitFct[1]      ; read the current auxiliary position factor
```

## See also

- [PosAuxUnitGrp](PosAuxUnitGrp.md) — keywords scaled by this factor
- [PosAuxUnitUnt](PosAuxUnitUnt.md) — unit label for the auxiliary position quantity
- [PosUnitFct](PosUnitFct.md) — main-feedback position scale factor
- [UserUnitsEn](UserUnitsEn.md) — enables the Global User Units feature per axis
- [AuxUsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — embedded auxiliary scaling (mutually exclusive)
