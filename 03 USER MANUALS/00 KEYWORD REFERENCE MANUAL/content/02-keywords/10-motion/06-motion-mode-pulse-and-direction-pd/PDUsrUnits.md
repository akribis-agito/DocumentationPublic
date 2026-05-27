---
keyword: PDUsrUnits
summary: Counts-per-user-unit scale for converting PDPos and PDVel to user units on query.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 66
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 1
  - 2147483647
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDUsrUnits

Counts-per-user-unit scale for converting PDPos and PDVel to user units on query.

## Overview

`PDUsrUnits` scales the internal pulse-and-direction variables [PDPos](PDPos.md) and [PDVel](PDVel.md) from the controller's internal counts to user units when the user queries these statuses over a communication channel. It only affects the reported (queried) value, not the internal control computation. The default value `65536` represents a scale of one count per user unit.

## How it works

For example:

$$
Queried\ PDPos\ \lbrack user\ units\rbrack = \frac{1}{\frac{PDUsrUnits}{65536}\left\lbrack \frac{counts}{user\ units} \right\rbrack\ } \bullet \ Controller\ PDPos\ \lbrack counts\rbrack\ 
$$

## Examples

```text
PDUsrUnits=65536    ; 1 count per user unit (default)
PDUsrUnits?         ; read the current scale
```

## See also

- [PDPos](PDPos.md) — scaled P/D counter reported in these user units
- [PDVel](PDVel.md) — P/D velocity reported in these user units
