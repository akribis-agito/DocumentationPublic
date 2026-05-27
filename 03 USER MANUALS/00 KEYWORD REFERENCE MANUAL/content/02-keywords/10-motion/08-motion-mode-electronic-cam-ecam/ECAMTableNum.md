---
keyword: ECAMTableNum
summary: Selects the active ECAM cam pattern / look-up table (1-10).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 311
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 1
  - 10
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ECAMTableNum

Selects the active ECAM cam pattern / look-up table (1-10).

## Overview

`ECAMTableNum` selects which of the up-to-10 cam patterns (look-up tables) is active. Each cam pattern has its own set of parameters that fully define it — [ECAMStart](ECAMStart.md), [ECAMEnd](ECAMEnd.md), [ECAMStartCyc](ECAMStartCyc.md), [ECAMEndCyc](ECAMEndCyc.md), [ECAMGap](ECAMGap.md), [ECAMCycles](ECAMCycles.md), [ECAMMaster](ECAMMaster.md) and [ECAMMasterIni](ECAMMasterIni.md) — held as element-per-pattern arrays. The pattern can be changed only when the axis is not in motion.

## Examples

```text
AECAMTableNum=1      ; select cam pattern 1 (default)
AECAMTableNum       ; read the active cam pattern
```

## See also

- [ECAMStart](ECAMStart.md) / [ECAMEnd](ECAMEnd.md) — pattern bounds for the selected table
- [ECAMGap](ECAMGap.md) — master-value spacing for the selected table
- [Motion mode – Electronic cam (ECAM)](00-overview.md) — ECAM motion overview
