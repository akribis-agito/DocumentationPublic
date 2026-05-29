# UPMRptMotion

**Definition:**

UPMRptMotion selects which learned-motion slot the UPM repetitive compensation function uses, choosing the stored feedforward correction table that matches the current motion. Its range is 0 to (number of learnable motions - 1); the number of available slots depends on the controller model. It cannot be changed while the axis is in motion; it can be changed with the motor on. It is an axis-related parameter and is not saved to flash.

**See also:**

[UPMRptOn](UPMRptOn.md), [UPMRptTime](UPMRptTime.md), [UPMRptCalc](UPMRptCalc.md)
