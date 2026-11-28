---
keyword: RecTrigVal
summary: Comparison value used in trigger activation logic for each trigger.
availability:
- controller
- ci-master
can_code: 246
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 7
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0.0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    data_type: float64
  agc300-et:
    array_size: 4
  agd200-et-2d01:
    array_size: 4
  agd200-et-2d02:
    array_size: 4
  agd200-et-2d05:
    array_size: 4
  agd200-et-2d05-71:
    array_size: 4
  agd155-af-2a06:
    array_size: 4
  agd155-af-2a10:
    array_size: 4
  agd155-ec:
    array_size: 4
  agd155-ec-var34:
    array_size: 4
  agd155-ec-var34-3:
    array_size: 4
  agd156-ec:
    array_size: 4
  agd101-ec-34a:
    array_size: 4
  agd101-ec-17a:
    array_size: 4
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# RecTrigVal

Comparison value used in trigger activation logic for each trigger.

## Overview

`RecTrigVal` stores the comparison value used in the trigger activation logic selected by [RecTrigTyp](RecTrigTyp.md). For range types it is the lower bound, paired with [RecTrigValMax](RecTrigValMax.md) as the upper bound. The value is compared against the masked trigger source value. Each index refers to a different trigger.

| Index | Scope no. | Trigger |
|---|---|---|
| 1 | 1 (First) | 1 |
| 2 | 1 (First) | 2 |
| 3 | 1 (First) | 3 |
| 4 | 2 (Second) | 1 |
| 5 | 2 (Second) | 2 |
| 6 | 2 (Second) | 3 |

Please refer to [RecTrigTyp](RecTrigTyp.md) on how the comparison value is used.

When the trigger source ([RecTrigSrc](RecTrigSrc.md)) is a variable that is expressed in user units, the comparison value is interpreted in those same user units: at [RecStart](RecStart.md) the threshold is converted from user units to the controller's internal units before it is compared with the source. The same conversion is applied to [RecTrigValMax](RecTrigValMax.md). For sources that have no user-unit scaling, the value is compared directly.

> **Note:** In v4 the comparison value is a 32-bit integer. In v5 (Central-i) it is a 64-bit floating-point value, so non-integer thresholds can be specified directly.

## Examples

```text
ARecTrigVal[1]=1000  ; comparison value for trigger 1 of the first scope
ARecTrigVal[1]      ; query the comparison value of trigger 1 (first scope)
```

## See also

- [RecTrigTyp](RecTrigTyp.md) — trigger activation type
- [RecTrigValMax](RecTrigValMax.md) — range upper bound
- [RecTrigSrc](RecTrigSrc.md) — trigger source variable
- [RecTrigMask](RecTrigMask.md) — bitwise mask on the values
