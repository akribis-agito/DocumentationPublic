---
keyword: PIVNoiseStat
summary: Read-only status array exposing the live noise statistic and active threshold of the PIV noise detector.
availability:
  standalone: []
  central-i:
  - v5
can_code: 799
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PIVNoiseStat

Read-only status array exposing the live noise statistic and active threshold of the PIV noise detector.

## Overview

`PIVNoiseStat` is a read-only array that reports what the PIV noise detector ([PIVNoiseDtct](PIVNoiseDtct.md)) is computing. It lets you watch the measured standstill noise statistic against the active trip threshold while tuning, so you can pick a sensible value for [PIVNoiseSTD](PIVNoiseSTD.md) and judge how much margin there is.

The values are updated while the detector is enabled and the axis is at a commanded standstill. The reported statistic reads as zero until the axis has been held still long enough to fill the window (see [PIVNoiseWSize](PIVNoiseWSize.md)), which is the controller's way of suppressing the measurement during and just after a move.

This keyword is available from v5 (central-i) only.

## How it works

The array is 1-indexed. The usable elements are:

| Index | Element |
|---|---|
| 1 | Measured spread (variance) of the current reference at standstill over the window. Reads zero until the standstill window is full. |
| 2 | Active spread threshold the measurement at index 1 is compared against. |

A fault is raised when the measured spread (index 1) exceeds the threshold (index 2). The threshold at index 2 is derived from [PIVNoiseSTD](PIVNoiseSTD.md) scaled against the peak current limit. On a trip the controller turns the motor off and logs fault code 1072 in [ConFlt](../../07-status-and-faults/ConFlt.md).

## Examples

```text
APIVNoiseStat[1]      ; live standstill noise statistic
APIVNoiseStat[2]      ; active threshold (trip level for index 1)
```

## See also

- [PIVNoiseDtct](PIVNoiseDtct.md) — enable the PIV noise detector
- [PIVNoiseSTD](PIVNoiseSTD.md) — spread threshold (reflected at index 2)
- [PIVNoiseWSize](PIVNoiseWSize.md) — statistics window size
- [ConFlt](../../07-status-and-faults/ConFlt.md) — controller fault code (1072 on detection)
