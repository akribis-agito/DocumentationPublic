---
keyword: PosPDUnitFct
summary: Scale factor applied to pulse-and-direction position values when Global User Units is enabled.
availability:
  standalone: []
  central-i:
  - v5
can_code: 818
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
# PosPDUnitFct

Scale factor applied to pulse-and-direction position values when Global User Units is enabled.

## Overview

`PosPDUnitFct` is the per-axis scale factor for the pulse-and-direction (P/D) position quantity under the Global User Units feature ([UserUnitsEn](UserUnitsEn.md) = 1). It is the P/D counterpart of the main-feedback [PosUnitFct](PosUnitFct.md): it scales the P/D position counter [PDPos](../10-motion/06-motion-mode-pulse-and-direction-pd/PDPos.md) and the other members of the P/D position unit group ([PosPDUnitGrp](PosPDUnitGrp.md)) into the engineering unit you want the host to show.

The factor affects only how values are presented to and accepted from the host; the internal control computation is unaffected. The matching textual label is set with [PosPDUnitUnt](PosPDUnitUnt.md).

## How it works

`PosPDUnitFct` is a floating-point factor that relates internal P/D position units to the displayed user unit, applied to every keyword listed in [PosPDUnitGrp](PosPDUnitGrp.md). The default is `1` (values presented unchanged).

The factor is stored in flash, so it persists across power cycles.

Global User Units and the embedded P/D scaling [PDUsrUnits](../10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md) are mutually exclusive on the same axis. Use one or the other for the P/D position; enabling both raises a conflict when an affected keyword is accessed.

This keyword is available from v5 (central-i) only.

## Examples

```text
APosPDUnitFct=1       ; default — present P/D position unchanged
APosPDUnitFct=0.01    ; present the P/D position scaled by 0.01
APosPDUnitFct[1]      ; read the current P/D position factor
```

## See also

- [PosPDUnitGrp](PosPDUnitGrp.md) — keywords scaled by this factor
- [PosPDUnitUnt](PosPDUnitUnt.md) — unit label for the P/D position quantity
- [PosUnitFct](PosUnitFct.md) — main-feedback position scale factor
- [UserUnitsEn](UserUnitsEn.md) — enables the Global User Units feature per axis
- [PDUsrUnits](../10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md) — embedded P/D scaling (mutually exclusive)
