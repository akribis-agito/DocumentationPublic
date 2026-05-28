---
keyword: RecTrigTyp
summary: Trigger activation logic (edge, comparison, or range) for each trigger.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 245
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
  - 0
  - 12
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecTrigTyp

Trigger activation logic (edge, comparison, or range) for each trigger.

## Overview

`RecTrigTyp` defines how each trigger is activated (the trigger type). It selects the comparison applied between the trigger source value ([RecTrigSrc](RecTrigSrc.md), subject to masking by [RecTrigMask](RecTrigMask.md)) and the comparison values [RecTrigVal](RecTrigVal.md) and [RecTrigValMax](RecTrigValMax.md). Each index refers to a different trigger.

| Index | Scope no. | Trigger |
|---|---|---|
| 1 | 1 (First) | 1 |
| 2 | 1 (First) | 2 |
| 3 | 1 (First) | 3 |
| 4 | 2 (Second) | 1 |
| 5 | 2 (Second) | 2 |
| 6 | 2 (Second) | 3 |

## How it works

Each `RecTrigTyp` value selects a different trigger activation logic. The trigger source value originates from the variable pointed to by [RecTrigSrc](RecTrigSrc.md), subject to masking.

| Value | Trigger activation logic |
|----|----|
| 0 | Immediate trigger (no trigger source needed) |
| 1 | Activated when the source value is more than RecTrigVal |
| 2 | Activated when the source value equals RecTrigVal |
| 3 | Activated when the source value is not equal to RecTrigVal |
| 4 | Activated when the source value is less than RecTrigVal |
| 5 | Activated upon the rising edge of source value beyond RecTrigVal. |
| 6 | Activated upon the falling edge of source value below RecTrigVal. |
| 7 | Manual trigger only (activated solely by [RecTrigForce](RecTrigForce.md); no trigger source needed) |
| 8 | Activated when the source value is different from its value at the start of recording |
| 9 | Activated when the source value is within the range of (RecTrigVal, RecTrigValMax) |
| 10 | Activated when the source value is not within the range of (RecTrigVal, RecTrigValMax) |
| 11 | Activated upon the entry of source value into the range of (RecTrigVal, RecTrigValMax) |
| 12 | Activated upon the exit of source value out of the range of (RecTrigVal, RecTrigValMax) |

## Examples

```text
ARecTrigTyp[2]=5     ; trigger 2 (first scope) on rising edge above RecTrigVal
ARecTrigTyp[1]      ; query the activation type of trigger 1 (first scope)
```

> **Note:** `RecTrigTyp[2] = 0`, `RecTrigTyp[3] = 0`, `RecTrigsLogic[1] = 1`, `RecTrigsLogic[2] = 1` and `RecTrigsMode[1] = 1` are normally commanded to achieve a single-trigger setting for the first scope. Similar commands can be made for the second scope.

## See also

- [RecTrigSrc](RecTrigSrc.md) — trigger source variable
- [RecTrigVal](RecTrigVal.md) — comparison value
- [RecTrigValMax](RecTrigValMax.md) — range upper bound (types 9–12)
- [RecTrigMask](RecTrigMask.md) — bitwise mask on the source value
