---
keyword: SetPDPos
summary: Command that presets/re-zeroes the pulse-and-direction position counter without moving.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`SetPDPos` is a command that sets the pulse-and-direction input position counter [PDPos](PDPos.md) to a specified value. It lets the P/D counter be re-zeroed or preset without physically moving the axis, which is useful when aligning the decoded counter to a known reference. It is an axis-related command function that cannot be issued while the axis is in motion (the motor may be on).

## How it works

`SetPDPos` (`AG300_CTL01Funcs.c:7344`) writes the value to both representations of the counter atomically (interrupts disabled around the write), and clears the derived velocity:

```text
glPDPos  = value
gllPDPos = (long long) value << 32      ; rebuild the 32.32 accumulator
glPDVel  = 0
```

Because it sets the 32.32 accumulator `gllPDPos` directly (not just the reported `PDPos`), subsequent per-cycle deltas accumulate from the new base. It does **not** touch the value latched at [Begin](../04-motion-command/Begin.md) (`gllPDPosInitial`): during an active direct/indirect P/D motion, motion is measured relative to that latched value, so presetting the counter mid-motion would shift it — preset before issuing `Begin`. This is the P/D-input analogue of [SetPosition](../03-kinematics-configuration/SetPosition.md), which presets the axis feedback.

## Examples

```text
ASetPDPos=0          ; re-zero the P/D counter
ASetPDPos=100000     ; preset the P/D counter to a known value
```

## See also

- [PDPos](PDPos.md) — the counter this command sets
- [PDSubType](PDSubType.md) — P/D input signal format
- [PDFact](PDFact.md) — P/D input scaling factor numerator
- [SetPosition](../03-kinematics-configuration/SetPosition.md) — analogous preset for the axis feedback position
