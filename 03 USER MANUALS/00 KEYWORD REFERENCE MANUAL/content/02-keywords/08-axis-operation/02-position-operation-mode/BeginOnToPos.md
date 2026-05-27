---
keyword: BeginOnToPos
summary: One-time flag to run a point-to-point move on entering position mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 587
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
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
# BeginOnToPos

One-time flag to run a point-to-point move on entering position mode.

## Overview

`BeginOnToPos` is a one-time flag which, if set, instructs the controller to perform a point-to-point motion upon entering position operation mode. After the motion, `BeginOnToPos` is cleared.

The target position is defined by [RetractTarget](RetractTarget.md) (or [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md)) and the velocity by [RetractSpeed](RetractSpeed.md). This flag works only with the [GoToPosMode](GoToPosMode.md) command and the internal switching algorithm; it has no effect when [OperationMode](../01-general-keywords/OperationMode.md) is changed by direct assignment.

## Examples

```text
ARetractTarget=50000 ; target for the entry move
ARetractSpeed=20000  ; speed for the entry move
ABeginOnToPos=1      ; arm the entry move
AGoToPosMode         ; switch to position mode and start the move
```

## See also

- [GoToPosMode](GoToPosMode.md) — command that triggers the armed move
- [RetractTarget](RetractTarget.md) — absolute target of the entry move
- [RetractSpeed](RetractSpeed.md) — speed of the entry move
