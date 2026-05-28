---
keyword: RecTrigMask
summary: Bitwise mask applied to trigger source and comparison values.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 251
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
  default: null
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# RecTrigMask

Bitwise mask applied to trigger source and comparison values.

## Overview

`RecTrigMask` masks the bits of the values used in the trigger comparison operation. The trigger source value (from [RecTrigSrc](RecTrigSrc.md)) and the trigger comparison values ([RecTrigVal](RecTrigVal.md) and [RecTrigValMax](RecTrigValMax.md)) are all masked before comparison. This lets a trigger activate based on single or multiple selected bits of a status word. Each index of `RecTrigMask` refers to a different trigger of a different scope.

## How it works

| Index | Scope no. | Trigger |
|---|---|---|
| 1 | 1 (First) | 1 |
| 2 | 1 (First) | 2 |
| 3 | 1 (First) | 3 |
| 4 | 2 (Second) | 1 |
| 5 | 2 (Second) | 2 |
| 6 | 2 (Second) | 3 |

Masking is only applicable if the trigger source ([RecTrigSrc](RecTrigSrc.md)) is of a fixed-point data type (32-bit int or 64-bit long). By default, the `RecTrigMask` value is -1 (all bits set), where no bits are masked and the trigger comparison uses the unaltered values. The masking is done using a bitwise AND operation.

> **Note:** In v4 the mask is a 32-bit integer. In v5 (Central-i) it is a 64-bit integer, allowing all bits of a 64-bit trigger source to be masked.

$$
Masked\ value\  = (Original\ value)\ \&\ \left( RecTrigMask\lbrack x\rbrack \right)
$$

## Examples

Assuming the second trigger of the first scope is to be activated upon the rising edge of the acceleration bit of axis A `MotionStat`, the following settings are required:

1.  RecTrigTyp\[2\] = 5 (rising edge)

2.  RecTrigSrc\[2\] = 32 (AMotionStat as the trigger source variable)

3.  RecTrigMask\[2\] = 16 (masking bit 4)

4.  RecTrigVal\[2\] = 0 (to trigger when rising edge above this value is detected)

## See also

- [RecTrigSrc](RecTrigSrc.md) — trigger source variable
- [RecTrigVal](RecTrigVal.md) — comparison value
- [RecTrigValMax](RecTrigValMax.md) — range upper bound
- [RecTrigTyp](RecTrigTyp.md) — trigger activation type
