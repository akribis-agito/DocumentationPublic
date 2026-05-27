---
keyword: AInMode
summary: Assigns a control function to each analog input, with per-axis targeting.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`AInMode` assigns a functionality to an analog input — it routes the *conditioned* reading of an input (the result of the [conditioning chain](00-overview.md): filter, offset, deadband, gain, mute) to a specific control function such as a velocity command, current command, or force feedback. The array **index** selects the input (e.g. `AInMode[2]` configures analog input 2). The value is a 32-bit field: the lower 16 bits choose the function, the upper 16 bits choose which axes consume it.

`AInMode` is saved to flash. Changing it does not move data each cycle; instead the firmware rebuilds an internal routing table (see below) whenever the keyword is written.

## How it works

When `AInMode` is written the firmware re-parses every input and rebuilds a routing table `stAInFunctionality[axis][function]` (`SpecialFuncs.c:1494`, `SpAInMode`). Each entry holds a pointer to the conditioned reading (`AInPort[1..4]`) and the raw reading (`AInPort[5..8]`) of the input assigned to that function, plus an `sIsDefined` flag. Functions that are not assigned point at a constant zero, so an unconfigured function reads `0` rather than stale data. The table is double-buffered and copied into the live table with interrupts disabled, so a control cycle never sees a half-updated routing (`SpecialFuncs.c:1571`).

The **lower 16 bits** select the function (`AG300_CTL01ParamsCommon.h:2486`, `MAX_ANALOG_INPUT_MODE = 10`):

| Lower 16-bit value | Firmware constant | Functionality | Consumed by |
|--------------------|-------------------|---------------|-------------|
| 0 | `ANALOG_USER_INPUT` | General input – no control function | Read via `AInPort` only |
| 1 | `ANALOG_VELOCITY_COMMAND` | Velocity command | Velocity-control mode sets the velocity reference from this input (`AG300_CTL01ControlLoops.c:475`) |
| 2 | `ANALOG_CURRENT_COMMAND` | Current command | Current-mode current reference (`AG300_CTL01ControlLoops.c:969`) |
| 3 | `ANALOG_FORCE_FEEDBACK` | Force feedback | Force feedback `Force`/`gfForce`; also the value tested by [CurrAInTh](../../08-axis-operation/03-current-operation-mode/CurrAInTh.md) and [ForceAInTh](../../08-axis-operation/04-force-operation-mode/ForceAInTh.md) (`AG300_CTL01ControlInterrupt.c:2382`) |
| 4 | `ANALOG_FORCE_COMMAND` | Force command | Force-mode force reference (`AG300_CTL01ControlLoops.c:1131`) |
| 5 | `ANALOG_JOYSTICK_INPUT` | Joystick input | Jog / position target in the profiler (`AG300_CTL01Profiler.c:767`) |
| 6 | `ANALOG_TORQUE_COMP_INPUT` | Torque compensation | Added to the current reference (`AG300_CTL01ControlLoops.c:907`) |
| 7 | `ANALOG_INPUT_REVERSE_TORQUE_LIMIT` | Reverse (negative) current limit | Clamps the current reference (`AG300_CTL01ControlLoops.c:1897`) |
| 8 | `ANALOG_INPUT_FORWARD_TORQUE_LIMIT` | Forward (positive) current limit | Clamps the current reference (`AG300_CTL01ControlLoops.c:1887`) |
| 9 | `ANALOG_INPUT_TACHO_FEEDBACK` | Tachometer feedback | Velocity feedback for dual-loop (`AG300_CTL01ControlInterrupt.c:3270`) |
| 10 | `ANALOG_INPUT_POSITION_FEEDBACK` | Position feedback | Main/aux encoder position from the *raw* reading (`AG300_CTL01ControlInterrupt.c:2178`) |

Writing a function value greater than 10 is rejected: the firmware zeroes that `AInMode` entry and logs `AINMODE_OUT_OF_RANGE` (`SpecialFuncs.c:1532`).

The **upper 16 bits** select which axes consume the function — each bit is one axis, and multiple bits may be set so one physical input can drive several axes:

| Value, Bit# | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|-------------|----|----|----|----|----|----|----|----|
| Axis | A | B | C | D | E | F | G | H |

If the upper 16 bits are **all zero**, the function is assigned to axis A — preserved for backward compatibility (`SpecialFuncs.c:1543`).

> Note: position feedback (function 10) uses the **raw** reading (`lpSrcAinFromHW`, `AInPort[5..8]`), not the conditioned one; the filter/offset/gain stages do not apply to it.

## Examples

To use analog input 2 of axis C as the force feedback of axis A:

$$
CAInMode\lbrack 2\rbrack\ = \ 3\ + \ 2\hat{}16\ = \ 65539
$$

```text
AAInMode[1]=1        ; analog input 1 -> velocity command of axis A
AAInMode[1]=3        ; analog input 1 -> force feedback of axis A
AAInMode               ; read the current AInMode assignments
```

## See also

- [AInPort](AInPort.md) — analog-input readings (the values routed by `AInMode`)
- [AInGain](AInGain.md), [AInOffset](AInOffset.md), [AInFilt](AInFilt.md), [AInDB](AInDB.md), [AInMuteRange](AInMuteRange.md) — the conditioning chain applied before routing
- [CurrAInTh](../../08-axis-operation/03-current-operation-mode/CurrAInTh.md), [ForceAInTh](../../08-axis-operation/04-force-operation-mode/ForceAInTh.md) — thresholds that act on the force-feedback function
