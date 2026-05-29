---
keyword: CurrStbleDtct
summary: Enables run-time detection of an unstable (oscillating) current loop on the axis.
availability:
  standalone: []
  central-i:
  - v5
can_code: 789
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrStbleDtct

Enables run-time detection of an unstable (oscillating) current loop on the axis.

## Overview

`CurrStbleDtct` turns the current-loop stability detector on or off. When enabled, the controller continuously watches the current loop and, if it concludes the loop is oscillating, turns the motor off and logs a controller fault so an unstable loop cannot keep driving the motor. This is useful as a safety net during current-loop tuning and in production, where a poorly tuned or marginal loop could otherwise self-excite.

| Value | Meaning |
|---|---|
| 0 | Detector disabled (default). |
| 1 | Detector enabled. |

This keyword is available from v5 (central-i) only.

## How it works

While the motor is on and the detector is enabled, the controller maintains running statistics over a sliding window of recent samples and tests two conditions every control cycle:

- the spread (variance) of the measured motor current is substantially larger than the spread of the commanded current reference, and
- the average magnitude of the current tracking error is above its threshold.

When both conditions hold at the same time, the loop is judged to be oscillating: the controller turns the motor off and records the fault, which appears in [ConFlt](../../07-status-and-faults/ConFlt.md) as fault code 1071 (unstable current loop detected).

The two thresholds are configured as a percentage of the axis peak current limit ([PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md)): [CurrStbleSTD](CurrStbleSTD.md) sets the spread threshold and [CurrStbleErr](CurrStbleErr.md) sets the tracking-error threshold. The live statistics and active thresholds can be read back through [CurrStbleStat](CurrStbleStat.md).

Enabling the detector takes effect when the motor is on; the statistics windows are cleared at that point so detection starts from a clean state. Setting the keyword back to 0 disables detection immediately. Because the detector can be turned on and off at any time, this keyword can be written while the axis is in motion and while the motor is on.

## Examples

```text
ACurrStbleSTD=2       ; spread threshold 2% of peak current limit
ACurrStbleErr=2       ; tracking-error threshold 2% of peak current limit
ACurrStbleDtct=1      ; enable the current-loop stability detector
ACurrStbleDtct[1]     ; read back the enable state
```

## See also

- [CurrStbleErr](CurrStbleErr.md) — current-loop tracking-error threshold
- [CurrStbleSTD](CurrStbleSTD.md) — current-loop spread threshold
- [CurrStbleStat](CurrStbleStat.md) — current-loop stability detector status array
- [ConFlt](../../07-status-and-faults/ConFlt.md) — controller fault code (1071 on detection)
- [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) — peak current limit the thresholds are scaled to
