---
keyword: PDSubType
summary: Selects the pulse-and-direction input signal format (e.g. step/direction vs. CW/CCW).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 421
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDSubType

Selects the pulse-and-direction input signal format (e.g. step/direction vs. CW/CCW).

## Overview

`PDSubType` selects the sub-type of pulse-and-direction input mode, choosing between different input signal formats (for example, step/direction vs. CW/CCW pulse inputs). It tells the decoder how to interpret the incoming pulse pair so that [PDPos](PDPos.md) accumulates correctly for the connected master device. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion or the motor is on.

## Examples

```text
APDSubType=0         ; default input format
APDSubType=1         ; alternate input format
```

## See also

- [PDPos](PDPos.md) — counter populated according to the selected sub-type
- [PDFact](PDFact.md) / [PDFactDen](PDFactDen.md) — input scaling factor
- [SetPDPos](SetPDPos.md) — preset/re-zero the P/D counter
