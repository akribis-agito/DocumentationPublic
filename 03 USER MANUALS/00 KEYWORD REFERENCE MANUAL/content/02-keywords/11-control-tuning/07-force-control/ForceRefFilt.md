---
keyword: ForceRefFilt
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 586
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 1
  - 500000
  default: 10000
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceRefFilt

Cut-off frequency of the force-command reference filter.

## Overview

`ForceRefFilt` defines the cut-off frequency of the first-order low-pass filter applied to the force command, expressed in **Hz/100** (the value is the cut-off frequency in hertz multiplied by 100). The filtered result is the force reference [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md) used by the force loop and reported as [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md).

For example, a 500 Hz cut-off is set as `ForceRefFilt = 50000`.

Value range is `1` to `500000` (0.01 Hz to 5000 Hz); the default is `10000` (100 Hz). The keyword is stored in flash. The filter is only active when [ForceRefFOn](ForceRefFOn.md) = 1.

## How it works

Each control cycle the raw force command (from the selected command source) is passed through the first-order low-pass section to produce [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md):

$$
\text{ForceRef} = a \cdot \text{command} + (1 - a) \cdot \text{ForceRef}_{\text{prev}}
$$

When the filter is enabled ([ForceRefFOn](ForceRefFOn.md) = 1), the coefficient is derived from the cut-off frequency and the controller sample time:

$$
a = 1 - e^{-2\pi \, T_s \, \frac{\text{ForceRefFilt}}{100}}
$$

where $T_s$ is the controller sample time. A higher `ForceRefFilt` gives a higher cut-off and a faster reference response; a lower value smooths the command more. When the filter is disabled (`ForceRefFOn = 0`) the coefficient is forced to $a = 1$, so `ForceRef` equals the raw command unfiltered.

Writing `ForceRefFilt` recomputes the coefficient immediately. The same reference filter is used in both force-control structures selected by [ForcePIVOn](ForcePIVOn.md).

## Examples

```text
AForceRefFOn[1]=1       ; enable the force-command reference filter
AForceRefFilt[1]=50000  ; cut-off 500 Hz (Hz/100)
AForceRefFilt[1]        ; read the cut-off setting
```

## See also

- [ForceRefFOn](ForceRefFOn.md) — enables/bypasses this reference filter
- [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md) — filtered force reference produced by this filter
- [Force control](00-overview.md) — force-loop structure overview
