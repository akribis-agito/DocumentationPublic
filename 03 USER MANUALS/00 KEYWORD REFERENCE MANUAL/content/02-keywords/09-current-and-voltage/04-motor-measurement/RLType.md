---
keyword: RLType
summary: Selects whether PCSuite R/L measurements are reported as phase (0) or line-to-line (1) data.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 375
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# RLType

Selects whether PCSuite R/L measurements are reported as phase (0) or line-to-line (1) data.

## Overview

`RLType` defines the type of measurement made by PCSuite's resistance-and-inductance measurement tool. It determines how the measured [Rm](Rm.md) and [Lm](Lm.md) values are interpreted (phase versus line-to-line).

## How it works

| RLType | Measurement type  |
|--------|-------------------|
| 0      | Phase data        |
| 1      | Line-to-line data |

## Examples

```text
ARLType=1            ; report line-to-line data (default)
ARLType=0            ; report phase data
```

## See also

- [Rm](Rm.md) — measured motor resistance
- [Lm](Lm.md) — measured motor inductance
