---
keyword: RecTrigSrc
summary: Complex CAN code of the trigger source variable for each trigger.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 243
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecTrigSrc

Complex CAN code of the trigger source variable for each trigger.

## Overview

`RecTrigSrc` defines the [complex CAN code](../../01-keyword-usage-and-syntax/complex-can-code.md) of the variable whose value is monitored by each trigger. The trigger compares this source value (after masking by [RecTrigMask](RecTrigMask.md)) against [RecTrigVal](RecTrigVal.md) / [RecTrigValMax](RecTrigValMax.md) according to [RecTrigTyp](RecTrigTyp.md). Each index refers to a different trigger.

| Index | Scope no. | Trigger |
|---|---|---|
| 1 | 1 (First) | 1 |
| 2 | 1 (First) | 2 |
| 3 | 1 (First) | 3 |
| 4 | 2 (Second) | 1 |
| 5 | 2 (Second) | 2 |
| 6 | 2 (Second) | 3 |

It is possible to use the same variable as both a trigger source and a recorded variable at the same time.

## Examples

`RecTrigSrc[4] = 2` means `APos` is used as the trigger source for trigger 1 of the second scope.

## See also

- [RecTrigTyp](RecTrigTyp.md) — trigger activation type
- [RecTrigMask](RecTrigMask.md) — bitwise mask on the source value
- [RecTrigVal](RecTrigVal.md) — comparison value
- [RecParamA/RecParamB](RecParamA-RecParamB.md) — parameters to capture
