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

`AInMode` is saved to flash. Changing it does not move data each cycle; instead an internal routing table (see below) is rebuilt whenever the keyword is written.

## How it works

When `AInMode` is written, every input is re-parsed and an internal routing table is rebuilt. Each function holds a reference to the conditioned reading ([AInPort](AInPort.md)`[1]`–`[4]`) and the raw reading ([AInPort](AInPort.md)`[5]`–`[8]`) of the input assigned to it, plus a defined/undefined flag. Functions that are not assigned read a constant zero, so an unconfigured function reads `0` rather than stale data. The table is updated atomically so a control cycle never sees a half-updated routing.

The **lower 16 bits** select the function (valid range 0–10):

| Lower 16-bit value | Functionality | Consumed by |
|--------------------|---------------|-------------|
| 0 | General input – no control function | Read via `AInPort` only |
| 1 | Velocity command | Velocity-control mode sets the velocity reference from this input |
| 2 | Current command | Current-mode current reference |
| 3 | Force feedback | Force feedback `Force`; also the value tested by [CurrAInTh](../../08-axis-operation/03-current-operation-mode/CurrAInTh.md) and [ForceAInTh](../../08-axis-operation/04-force-operation-mode/ForceAInTh.md) |
| 4 | Force command | Force-mode force reference |
| 5 | Joystick input | Jog / position target in the profiler |
| 6 | Torque compensation | Added to the current reference |
| 7 | Reverse (negative) current limit | Clamps the current reference |
| 8 | Forward (positive) current limit | Clamps the current reference |
| 9 | Tachometer feedback | Velocity feedback for dual-loop |
| 10 | Position feedback | Main/aux encoder position from the *raw* reading |

Writing a function value greater than 10 is rejected: that `AInMode` entry is zeroed and an out-of-range condition is logged.

The **upper 16 bits** select which axes consume the function — each bit is one axis, and multiple bits may be set so one physical input can drive several axes:

| Value, Bit# | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|-------------|----|----|----|----|----|----|----|----|
| Axis | A | B | C | D | E | F | G | H |

If the upper 16 bits are **all zero**, the function is assigned to axis A — preserved for backward compatibility.

> Note: position feedback (function 10) uses the **raw** reading ([AInPort](AInPort.md)`[5]`–`[8]`), not the conditioned one; the filter/offset/gain stages do not apply to it.

## Examples

To use analog input 2 of axis C as the force feedback of axis A:

$$
\text{CAInMode}[2] = 3 + 2^{16} = 65539
$$

```text
AAInMode[1]=1        ; analog input 1 -> velocity command of axis A
AAInMode[1]=3        ; analog input 1 -> force feedback of axis A
AAInMode               ; read the current AInMode assignments
```

### Edge cases

- **Index 0** — invalid; valid indices are `AInMode[1]`–`AInMode[4]`. `AInMode[0]` does not exist.
- **Out-of-range function** — values with lower 16 bits > 10 are rejected: the entry is zeroed and an `AINMODE_OUT_OF_RANGE` warning is logged.
- **Unassigned function** — a function that no input maps to reads a constant `0` rather than stale data, so a missing route fails safe.
- **Multiple inputs to one function** — the routing table is rebuilt input-by-input in ascending order; if two inputs assign the same function to the same target axis, the later input's pointer wins.
- **Multi-axis broadcast** — setting more than one upper-bit fans one input out to multiple axes; each target axis reads the same conditioned value.
- **Wrong-mode use** — assigning function 1 (velocity command) does not switch the axis into [VELOCITY_CONTROL](../../08-axis-operation/01-general-keywords/OperationMode.md); the routed value is only used while the consuming mode is active. The route is harmless in other modes.
- **Position feedback (code 10)** — uses the **raw** [AInPort](AInPort.md)`[5]`–`[8]` reading; the filter, offset, deadband and gain stages do not apply to it.
- **Motor on/off** — routing is rebuilt on write; existing routes are unaffected by `MotorOn` transitions.
- **Save / Reset** — `AInMode` is flash-saveable. Persisted routes are reapplied at boot via the same parser.
- **Platform** — code list 0–10 is identical on standalone, central-i v4 and central-i v5.

## See also

- [AInPort](AInPort.md) — analog-input readings (the values routed by `AInMode`)
- [AInGain](AInGain.md), [AInOffset](AInOffset.md), [AInFilt](AInFilt.md), [AInDB](AInDB.md), [AInMuteRange](AInMuteRange.md) — the conditioning chain applied before routing
- [CurrAInTh](../../08-axis-operation/03-current-operation-mode/CurrAInTh.md), [ForceAInTh](../../08-axis-operation/04-force-operation-mode/ForceAInTh.md) — thresholds that act on the force-feedback function
