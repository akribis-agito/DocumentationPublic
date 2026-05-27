---
keyword: RecTrigVal
summary: Comparison value used in trigger activation logic for each trigger.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 246
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 4
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
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
