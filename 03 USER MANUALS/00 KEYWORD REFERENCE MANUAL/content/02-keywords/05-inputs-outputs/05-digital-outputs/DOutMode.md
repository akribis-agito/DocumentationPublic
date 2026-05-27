---
keyword: DOutMode
summary: Maps a controller status onto each digital output (software function assignment).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 210
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
  - 65557
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DOutMode

Maps a controller status onto each digital output (software function assignment).

## Overview

`DOutMode` assigns a software function to a digital output so the output reflects a selected controller status. It applies only when [DOutSelect](DOutSelect.md) for that output is `0` (software control). The array **index** is the output number (1-based: `DOutMode[1]` is output 1).

## How it works

The **lower 16 bits** select the function; the **upper 16 bits** select the axis whose status is reflected (A = 0, B = 1, …, L = 11).

| Value | Function |
|-------|----------|
| 0 | General output – no function (uses [DOutPort](DOutPort.md)) |
| 1 | Reserved |
| 2 | Motor-on status (1 = enabled) |
| 3 | In-motion status |
| 4 | In-acceleration status¹ |
| 5 | In-deceleration status¹ |
| 6 | In-constant-speed status¹ |
| 7 | End of motion – not implemented |
| 8 | In-target status (`InTargetStat = 4`) |
| 9 | Fault/alarm status (`ConFlt` ≠ 0) |
| 10 | Warnings in last motion – not implemented |
| 11 | Current saturation in last motion – not implemented |
| 12 | Limit active (`LimitsStat` ≠ 0) |
| 13 | Out-of-travel-range (PosRef > FwdPLim or < RevPLim) |
| 14 | Regeneration active |
| 15 | Dynamic-brake active |
| 16 | Motor-brake active |
| 17 | Reserved |
| 18 | Reverse limit switch (RLS) active (`LimitsStat` bit 0) |
| 19 | Forward limit switch (FLS) active (`LimitsStat` bit 1) |
| 20 | Homing done (`HomingStat = 100`) |
| 21 | Force-in-target status (`ForceInTrgtStat = 4`) |

¹ Valid only for motion modes that use the built-in profiler (e.g. indirect Pulse/Direction does; direct Pulse/Direction does not).

## Examples

`ADOutMode[2] = 65538` (upper 16 bits = 1 → axis B; lower 16 bits = 2 → motor-on): digital output 2 (of axis A) reflects axis B's motor-on status.

## See also

- [DOutSelect](DOutSelect.md) — must be 0 for DOutMode to apply
- [DOutPort](DOutPort.md) — manual output state (function 0)
