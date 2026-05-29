---
keyword: CurrStbleSTD
summary: "Current-loop spread threshold for stability detection, in percent of the peak current limit."
availability:
  standalone: []
  central-i:
  - v5
can_code: 791
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 100
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrStbleSTD

Current-loop spread threshold for stability detection, in percent of the peak current limit.

## Overview

`CurrStbleSTD` sets the spread (standard-deviation) threshold used by the current-loop stability detector ([CurrStbleDtct](CurrStbleDtct.md)). It defines a floor on how much the measured motor current is allowed to swing before that swing can be treated as oscillation.

The value is a percentage of the axis peak current limit ([PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md)). The default is 2 (i.e. a 2% standard deviation of the peak current). A larger value makes the detector tolerate more current swing; a smaller value makes it more sensitive.

This keyword is available from v5 (central-i) only.

## How it works

The detector tracks the spread of the measured motor current over a sliding window. The current swing is considered excessive when it exceeds the larger of two limits:

- a fixed multiple of the spread of the commanded current reference (so an axis that is genuinely commanded to move a lot is not flagged), and
- the absolute floor set by `CurrStbleSTD` (so a quiet command with a swinging motor current is flagged).

When the motor-current spread is above this combined limit *and* the tracking error exceeds its threshold ([CurrStbleErr](CurrStbleErr.md)), the detector turns the motor off and logs fault code 1071, visible in [ConFlt](../../07-status-and-faults/ConFlt.md).

The percentage is scaled against the peak current limit and squared internally (because spread is compared on a variance basis), so the comparison floor tracks [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) automatically. The value is saved to flash and can be changed while the axis is in motion and while the motor is on; it is applied the next time the detector is (re)enabled with the motor on. The active spread threshold can be read back from element 4 of [CurrStbleStat](CurrStbleStat.md).

## Examples

```text
ACurrStbleSTD=2       ; spread threshold = 2% of peak current limit (default)
ACurrStbleSTD=10      ; tolerate more current swing before flagging
ACurrStbleSTD[1]      ; read back the configured percentage
```

## See also

- [CurrStbleDtct](CurrStbleDtct.md) — enable the current-loop stability detector
- [CurrStbleErr](CurrStbleErr.md) — current-loop tracking-error threshold (the other trip condition)
- [CurrStbleStat](CurrStbleStat.md) — current-loop stability detector status array
- [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) — peak current limit the threshold is scaled to
