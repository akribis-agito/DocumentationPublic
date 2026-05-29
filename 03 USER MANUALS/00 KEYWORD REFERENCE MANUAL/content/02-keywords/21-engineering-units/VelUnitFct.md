---
keyword: VelUnitFct
summary: "Scale factor between internal velocity units and the selected velocity engineering unit."
availability:
  standalone: []
  central-i:
  - v5
can_code: 806
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
# VelUnitFct

Scale factor between internal velocity units and the selected velocity engineering unit.

## Overview

`VelUnitFct` holds the floating-point scale factor that relates the controller's internal velocity units to the engineering unit you want to work in for the **velocity** quantity. The single factor applies to every keyword in the velocity unit group (see [VelUnitGrp](VelUnitGrp.md)), and the engineering unit it represents is labelled by [VelUnitUnt](VelUnitUnt.md). The factor takes effect as part of the global engineering-units feature, which is switched on per axis with [UserUnitsEn](UserUnitsEn.md).

This keyword is available from central-i v5 only.

## How it works

`VelUnitFct` is a per-axis, double-precision factor stored in flash. Its default value is `1`, which represents no rescaling relative to the controller's internal velocity units. Set it to relate the internal velocity unit to the engineering unit you label with [VelUnitUnt](VelUnitUnt.md), so that the whole velocity group is presented consistently.

A single factor covers the whole velocity group, so velocity, velocity error, references, thresholds, and the other members listed by [VelUnitGrp](VelUnitGrp.md) all share the same conversion.

> Note: the firmware stores this factor as the configuration for the velocity engineering unit; the application of the factor to displayed/accepted values is handled by the global engineering-units feature together with [UserUnitsEn](UserUnitsEn.md). The control loop continues to run in internal units regardless of this setting.

## Examples

```text
AVelUnitFct[1]=1.0        ; default — no rescaling of the velocity group
AVelUnitFct[1]=0.001      ; example factor for the velocity group
AVelUnitFct[1]            ; read the current velocity factor
```

## See also

- [00-overview](00-overview.md) — the Group / Factor / Unit model
- [VelUnitGrp](VelUnitGrp.md) — keywords this factor applies to
- [VelUnitUnt](VelUnitUnt.md) — velocity unit label
- [UserUnitsEn](UserUnitsEn.md) — master enable
- [PosUnitFct](PosUnitFct.md) · [AccUnitFct](AccUnitFct.md) · [FrcUnitFct](FrcUnitFct.md) — the other quantity factors
