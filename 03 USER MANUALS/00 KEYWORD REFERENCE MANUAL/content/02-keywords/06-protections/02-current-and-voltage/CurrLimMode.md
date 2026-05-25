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
