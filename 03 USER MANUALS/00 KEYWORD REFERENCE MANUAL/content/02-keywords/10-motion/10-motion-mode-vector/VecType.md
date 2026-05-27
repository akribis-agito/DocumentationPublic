---
keyword: VecType
summary: Selects the vector motion geometry (0 = linear, 1 = arc).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 630
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecType

Selects the vector motion geometry (0 = linear, 1 = arc).

## Overview

`VecType` defines whether the requested vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16) is linear (`VecType = 0`) or an arc (`VecType = 1`). It selects the geometry of the coordinated path; when arc is chosen, the move is further described by [VecArcCenter](VecArcCenter.md), [VecArcDir](VecArcDir.md) and [VecNumCircles](VecNumCircles.md). It is saved to flash and cannot be modified while in motion.

> **Note:** A combined arc (main motion) plus linear (other axes) mode, `VecType = 2`, is identified as a near-future need but is outside the current range (0-1).

## Examples

```text
VecType=0           ; linear vector (default)
VecType=1           ; arc vector
```

## See also

- [VecArcCenter](VecArcCenter.md) — arc center / radius (arc type)
- [VecArcDir](VecArcDir.md) — arc sweep direction (arc type)
- [VecMemberAxes](VecMemberAxes.md) — axes forming the vector
