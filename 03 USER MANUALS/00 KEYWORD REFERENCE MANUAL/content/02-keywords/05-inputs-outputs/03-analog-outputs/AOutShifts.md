---
keyword: AOutShifts
summary: Power-of-two scaling applied to the monitored parameter on an analog output.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 221
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
  range:
  - -31
  - 31
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AOutShifts

Power-of-two scaling applied to the monitored parameter on an analog output.

## Overview

`AOutShifts` scales the monitored parameter (see [AOutMode](AOutMode.md)) by a power of two, to fit it into the output's dynamic range. The array index is the analog-output number (e.g. `AOutShifts[1]` applies to analog output 1). This is the scaling stage of the [analog-output signal path](00-overview.md) in monitoring mode.

## How it works

A **positive** value shifts left — multiplying the value by $2^{AOutShifts}$. A **negative** value shifts right — dividing by $2^{|AOutShifts|}$.

$$
\text{Analog output [mV]} = \text{Monitored parameter [internal units]} \times 2^{\text{AOutShifts}}
$$

## Examples

```text
AOutShifts[1]=2     ; multiply the monitored value by 4
AOutShifts[1]=-3    ; divide the monitored value by 8
```

## See also

- [AOutMode](AOutMode.md) — selects the monitored parameter
- [AOutOffset](AOutOffset.md) — output offset (applied after scaling)
