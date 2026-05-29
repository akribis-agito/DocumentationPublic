---
keyword: FrcUnitGrp
summary: Read-only list of the keywords that belong to the force unit group.
availability:
  standalone: []
  central-i:
  - v5
can_code: 811
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 9
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
# FrcUnitGrp

Read-only list of the keywords that belong to the force unit group.

## Overview

`FrcUnitGrp` reports which keywords make up the **force** unit group of the global engineering-units feature. These are the force-related keywords whose values are reinterpreted together when the force engineering unit is changed through [FrcUnitFct](FrcUnitFct.md) and [FrcUnitUnt](FrcUnitUnt.md). The list is fixed by the firmware; reading it lets you confirm exactly which keywords a force-unit change affects.

This keyword is available from central-i v5 only.

## How it works

`FrcUnitGrp` is a read-only, non-axis array. The firmware fills it with the identities of the force-group member keywords; each element identifies one member keyword. The array is 1-indexed: element [1] is the first member and element [0] is reserved and not used.

The force group contains the following keywords:

| Index | Member keyword |
|---|---|
| 1 | ForceCmdVal |
| 2 | ForceRef |
| 3 | Force |
| 4 | ForceErr |
| 5 | MaxForceErr |
| 6 | ForceAInTh |
| 7 | ForceInTTol |
| 8 | MaxForceErrOL |

The highest usable index is one less than the array size.

## Examples

```text
AFrcUnitGrp[1]      ; read the first member of the force unit group
AFrcUnitGrp[3]      ; read the member at index 3
```

## See also

- [00-overview](00-overview.md) — the Group / Factor / Unit model
- [FrcUnitFct](FrcUnitFct.md) — force scale factor
- [FrcUnitUnt](FrcUnitUnt.md) — force unit label
- [UserUnitsEn](UserUnitsEn.md) — master enable
- [PosUnitGrp](PosUnitGrp.md) · [VelUnitGrp](VelUnitGrp.md) · [AccUnitGrp](AccUnitGrp.md) — the other quantity groups
