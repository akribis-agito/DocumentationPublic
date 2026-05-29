---
keyword: AccUnitFct
summary: Scale factor between internal acceleration units and the selected acceleration engineering unit.
availability:
  standalone: []
  central-i:
  - v5
can_code: 809
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
# AccUnitFct

Scale factor between internal acceleration units and the selected acceleration engineering unit.

## Overview

`AccUnitFct` holds the floating-point scale factor that relates the controller's internal acceleration units to the engineering unit you want to work in for the **acceleration** quantity. The single factor applies to every keyword in the acceleration unit group (see [AccUnitGrp](AccUnitGrp.md)), and the engineering unit it represents is labelled by [AccUnitUnt](AccUnitUnt.md). The factor takes effect as part of the global engineering-units feature, which is switched on per axis with [UserUnitsEn](UserUnitsEn.md).

This keyword is available from central-i v5 only.

## How it works

`AccUnitFct` is a per-axis, double-precision factor stored in flash. Its default value is `1`, which represents no rescaling relative to the controller's internal acceleration units. Set it to relate the internal acceleration unit to the engineering unit you label with [AccUnitUnt](AccUnitUnt.md), so that the whole acceleration group is presented consistently.

A single factor covers the whole acceleration group, so the acceleration limit, accel/decel rates, jerk-related members, and the other keywords listed by [AccUnitGrp](AccUnitGrp.md) all share the same conversion.

> Note: the firmware stores this factor as the configuration for the acceleration engineering unit; the application of the factor to displayed/accepted values is handled by the global engineering-units feature together with [UserUnitsEn](UserUnitsEn.md). The control loop continues to run in internal units regardless of this setting.

## Examples

```text
AAccUnitFct[1]=1.0        ; default — no rescaling of the acceleration group
AAccUnitFct[1]=0.001      ; example factor for the acceleration group
AAccUnitFct[1]            ; read the current acceleration factor
```

## See also

- [00-overview](00-overview.md) — the Group / Factor / Unit model
- [AccUnitGrp](AccUnitGrp.md) — keywords this factor applies to
- [AccUnitUnt](AccUnitUnt.md) — acceleration unit label
- [UserUnitsEn](UserUnitsEn.md) — master enable
- [PosUnitFct](PosUnitFct.md) · [VelUnitFct](VelUnitFct.md) · [FrcUnitFct](FrcUnitFct.md) — the other quantity factors
