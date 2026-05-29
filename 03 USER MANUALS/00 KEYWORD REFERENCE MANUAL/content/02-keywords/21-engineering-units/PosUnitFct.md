---
keyword: PosUnitFct
summary: Scale factor between internal position units and the selected position engineering unit.
availability:
  standalone: []
  central-i:
  - v5
can_code: 803
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
# PosUnitFct

Scale factor between internal position units and the selected position engineering unit.

## Overview

`PosUnitFct` holds the floating-point scale factor that relates the controller's internal position units to the engineering unit you want to work in for the **position** quantity. The single factor applies to every keyword in the position unit group (see [PosUnitGrp](PosUnitGrp.md)), and the engineering unit it represents is labelled by [PosUnitUnt](PosUnitUnt.md). The factor takes effect as part of the global engineering-units feature, which is switched on per axis with [UserUnitsEn](UserUnitsEn.md).

This keyword is available from central-i v5 only.

## How it works

`PosUnitFct` is a per-axis, double-precision factor stored in flash. Its default value is `1`, which represents no rescaling relative to the controller's internal position units. Set it to relate the internal position unit to the engineering unit you label with [PosUnitUnt](PosUnitUnt.md), so that the whole position group is presented consistently.

A single factor covers the whole position group, so position, position error, references, targets, limits, and the other members listed by [PosUnitGrp](PosUnitGrp.md) all share the same conversion.

> Note: the firmware stores this factor as the configuration for the position engineering unit; the application of the factor to displayed/accepted values is handled by the global engineering-units feature together with [UserUnitsEn](UserUnitsEn.md). The exact conversion direction and rounding are governed by the host/units layer rather than by an internal control-loop rescaling — the control loop continues to run in internal units regardless of this setting.

## Examples

```text
APosUnitFct[1]=1.0        ; default — no rescaling of the position group
APosUnitFct[1]=0.001      ; example factor for the position group
APosUnitFct[1]            ; read the current position factor
```

## See also

- [00-overview](00-overview.md) — the Group / Factor / Unit model
- [PosUnitGrp](PosUnitGrp.md) — keywords this factor applies to
- [PosUnitUnt](PosUnitUnt.md) — position unit label
- [UserUnitsEn](UserUnitsEn.md) — master enable
- [VelUnitFct](VelUnitFct.md) · [AccUnitFct](AccUnitFct.md) · [FrcUnitFct](FrcUnitFct.md) — the other quantity factors
