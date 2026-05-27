---
keyword: RecTrigValMax
summary: Upper bound for range-based trigger activation logic (RecTrigTyp 9–12).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 293
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
# RecTrigValMax

Upper bound for range-based trigger activation logic (RecTrigTyp 9–12).

## Overview

`RecTrigValMax` stores the maximum (upper-bound) value for range-based trigger activation logic. It is only applicable when the corresponding [RecTrigTyp](RecTrigTyp.md) is range-related (`9`, `10`, `11`, or `12`), pairing with [RecTrigVal](RecTrigVal.md) as the lower bound. Each index refers to a different trigger.

| Index | Scope no. | Trigger |
|---|---|---|
| 1 | 1 (First) | 1 |
| 2 | 1 (First) | 2 |
| 3 | 1 (First) | 3 |
| 4 | 2 (Second) | 1 |
| 5 | 2 (Second) | 2 |
| 6 | 2 (Second) | 3 |

Please refer to [RecTrigTyp](RecTrigTyp.md) on how the maximum value is used.

## Examples

```text
RecTrigValMax[1]=2000   ; range upper bound for trigger 1 of the first scope
RecTrigValMax[1]?       ; query the upper bound of trigger 1 (first scope)
```

## See also

- [RecTrigTyp](RecTrigTyp.md) — trigger activation type (range types 9–12)
- [RecTrigVal](RecTrigVal.md) — range lower bound
- [RecTrigSrc](RecTrigSrc.md) — trigger source variable
