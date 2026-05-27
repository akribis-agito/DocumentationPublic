---
keyword: OpenLoopCurr
summary: Current reference applied to the current loop in current open-loop mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 145
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# OpenLoopCurr

Current reference applied to the current loop in current open-loop mode.

## Overview

`OpenLoopCurr` is the current reference, in milliamperes, applied onto the current loop while the axis is in the current open-loop condition. It is only used when [OpenLoopOn](OpenLoopOn.md) = 1.

This value bypasses all current references contributed by position, velocity or force control, except for cogging compensation ([UPMVelTable](../../../02-keywords/09-current-and-voltage/03-current-compensation/UPMVelTable.md)) and DC offset ([CurrRefOffset](../../../02-keywords/09-current-and-voltage/03-current-compensation/CurrRefOffset.md)). It is applied on a per-individual-motor basis, which means the decoupling matrix is not used (for example, excitation is not applied across a gantry axis).

## Examples

```text
OpenLoopOn=1        ; enter current open loop
OpenLoopCurr=1000   ; apply 1000 mA current reference
```

## See also

- [OpenLoopOn](OpenLoopOn.md) — selects the open-loop point (1 = current open loop)
- [OpenLoopVolt](OpenLoopVolt.md) — voltage reference for voltage open loop
