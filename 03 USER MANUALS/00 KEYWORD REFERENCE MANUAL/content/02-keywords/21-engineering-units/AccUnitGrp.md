---
keyword: AccUnitGrp
summary: Read-only list of the keywords that belong to the acceleration unit group.
availability:
  standalone: []
  central-i:
  - v5
can_code: 808
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 8
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
# AccUnitGrp

Read-only list of the keywords that belong to the acceleration unit group.

## Overview

`AccUnitGrp` reports which keywords make up the **acceleration** unit group of the global engineering-units feature. These are the acceleration-related keywords whose values are reinterpreted together when the acceleration engineering unit is changed through [AccUnitFct](AccUnitFct.md) and [AccUnitUnt](AccUnitUnt.md). The list is fixed by the firmware; reading it lets you confirm exactly which keywords an acceleration-unit change affects.

This keyword is available from central-i v5 only.

## How it works

`AccUnitGrp` is a read-only, non-axis array. The firmware fills it with the identities of the acceleration-group member keywords; each element identifies one member keyword. The array is 1-indexed: element [1] is the first member and element [0] is reserved and not used.

The acceleration group contains the following keywords:

| Index | Member keyword |
|---|---|
| 1 | MaxAcc |
| 2 | Accel |
| 3 | Decel |
| 4 | EmrgDec |
| 5 | AutoGAccTh |
| 6 | JerkInAcc |
| 7 | JerkInDec |

The highest usable index is one less than the array size.

## Examples

```text
AAccUnitGrp[1]      ; read the first member of the acceleration unit group
AAccUnitGrp[3]      ; read the member at index 3
```

## See also

- [00-overview](00-overview.md) — the Group / Factor / Unit model
- [AccUnitFct](AccUnitFct.md) — acceleration scale factor
- [AccUnitUnt](AccUnitUnt.md) — acceleration unit label
- [UserUnitsEn](UserUnitsEn.md) — master enable
- [PosUnitGrp](PosUnitGrp.md) · [VelUnitGrp](VelUnitGrp.md) · [FrcUnitGrp](FrcUnitGrp.md) — the other quantity groups
