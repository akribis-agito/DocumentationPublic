---
keyword: VelUnitGrp
summary: Read-only list of the keywords that belong to the velocity unit group.
availability:
  standalone: []
  central-i:
  - v5
can_code: 805
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 17
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1023
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VelUnitGrp

Read-only list of the keywords that belong to the velocity unit group.

## Overview

`VelUnitGrp` reports which keywords make up the **velocity** unit group of the global engineering-units feature. These are the velocity-related keywords whose values are reinterpreted together when the velocity engineering unit is changed through [VelUnitFct](VelUnitFct.md) and [VelUnitUnt](VelUnitUnt.md). The list is fixed by the firmware; reading it lets you confirm exactly which keywords a velocity-unit change affects.

This keyword is available from central-i v5 only.

## How it works

`VelUnitGrp` is a read-only, non-axis array. The firmware fills it with the identities of the velocity-group member keywords; each element identifies one member keyword. The array is 1-indexed: element [1] is the first member and element [0] is reserved and not used.

The velocity group contains the following keywords:

| Index | Member keyword |
|---|---|
| 1 | Vel |
| 2 | VelErr |
| 3 | VelRef |
| 4 | MaxVel |
| 5 | MaxVelErr |
| 6 | InjectVelAmp |
| 7 | Speed |
| 8 | dPosRef |
| 9 | DualStuckVel |
| 10 | InTargetVelTh |
| 11 | SpeedChgNew |
| 12 | AutoGVelTh |
| 13 | MaxVelErrOL |
| 14 | RetractSpeed |
| 15 | FIFOPosVelOf |
| 16 | StuckVel |

The highest usable index is one less than the array size.

## Examples

```text
AVelUnitGrp[1]      ; read the first member of the velocity unit group
AVelUnitGrp[7]      ; read the member at index 7
```

## See also

- [00-overview](00-overview.md) — the Group / Factor / Unit model
- [VelUnitFct](VelUnitFct.md) — velocity scale factor
- [VelUnitUnt](VelUnitUnt.md) — velocity unit label
- [UserUnitsEn](UserUnitsEn.md) — master enable
- [PosUnitGrp](PosUnitGrp.md) · [AccUnitGrp](AccUnitGrp.md) · [FrcUnitGrp](FrcUnitGrp.md) — the other quantity groups
