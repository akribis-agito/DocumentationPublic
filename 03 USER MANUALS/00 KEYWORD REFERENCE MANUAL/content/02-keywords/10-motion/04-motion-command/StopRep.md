---
keyword: StopRep
summary: Stops repetitive (repeat) motion and clears the repeat-motion state.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 148
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# StopRep

Stops repetitive (repeat) motion and clears the repeat-motion state.

## Overview

`StopRep` is a command that stops repetitive point-to-point motion (the mode selected by [MotionMode](../02-motion-configuration/MotionMode.md) = 2). It decelerates the axis to rest and clears the repeat-motion state, ending the cycle early instead of waiting for [RptCycles](../02-motion-configuration/RptCycles.md) to be reached. The repetition behaviour it terminates is configured by [RptMode](../02-motion-configuration/RptMode.md). It can be issued during motion. It is an axis-related command function.

## Examples

```text
AStopRep             ; stop repetitive motion
```

## See also

- [Stop](Stop.md) — general controlled stop
- [RptMode](../02-motion-configuration/RptMode.md) — repetition direction
- [RptCycles](../02-motion-configuration/RptCycles.md) — number of repetitions
