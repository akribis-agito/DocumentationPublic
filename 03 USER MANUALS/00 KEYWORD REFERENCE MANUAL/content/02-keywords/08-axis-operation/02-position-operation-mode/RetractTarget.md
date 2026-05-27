---
keyword: RetractTarget
summary: Absolute target of the point-to-point move on entry to position mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 609
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RetractTarget

Absolute target of the point-to-point move on entry to position mode.

## Overview

`RetractTarget` is the absolute target used in the point-to-point motion that runs upon entry to position operation mode, subject to the [BeginOnToPos](BeginOnToPos.md) flag and the [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md) value. If `RelTrgt` is non-zero, the target position is instead `RelTrgt` relative to the position reference at the moment of entry into position mode. The move runs at [RetractSpeed](RetractSpeed.md).

## Examples

```text
ARetractTarget=50000 ; absolute entry-move target (user units)
ARetractSpeed=20000  ; entry-move speed
ABeginOnToPos=1      ; arm the move
AGoToPosMode         ; switch and start the move
```

## See also

- [BeginOnToPos](BeginOnToPos.md) — arms the entry move
- [RetractSpeed](RetractSpeed.md) — speed of the entry move
- [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md) — relative-target override
