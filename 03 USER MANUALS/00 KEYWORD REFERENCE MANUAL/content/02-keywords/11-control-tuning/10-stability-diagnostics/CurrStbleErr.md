---
keyword: CurrStbleErr
summary: Current-loop tracking-error threshold for stability detection, in percent of the peak current limit.
availability:
  standalone: []
  central-i:
  - v5
can_code: 790
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
# CurrStbleErr

Current-loop tracking-error threshold for stability detection, in percent of the peak current limit.

## Overview

`CurrStbleErr` sets one of the two thresholds used by the current-loop stability detector ([CurrStbleDtct](CurrStbleDtct.md)). It is the tracking-error threshold: the smallest average current tracking error that, combined with an oscillating current spread, is treated as evidence of an unstable current loop.

The value is a percentage of the axis peak current limit ([PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md)). A larger value makes the detector less sensitive (the loop must mistrack more before it trips); a smaller value makes it trip on smaller errors. The default is 2 (i.e. 2% of the peak current limit).

This keyword is available from v5 (central-i) only.

## How it works

The detector measures the average magnitude of the difference between the commanded current reference and the measured motor current over its sliding window. A fault is raised only when this average error exceeds the `CurrStbleErr` threshold *and* the current spread test (see [CurrStbleSTD](CurrStbleSTD.md)) is also satisfied at the same time. Requiring both conditions avoids tripping on a quiet loop that simply has a steady offset, or on a noisy reference that the loop is in fact tracking well.

Internally the percentage is converted to a current threshold by scaling against the peak current limit, so changing [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) automatically rescales the effective error threshold. The value is saved to flash and can be changed while the axis is in motion and while the motor is on. The effective tracking-error threshold is recomputed immediately whenever the value is written — including while the detector is already running and the motor is on — and takes effect on the next control cycle; no re-enable is required.

The threshold currently in effect can be read back from element 5 of [CurrStbleStat](CurrStbleStat.md).

## Examples

```text
ACurrStbleErr=2       ; tracking-error threshold = 2% of peak current limit (default)
ACurrStbleErr=5       ; less sensitive: require a larger tracking error
ACurrStbleErr[1]      ; read back the configured percentage
```

## See also

- [CurrStbleDtct](CurrStbleDtct.md) — enable the current-loop stability detector
- [CurrStbleSTD](CurrStbleSTD.md) — current-loop spread threshold (the other trip condition)
- [CurrStbleStat](CurrStbleStat.md) — current-loop stability detector status array
- [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) — peak current limit the threshold is scaled to
