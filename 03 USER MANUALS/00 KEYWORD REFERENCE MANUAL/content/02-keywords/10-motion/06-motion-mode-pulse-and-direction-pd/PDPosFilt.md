---
keyword: PDPosFilt
summary: First-order low-pass cut-off frequency (Hz/100) smoothing PDPos in direct P/D mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 150
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 4150
  - 2147483647
  default: 12800
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDPosFilt

First-order low-pass cut-off frequency (Hz/100) smoothing PDPos in direct P/D mode.

## Overview

`PDPosFilt` is the cut-off frequency of a first-order low-pass filter applied to the change of [PDPos](PDPos.md) since the start of motion. It smooths the generated position reference so that the axis ramps rather than steps when the decoded pulse-and-direction command jumps. It is only used in **direct** P/D motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 3); indirect P/D motion uses the second-order profile generator instead and has no such filter.

`PDPosFilt` is the cut-off-frequency form of the same smoothing concept as the coefficient-based [PDFiltFact](PDFiltFact.md).

## How it works

The value is expressed in units of Hz/100. For example, a required cut-off frequency of 250 Hz means `PDPosFilt = 25000`. The default value of `12800` corresponds to a cut-off frequency of 128 Hz.

## Examples

```text
PDPosFilt=25000     ; 250 Hz cut-off frequency
PDPosFilt=12800     ; 128 Hz cut-off frequency (default)
```

## See also

- [PDPos](PDPos.md) — counter whose change is filtered
- [PDFiltFact](PDFiltFact.md) — coefficient-based form of the direct-mode P/D filter
- [MotionMode](../02-motion-configuration/MotionMode.md) — selects direct (3) vs. indirect (4) P/D motion
