---
keyword: MapErrOffRamp
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 454
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
  - 1
  - 2147483647
  default: 16384
  scaling: 1.0
  implemented: final
overrides: {}
summary: Rate at which the map error offset ramps toward its target.
---
# MapErrOffRamp

Rate at which the map error offset ramps toward its target.

## Overview

`MapErrOffRamp` sets the rate at which [MapErrOffset](MapErrOffset.md) is ramped toward its target value when the map correction changes. Ramping the offset rather than applying it as a step avoids an abrupt position jump in the corrected feedback. A higher value makes the offset converge more quickly. It works alongside [MapErrOnStep](MapErrOnStep.md), which sets the step applied when mapping engages, and [MapType](MapType.md), which enables the mapping.

It is an axis-scoped parameter saved to flash and can be changed at any time, including during motion.

## Examples

```text
MapErrOffRamp=16384 ; default convergence rate
MapErrOffRamp?      ; query the current ramp rate
```

## See also

- [MapErrOffset](MapErrOffset.md) — the offset this keyword ramps
- [MapErrOnStep](MapErrOnStep.md) — step size applied when mapping engages
- [MapType](MapType.md) — enables the error mapping
