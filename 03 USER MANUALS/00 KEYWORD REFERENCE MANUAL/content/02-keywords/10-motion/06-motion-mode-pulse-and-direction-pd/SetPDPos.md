---
keyword: SetPDPos
summary: Command that presets/re-zeroes the pulse-and-direction position counter without moving.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 156
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# SetPDPos

Command that presets/re-zeroes the pulse-and-direction position counter without moving.

## Overview

`SetPDPos` is a command that sets the pulse-and-direction input position counter [PDPos](PDPos.md) to a specified value. It lets the P/D position reference be re-zeroed or preset without physically moving the axis, which is useful when aligning the decoded counter to a known reference. It is an axis-related command function that cannot be issued while the axis is in motion.

## Examples

```text
ASetPDPos=0          ; re-zero the P/D counter
ASetPDPos=100000     ; preset the P/D counter to a known value
```

## See also

- [PDPos](PDPos.md) — the counter this command sets
- [PDSubType](PDSubType.md) — P/D input signal format
- [PDFact](PDFact.md) — P/D input scaling factor numerator
- [SetPosition](../03-kinematics-configuration/SetPosition.md) — analogous preset for the axis position
