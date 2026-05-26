---
keyword: AInMode
summary: Assigns a control function to each analog input, with per-axis targeting.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 257
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AInMode

Assigns a control function to each analog input, with per-axis targeting.

## Overview

`AInMode` assigns a functionality to an analog input. The **index** selects the input — e.g. `AInMode[2]` configures analog input 2. (The axis prefix is only relevant on Central-i products with multiple I/O modules on different axes.)

## How it works

The **lower 16 bits** of the value select the function:

| Lower 16-bit value | Functionality |
|--------------------|---------------|
| 0 | General input – no function |
| 1 | Velocity command |
| 2 | Current command |
| 3 | Force feedback |
| 4 | Force command |
| 5 | Joystick input |
| 6 | Torque compensation |
| 7 | Negative current limit (for CurrRef) |
| 8 | Positive current limit (for CurrRef) |
| 9 | Tachometer feedback |
| 10 | Position feedback |

The **upper 16 bits** select which axes the function applies to — each bit is one axis, and multiple bits may be set:

| Value, Bit# | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|-------------|----|----|----|----|----|----|----|----|
| Axis | A | B | C | D | E | F | G | H |

## Examples

To use analog input 2 of axis C as the force feedback of axis A:

$$
CAInMode\lbrack 2\rbrack\ = \ 3\ + \ 2\hat{}16\ = \ 65539
$$

## See also

- [AInPort](AInPort.md) — analog-input readings
- [AInGain](AInGain.md), [AInOffset](AInOffset.md) — input conditioning
