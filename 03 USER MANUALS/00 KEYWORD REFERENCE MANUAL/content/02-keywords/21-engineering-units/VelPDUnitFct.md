---
keyword: VelPDUnitFct
summary: "Scale factor applied to pulse-and-direction velocity values when Global User Units is enabled."
availability:
  standalone: []
  central-i:
  - v5
can_code: 824
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
# VelPDUnitFct

Scale factor applied to pulse-and-direction velocity values when Global User Units is enabled.

## Overview

`VelPDUnitFct` is the per-axis scale factor for the pulse-and-direction (P/D) velocity quantity under the Global User Units feature ([UserUnitsEn](UserUnitsEn.md) = 1). It is the P/D counterpart of the main-feedback [VelUnitFct](VelUnitFct.md): it scales the P/D velocity [PDVel](../10-motion/06-motion-mode-pulse-and-direction-pd/PDVel.md), the member of the P/D velocity unit group ([VelPDUnitGrp](VelPDUnitGrp.md)), into the engineering unit you want the host to show.

The factor affects only how values are presented to the host; the internal control computation is unaffected. The matching textual label is set with [VelPDUnitUnt](VelPDUnitUnt.md).

## How it works

`VelPDUnitFct` is a floating-point factor that relates internal P/D velocity units to the displayed user unit, applied to every keyword listed in [VelPDUnitGrp](VelPDUnitGrp.md). The default is `1` (values presented unchanged).

The factor is stored in flash, so it persists across power cycles.

Global User Units and the embedded P/D scaling [PDUsrUnits](../10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md) are mutually exclusive on the same axis. Use one or the other for the P/D feedback; enabling both raises a conflict when an affected keyword is accessed.

This keyword is available from v5 (central-i) only.

## Examples

```text
AVelPDUnitFct=1       ; default — present P/D velocity unchanged
AVelPDUnitFct=0.01    ; present the P/D velocity scaled by 0.01
AVelPDUnitFct[1]      ; read the current P/D velocity factor
```

## See also

- [VelPDUnitGrp](VelPDUnitGrp.md) — keywords scaled by this factor
- [VelPDUnitUnt](VelPDUnitUnt.md) — unit label for the P/D velocity quantity
- [VelUnitFct](VelUnitFct.md) — main-feedback velocity scale factor
- [UserUnitsEn](UserUnitsEn.md) — enables the Global User Units feature per axis
- [PDUsrUnits](../10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md) — embedded P/D scaling (mutually exclusive)
