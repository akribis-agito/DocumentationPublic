---
keyword: VelRef
summary: Velocity-loop reference/input (position-controller output plus velocity reference).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 25
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -1300000000
  - 1300000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range: null
---
# VelRef

Velocity-loop reference/input (position-controller output plus velocity reference).

## Overview

`VelRef` is the velocity-loop reference/input, in main user units per second. It is generally the sum of the position-controller output and the (scaled) velocity reference, and it is the input to the velocity loop.

`VelRef` must not be confused with the velocity reference [dPosRef](dPosRef.md): `dPosRef` is the filtered derivative of the position reference, whereas `VelRef` also includes the position-controller output. The velocity error [VelErr](VelErr.md) is computed from `VelRef`.

Refer to [Control tuning – Velocity control](../../11-control-tuning/04-velocity-control/00-overview.md) (normal control) and [Control tuning – Dual-loop control](../../11-control-tuning/02-dual-loop-control/00-overview.md) (dual-loop control) for its signal path/derivation.

## Examples

```text
AVelRef             ; read the velocity-loop reference
```

## See also

- [dPosRef](dPosRef.md) — velocity reference (a different signal)
- [VelErr](VelErr.md) — velocity error (`VelRef - Vel[1]`)
- [Vel](Vel.md) — feedback velocity array
