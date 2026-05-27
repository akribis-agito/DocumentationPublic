---
keyword: DOutSelect
summary: Selects the hardware function (or software control) routed to each digital output.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 314
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 17
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 15
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DOutSelect

Selects the hardware function (or software control) routed to each digital output.

## Overview

`DOutSelect` assigns a hardware function to a digital output through a multiplexer. The array **index** is the output number (1-based: `DOutSelect[1]` is output 1). Setting it to `0` hands the output back to software control via [DOutMode](DOutMode.md). Hardware functions (events, P/D signals, UserPWM) run on the hardware layer for high-frequency signals; when a hardware function is selected, `DOutMode` and `DOutPort` are irrelevant for that output. The available functions differ by product:

| Value | Standalone | Central-i slaves |
|-------|------------|------------------|
| 0 | Software (using DOutMode) | Software (using DOutMode) |
| 1 | Reserved | Reserved |
| 2 | A event #1 | Main event #1 |
| 3 | A event #2 | Main event #2 |
| 4 | A event #3 | Main event #3 |
| 5 | B event #1 | Aux. event #1 (not implemented) |
| 6 | B event #2 | Aux. event #2 (not implemented) |
| 7 | B event #3 | Aux. event #3 (not implemented) |
| 8 | C event #1 | Pulse (P/D control) |
| 9 | C event #2 | Direction (P/D control) |
| 10 | C event #3 | Reserved |
| 11 | UserPWM 1 | Reserved |
| 12 | UserPWM 2 | UserPWM 1 |
| 13 | Reserved | UserPWM 2 |
| 14 | Reserved | Reserved |
| 15 | Reserved | Central-i remote signal |

## Examples

```text
ADOutSelect[3]=0     ; output 3 is software-controlled (uses DOutMode[3])
ADOutSelect[4]=2     ; output 4 = Main Event #1 (Central-i) / A event #1 (standalone)
```

## See also

- [DOutMode](DOutMode.md) — software function (when DOutSelect = 0)
- [DOutPort](DOutPort.md) — manual output state
- [UserPWM](UserPWM.md) — user PWM channels
