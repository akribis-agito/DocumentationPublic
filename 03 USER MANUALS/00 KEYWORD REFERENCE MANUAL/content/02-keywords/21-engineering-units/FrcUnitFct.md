---
keyword: FrcUnitFct
summary: Scale factor between internal force units and the selected force engineering unit.
availability:
  standalone: []
  central-i:
  - v5
can_code: 812
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
# FrcUnitFct

Scale factor between internal force units and the selected force engineering unit.

## Overview

`FrcUnitFct` holds the floating-point scale factor that relates the controller's internal force units to the engineering unit you want to work in for the **force** quantity. The single factor applies to every keyword in the force unit group (see [FrcUnitGrp](FrcUnitGrp.md)), and the engineering unit it represents is labelled by [FrcUnitUnt](FrcUnitUnt.md). The factor takes effect as part of the global engineering-units feature, which is switched on per axis with [UserUnitsEn](UserUnitsEn.md).

This keyword is available from central-i v5 only.

## How it works

`FrcUnitFct` is a per-axis, double-precision factor stored in flash. Its default value is `1`, which represents no rescaling relative to the controller's internal force units. Set it to relate the internal force unit to the engineering unit you label with [FrcUnitUnt](FrcUnitUnt.md), so that the whole force group is presented consistently.

A single factor covers the whole force group, so the force command, reference, feedback, error, and the other members listed by [FrcUnitGrp](FrcUnitGrp.md) all share the same conversion.

> Note: the firmware stores this factor as the configuration for the force engineering unit; the application of the factor to displayed/accepted values is handled by the global engineering-units feature together with [UserUnitsEn](UserUnitsEn.md). The control loop continues to run in internal units regardless of this setting.

## Examples

```text
AFrcUnitFct[1]=1.0        ; default — no rescaling of the force group
AFrcUnitFct[1]=0.001      ; example factor for the force group
AFrcUnitFct[1]            ; read the current force factor
```

## See also

- [00-overview](00-overview.md) — the Group / Factor / Unit model
- [FrcUnitGrp](FrcUnitGrp.md) — keywords this factor applies to
- [FrcUnitUnt](FrcUnitUnt.md) — force unit label
- [UserUnitsEn](UserUnitsEn.md) — master enable
- [PosUnitFct](PosUnitFct.md) · [VelUnitFct](VelUnitFct.md) · [AccUnitFct](AccUnitFct.md) — the other quantity factors
