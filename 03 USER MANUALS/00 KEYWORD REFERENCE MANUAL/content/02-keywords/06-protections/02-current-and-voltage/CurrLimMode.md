---
keyword: CurrLimMode
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 392
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
  - 0
  - 3
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrLimMode

**Definition:**

CurrLimMode defines the current command (CurrRef) saturation limits.

| Value | Limitation based on | Allowable CurrRef range \[mA\] |
|----|----|----|
| 0 | PeakCL (using absolute value) | \[-PeakCL, PeakCL\] |
| 1 | 2 analog inputs (using absolute values) | \[-AInPort\[q\], AInPort\[p\]\] |
| 2 | 1 analog input (using absolute value) | \[-AInPort\[p\], AInPort\[p\]\] |
| 3 | CurrLimFwd, CurrLimRev (using absolute value) | \[-CurrLimRev, CurrLimFwd\] |

<span class="mark">If CurrLimMode=1, the current command will take the positive limitation from AInPort\[p\] of which AInMode\[p\]=8. Similarly, the negative limitation is taken from AInPort\[q\] of which AinPort\[q\]=7.</span>
<span class="mark">If CurrLimMode=2, the current command will take the positive and negative limitation from AInPort\[p\] of which AInMode\[p\]=8.</span>
