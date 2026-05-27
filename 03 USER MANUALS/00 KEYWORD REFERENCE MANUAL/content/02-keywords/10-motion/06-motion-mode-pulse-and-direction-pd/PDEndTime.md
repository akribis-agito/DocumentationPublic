---
keyword: PDEndTime
summary: Settling-check delay (ms) after PDPos and the position reference stop changing.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 414
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 163840
  default: 16
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDEndTime

Settling-check delay (ms) after PDPos and the position reference stop changing.

## Overview

`PDEndTime` is the waiting time, in milliseconds, that must elapse after the pulse-direction counter [PDPos](PDPos.md) and the generated position reference stop changing, before the controller begins checking the settling status [InTargetStat](../05-motion-status/InTargetStat.md). Because both direct and indirect pulse-and-direction motion stay in the moving state as long as commands keep arriving, this delay prevents premature in-target reporting when a stream of pulses pauses briefly. It applies to both direct ([MotionMode](../02-motion-configuration/MotionMode.md) = 3) and indirect (`MotionMode` = 4) P/D motion.

## How it works

The `PDEndTime` timer resets whenever `PDPos` or the generated position reference starts changing again. Only after the input and reference have been stationary for the full `PDEndTime` does in-target checking begin.

## Examples

```text
PDEndTime=16        ; wait 16 ms of no change before checking settling (default)
PDEndTime?          ; read the current value
```

## See also

- [InTargetStat](../05-motion-status/InTargetStat.md) — settling status checked after this delay
- [PDPos](PDPos.md) — counter whose changes reset the timer
