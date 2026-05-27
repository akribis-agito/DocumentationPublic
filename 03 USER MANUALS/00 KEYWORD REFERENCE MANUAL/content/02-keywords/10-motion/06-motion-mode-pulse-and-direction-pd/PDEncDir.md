---
keyword: PDEncDir
summary: Configures the sign (direction) of PDPos accumulation relative to the direction signal.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 63
attributes:
  access: '0'
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides:
  central-i.v5:
    access: rw
    units: none
    range:
    - 0
    - 1
    implemented: final
---
# PDEncDir

Configures the sign (direction) of PDPos accumulation relative to the direction signal.

## Overview

`PDEncDir` configures the direction of [PDPos](PDPos.md) accumulation, i.e. whether a logic-high direction signal causes the counter to increment or decrement. It lets the pulse-and-direction decoding sense be reversed without rewiring, complementing the magnitude scaling set by [PDFact](PDFact.md) and [PDFactDen](PDFactDen.md).

> **Documentation pending:** This keyword is marked as not implemented in the current firmware. The behaviour below is described for reference; confirm against firmware before relying on it.

## How it works

| Value | Description |
|---|---|
| 0 | **Normal direction.** PDPos increments by the number of pulses received multiplied by scaling if the direction signal is logic high, and decrements by such value if the direction signal is logic low. |
| 1 | **Inverted direction.** PDPos decrements by the number of pulses received multiplied by scaling if the direction signal is logic high, and increments by such value if the direction signal is logic low. |

## Examples

```text
APDEncDir=0          ; normal accumulation direction (default)
APDEncDir=1          ; inverted accumulation direction
```

## See also

- [PDPos](PDPos.md) — counter whose accumulation direction this sets
- [PDFact](PDFact.md) / [PDFactDen](PDFactDen.md) — scaling-factor magnitude
