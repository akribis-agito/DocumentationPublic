---
keyword: PDPosFilt
summary: First-order low-pass cut-off frequency (Hz/100) smoothing PDPos in direct P/D mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`PDPosFilt` is the user-facing, cut-off-frequency form of the direct-mode P/D filter. It replaces the older approach of typing the filter coefficient directly: writing `PDPosFilt` causes the controller to compute the internal coefficient [PDFiltFact](PDFiltFact.md) automatically.

## How it works

The value is expressed in units of Hz × 100. A required cut-off frequency of 250 Hz means `PDPosFilt = 25000`; the default `12800` is 128 Hz.

When `PDPosFilt` is written, the special function `SpPDPosFilt` (`SpecialFuncs.c:5054`) converts the frequency into the integer filter coefficient `PDFiltFact` (range 1–64) used by the direct-mode reference update (`AG300_CTL01Profiler.c:1251`), using a backward-Euler discretisation of the continuous low-pass `w / (s + w)`:

$$
\text{PDFiltFact} = 64 \cdot \frac{2\pi\,T_s\,\text{PDPosFilt}}{100 + 2\pi\,T_s\,\text{PDPosFilt}}
$$

where `Ts` is the control sample time and `w = 2π·(PDPosFilt/100)`. The minimum value (4150 in the firmware) is the smallest frequency that keeps the computed `PDFiltFact` from rounding down to 0 (which would freeze the reference). A **higher** `PDPosFilt` means a faster filter (less smoothing, `PosRef` tracks the pulse stream more closely); a **lower** value means heavier smoothing.

The filter applies only in **direct** P/D motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 3); indirect P/D motion uses the second-order profile generator and has no such filter.

## Examples

```text
APDPosFilt=25000     ; 250 Hz cut-off frequency (faster, less smoothing)
APDPosFilt=12800     ; 128 Hz cut-off frequency (default)
APDPosFilt=4150      ; minimum (heaviest smoothing)
```

## See also

- [PDFiltFact](PDFiltFact.md) — the internal coefficient this frequency is converted into
- [PDPos](PDPos.md) — counter whose change is filtered into `PosRef`
- [MotionMode](../02-motion-configuration/MotionMode.md) — selects direct (3) vs. indirect (4) P/D motion
