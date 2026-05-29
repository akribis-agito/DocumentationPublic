---
keyword: CurrStbleStat
summary: Read-only status array exposing the live statistics and thresholds of the current-loop stability detector.
availability:
  standalone: []
  central-i:
  - v5
can_code: 792
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 7
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
# CurrStbleStat

Read-only status array exposing the live statistics and thresholds of the current-loop stability detector.

## Overview

`CurrStbleStat` is a read-only array that reports what the current-loop stability detector ([CurrStbleDtct](CurrStbleDtct.md)) is computing each control cycle. It lets you watch the running statistics and the active trip thresholds side by side while tuning a current loop, so you can choose sensible values for [CurrStbleSTD](CurrStbleSTD.md) and [CurrStbleErr](CurrStbleErr.md) and see how much headroom there is before a trip.

The array is updated while the detector is enabled and the motor is on. When the detector is disabled the values are not refreshed and hold their last contents.

This keyword is available from v5 (central-i) only.

## How it works

The array is 1-indexed. The usable elements are:

| Index | Element |
|---|---|
| 1 | Spread (variance) of the commanded current reference over the window. |
| 2 | Spread (variance) of the measured motor current over the window. |
| 3 | Average magnitude of the current tracking error over the window. |
| 4 | Active spread threshold the motor-current spread (index 2) is compared against. |
| 5 | Active tracking-error threshold the error (index 3) is compared against. |
| 6 | Reserved. |

A fault is raised when the motor-current spread (index 2) exceeds the spread threshold (index 4) and, at the same time, the tracking error (index 3) exceeds the error threshold (index 5). The thresholds at indices 4 and 5 are derived from [CurrStbleSTD](CurrStbleSTD.md) and [CurrStbleErr](CurrStbleErr.md) scaled against the peak current limit. On a trip the controller turns the motor off and logs fault code 1071 in [ConFlt](../../07-status-and-faults/ConFlt.md).

## Examples

```text
ACurrStbleStat[2]     ; live spread of the measured motor current
ACurrStbleStat[4]     ; active spread threshold (trip level for index 2)
ACurrStbleStat[3]     ; live average tracking error
ACurrStbleStat[5]     ; active tracking-error threshold (trip level for index 3)
```

## See also

- [CurrStbleDtct](CurrStbleDtct.md) — enable the current-loop stability detector
- [CurrStbleSTD](CurrStbleSTD.md) — spread threshold (reflected at index 4)
- [CurrStbleErr](CurrStbleErr.md) — tracking-error threshold (reflected at index 5)
- [ConFlt](../../07-status-and-faults/ConFlt.md) — controller fault code (1071 on detection)
