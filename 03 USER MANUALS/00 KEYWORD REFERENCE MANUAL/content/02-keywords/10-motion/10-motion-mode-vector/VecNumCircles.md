---
keyword: VecNumCircles
summary: Number of full circular arcs to run in vector arc mode (0 = run until StopVec).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 646
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
  - 100
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecNumCircles

Number of full circular arcs to run in vector arc mode (0 = run until StopVec).

## Overview

`VecNumCircles` sets the number of complete circular arcs to execute in vector arc motion ([VecType](VecType.md) = 1). Setting it to zero causes the arc to run indefinitely until a [StopVec](StopVec.md) command is issued, which is useful for continuous circular machining. It works together with [VecArcCenter](VecArcCenter.md) and [VecArcDir](VecArcDir.md), which define the arc geometry and direction. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

## Examples

```text
VecNumCircles=0     ; run continuously until StopVec (default)
VecNumCircles=5     ; execute five full circles, then stop
```

## See also

- [VecType](VecType.md) — selects arc vector motion
- [VecArcCenter](VecArcCenter.md) / [VecArcDir](VecArcDir.md) — arc geometry and direction
- [StopVec](StopVec.md) — stops a continuous arc
