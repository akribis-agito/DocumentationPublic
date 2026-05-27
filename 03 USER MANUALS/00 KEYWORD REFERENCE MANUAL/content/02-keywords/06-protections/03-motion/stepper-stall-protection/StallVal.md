---
keyword: StallVal
summary: Read-only current value of the stepper stall-detection metric.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 511
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# StallVal

Read-only current value of the stepper stall-detection metric.

## Overview

`StallVal` is the read-only, live value of the stepper stall-detection metric — the quantity compared against the threshold [StallTh](StallTh.md) to decide [StallStat](StallStat.md). It is derived from the motor phase voltages and acts as a proxy for the motor's load angle / back-EMF: when a stepper stalls, this value collapses.

## How it works

The metric is computed every control sample inside the stepper current-loop branch. First the sum of the squared phase-voltage differences is formed:

```text
voltage sum = (Va-Vc)² + (Vb-Vc)²
```

then it is passed through a first-order low-pass filter (smoothing factor `0.005`, ≈13 Hz cutoff) to produce `StallVal`:

```text
StallVal = voltage sum * 0.005 + 0.995 * previous StallVal
```

`Va`, `Vb`, `Vc` are the (post-saturation) phase voltages of the stepper. While the motor tracks its commanded electrical angle, these phase-voltage differences stay high; when the rotor falls out of step (stalls), the effective contribution drops and `StallVal` falls. A stall is declared when `StallVal` drops **below** the computed threshold [StallTh](StallTh.md). `StallVal` is reset to `0` when the motor is off.

> Note: this metric is produced only for stepper motors driven by the internal amplifier; it is not generated for servo or external-amplifier configurations.

## Examples

```text
AStallVal[1]          ; read the live stall metric (filtered)
```

## See also

- [StallTh](StallTh.md) — threshold this value is compared against (stall if `StallVal < StallTh`)
- [StallStat](StallStat.md) — resulting stall flag
- [StallCfg](StallCfg.md) — enables/selects stall detection
