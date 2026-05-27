---
keyword: ECAMTableNum
summary: Selects the active ECAM cam pattern / look-up table (1-10).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

## How it works

The controller keeps the eight defining parameters for all 10 patterns at all times, but only one is in effect during a move. When ECAM motion starts ([Begin](../04-motion-command/Begin.md)), the controller copies the parameters of the pattern named by `ECAMTableNum` into the active working set and validates them. A [Begin](../04-motion-command/Begin.md) is rejected if, for the selected pattern:

- any of `ECAMStart`, `ECAMStartCyc`, `ECAMEndCyc` or `ECAMEnd` is `0` (a zero index marks the pattern as unused);
- the indices do not satisfy `ECAMStart ≤ ECAMStartCyc < ECAMEndCyc ≤ ECAMEnd`;
- `ECAMGap` is `0`, or `ECAMCycles` is `0`;
- `ECAMMasterIni` is out of its allowed range, the `ECAMMaster` source is invalid, or two consecutive cam-table entries differ by too much.

Because the parameters are latched at start, changing `ECAMTableNum` mid-motion has no effect; it is therefore blocked while the axis is in motion. The current-cycle counter [ECAMCycCount](ECAMCycCount.md) is also indexed per pattern, so each pattern keeps its own cycle count.

## Examples

```text
AECAMTableNum=1      ; select cam pattern 1 (default)
AECAMTableNum       ; read the active cam pattern
```

## See also

- [ECAMStart](ECAMStart.md) / [ECAMEnd](ECAMEnd.md) — pattern bounds for the selected table
- [ECAMGap](ECAMGap.md) — master-value spacing for the selected table
- [Motion mode – Electronic cam (ECAM)](00-overview.md) — ECAM motion overview
