---
keyword: StallCnst
summary: Tuning constants for stepper stall detection (3-element array).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 515
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
# StallCnst

Tuning constants for stepper stall detection.

## Overview

`StallCnst` is an array holding the coefficients of a **linear fit of the expected stall metric versus commanded speed**. The stall-threshold calculation uses them to predict the healthy [StallVal](StallVal.md) at the current speed, so that a genuine collapse (stall) can be distinguished from the normal speed dependence of the metric.

## How it works

When building the threshold [StallTh](StallTh.md) each sample, the firmware evaluates the fit `slope·speed + intercept`:

```text
fit = StallCnst[1] * speed + StallCnst[2]    ; slope*speed + intercept
```

where `speed` is the (bit-shifted) absolute commanded speed.

| Element | Role |
|---------|------|
| `StallCnst[1]` | **Slope** — how fast the expected metric grows with speed |
| `StallCnst[2]` | **Intercept** — the expected metric at (near) zero speed |

The resulting fit is then scaled by [StallThPcnt](StallThPcnt.md) and offset to form [StallTh](StallTh.md). The array is sized 3; only the slope and intercept entries above participate in the threshold formula.

These coefficients are determined for a specific motor/load by characterising the healthy `StallVal` at several speeds and fitting a line. Until they are set appropriately for the application, stall detection will not track speed correctly.

## Examples

```text
AStallCnst[1]=...     ; slope of the expected-metric-vs-speed fit
AStallCnst[2]=...     ; intercept of the fit
AStallCnst[1]         ; read back the slope
```

## See also

- [StallTh](StallTh.md) — threshold that uses these coefficients
- [StallThPcnt](StallThPcnt.md) — percentage that scales the fit
- [StallVal](StallVal.md) — the metric these coefficients model
- [StallCfg](StallCfg.md) — stall-detection mode
