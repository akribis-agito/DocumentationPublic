---
keyword: VelAuxUnitFct
summary: "Scale factor applied to auxiliary-encoder velocity values when Global User Units is enabled."
availability:
  standalone: []
  central-i:
  - v5
can_code: 821
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
# VelAuxUnitFct

Scale factor applied to auxiliary-encoder velocity values when Global User Units is enabled.

## Overview

`VelAuxUnitFct` is the per-axis scale factor for the auxiliary-encoder velocity quantity under the Global User Units feature ([UserUnitsEn](UserUnitsEn.md) = 1). It is the auxiliary-encoder counterpart of the main-feedback [VelUnitFct](VelUnitFct.md): it scales the auxiliary velocity [AuxVel](../10-motion/01-kinematics-status/AuxVel.md), the member of the auxiliary velocity unit group ([VelAuxUnitGrp](VelAuxUnitGrp.md)), into the engineering unit you want the host to show.

The factor affects only how values are presented to the host; the internal control computation is unaffected. The matching textual label is set with [VelAuxUnitUnt](VelAuxUnitUnt.md).

## How it works

`VelAuxUnitFct` is a floating-point factor that relates internal auxiliary velocity units to the displayed user unit, applied to every keyword listed in [VelAuxUnitGrp](VelAuxUnitGrp.md). The default is `1` (values presented unchanged).

The factor is stored in flash, so it persists across power cycles.

Global User Units and the embedded auxiliary scaling [AuxUsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) are mutually exclusive on the same axis. Use one or the other for the auxiliary feedback; enabling both raises a conflict when an affected keyword is accessed.

This keyword is available from v5 (central-i) only.

## Examples

```text
AVelAuxUnitFct=1       ; default — present auxiliary velocity unchanged
AVelAuxUnitFct=0.001   ; present the auxiliary velocity scaled by 0.001
AVelAuxUnitFct[1]      ; read the current auxiliary velocity factor
```

## See also

- [VelAuxUnitGrp](VelAuxUnitGrp.md) — keywords scaled by this factor
- [VelAuxUnitUnt](VelAuxUnitUnt.md) — unit label for the auxiliary velocity quantity
- [VelUnitFct](VelUnitFct.md) — main-feedback velocity scale factor
- [UserUnitsEn](UserUnitsEn.md) — enables the Global User Units feature per axis
- [AuxUsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — embedded auxiliary scaling (mutually exclusive)
