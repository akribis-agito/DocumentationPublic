---
keyword: FricVelSrc
summary: Selects the velocity the friction models use (0 = dPosRef, 1 = VelRef, 2 = velocity feedback).
availability:
  standalone: []
  central-i:
  - v5
can_code: 927
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
  - 2
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
---
# FricVelSrc

Selects the velocity the friction models use (0 = dPosRef, 1 = VelRef, 2 = velocity feedback).

## Overview

`FricVelSrc` chooses which velocity drives friction methods 1, 2, 3 and 5. Available on AGM800 and AGM800-EC (central-i v5).

| `FricVelSrc` | Velocity used |
|---|---|
| 0 | Position-reference derivative (dPosRef) from the profiler |
| 1 | Velocity reference ([VelRef](../../02-keywords/10-motion/01-kinematics-status/VelRef.md)) |
| 2 | Velocity feedback (default) |

## How it works

All three sources are in counts/s, so the same band and Stribeck velocities apply whichever you choose. A reference (0 or 1) gives a clean, noise-free signal and switches direction exactly when the command does; the feedback (2) follows what the axis really does.

In velocity mode there is no position reference, so the stage always uses `VelRef` there, whatever `FricVelSrc` says. LuGre (method 4) and quadrant-switching compensation always use the velocity feedback. The viscous term ([FricViscous](FricViscous.md)) always uses the velocity feedback.

## Examples

```text
AFricVelSrc=1      ; drive the friction model from the velocity reference
```

## See also

- [FricMethod](FricMethod.md)
- [Friction feedforward](00-overview.md)
