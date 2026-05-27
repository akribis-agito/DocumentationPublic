---
keyword: ECAMMaster
summary: Complex CAN code selecting the master-variable source for each ECAM cam pattern.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 309
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: false
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
# ECAMMaster

Complex CAN code selecting the master-variable source for each ECAM cam pattern.

## Overview

`ECAMMaster` is the [complex CAN code](../../../01-keyword-usage-and-syntax/complex-can-code.md) (CCC) defining the source of the master variable in ECAM motion. It is an array of 10 cam patterns, one element per pattern. As the master value changes, the axis (slave) position reference tracks the cam pattern stored in [GenData](../../20-arrays/GenData.md), spaced by [ECAMGap](ECAMGap.md).

## Examples

```text
ECAMMaster[1]?      ; read the master-variable CCC for cam pattern 1
```

## See also

- [ECAMGap](ECAMGap.md) — spacing of master values
- [ECAMMasterIni](ECAMMasterIni.md) — initial master-value offset at start of motion
- [GenData](../../20-arrays/GenData.md) — array storing the cam pattern
