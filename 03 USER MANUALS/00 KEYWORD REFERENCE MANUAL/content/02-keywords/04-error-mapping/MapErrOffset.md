---
keyword: MapErrOffset
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 411
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
summary: Current position-error offset applied on top of the map correction.
---
# MapErrOffset

Current position-error offset applied on top of the map correction.

## Overview

`MapErrOffset` holds a position-error offset that is added to the map correction. When the active correction changes (for example as error mapping is engaged), the offset is ramped toward its target rather than applied as a step; `MapErrOffset` reflects the value currently in effect during that transition. The convergence behaviour is governed by [MapErrOffRamp](MapErrOffRamp.md) (ramp rate) and [MapErrOnStep](MapErrOnStep.md) (step size when applied on engagement). The underlying mapping is enabled by [MapType](MapType.md).

It is an axis-scoped parameter, not saved to flash, and cannot be changed while the axis is in motion or the motor is on.

## Examples

```text
MapErrOffset?       ; read the offset currently applied to the map correction
MapErrOffset=0      ; clear the applied offset
```

## See also

- [MapErrOffRamp](MapErrOffRamp.md) — rate at which this offset converges
- [MapErrOnStep](MapErrOnStep.md) — step size applied when mapping engages
- [MapType](MapType.md) — enables the error mapping this offset modifies
