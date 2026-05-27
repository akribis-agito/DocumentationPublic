---
keyword: PDUsrUnits
summary: Counts-per-user-unit scale for converting PDPos and PDVel to user units on query.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`PDUsrUnits` scales the internal pulse-and-direction variables [PDPos](PDPos.md) and [PDVel](PDVel.md) from the controller's internal counts to user units when these statuses are queried over a communication channel. It parallels the feedback-side [UsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) but applies only to the P/D status group. It affects the reported value only, not the internal control computation. The default `65536` is a scale of one count per user unit.

## How it works

Like `UsrUnits`, `PDUsrUnits` is a **16.16 fixed-point ratio**: the effective scale is `PDUsrUnits / 65536` counts per user unit (the fixed scaling base is 65536, i.e. a 16-bit shift). When a P/D status is read the controller divides the internal count value by this ratio:

$$
\text{Queried PDPos [user units]} = \frac{\text{Controller PDPos [counts]}}{\big(PDUsrUnits / 65536\big)} = \text{counts} \times \frac{65536}{PDUsrUnits}
$$

The conversion is selected per-keyword by the controller's unit-scaling logic for the P/D status group. When `PDUsrUnits` is an exact multiple of 65536 the controller takes the fast integer path (shift instead of divide); otherwise it uses the full fixed-point ratio. The default `65536` means a factor of 1 (values shown directly in counts). Only `PDPos` and `PDVel` belong to the P/D user-units group, so this scaling does not affect any other keyword.

To express "*N* internal counts = 1 user unit", set `PDUsrUnits = N × 65536`.

## Examples

```text
APDUsrUnits=65536    ; 1 count per user unit (default)
APDUsrUnits=327680   ; 5 counts per user unit (ratio 5 = 5 x 65536)
APDUsrUnits         ; read the current scale
```

## See also

- [PDPos](PDPos.md) — scaled P/D counter reported in these user units
- [PDVel](PDVel.md) — P/D velocity reported in these user units
- [UsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — the equivalent ratio for encoder-feedback position
