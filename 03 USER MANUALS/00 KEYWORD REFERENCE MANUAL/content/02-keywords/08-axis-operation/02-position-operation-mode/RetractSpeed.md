---
keyword: RetractSpeed
summary: Maximum velocity of the point-to-point move on entry to position mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 608
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
  - -1300000000
  - 1300000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
---
# RetractSpeed

Maximum velocity of the point-to-point move on entry to position mode.

## Overview

`RetractSpeed` is the maximum velocity used in the point-to-point motion that runs upon entry to position operation mode. The move runs only when the [BeginOnToPos](BeginOnToPos.md) flag is set, toward the target defined by [RetractTarget](RetractTarget.md).

## Examples

```text
RetractSpeed=20000  ; entry-move speed (user units)
RetractTarget=50000 ; entry-move target
BeginOnToPos=1      ; arm the move
GoToPosMode         ; switch and start the move
```

## See also

- [BeginOnToPos](BeginOnToPos.md) — arms the entry move
- [RetractTarget](RetractTarget.md) — target of the entry move
