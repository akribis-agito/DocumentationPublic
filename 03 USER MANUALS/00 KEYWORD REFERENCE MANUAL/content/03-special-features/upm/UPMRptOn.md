# UPMRptOn

**Definition:**

UPMRptOn requests UPM repetitive (periodic) motion compensation for the next motion. When active, the controller adapts a feedforward correction to cancel position errors that repeat with each motion cycle. The request has three values: 0 = none, 1 = first (capture a single learning pass), and 2 = repetitive (apply repetitive compensation). The request is consumed at the start of the next motion: the controller sets the corresponding repetitive state and then clears UPMRptOn back to 0, so it must be set again before each motion that should use the feature. It cannot be changed while the axis is in motion; it can be changed with the motor on. It is an axis-related parameter and is not saved to flash.

**See also:**

[UPMRptCalc](UPMRptCalc.md), [UPMRptLevel](UPMRptLevel.md), [UPMRptState](UPMRptState.md), [UPMRptTime](UPMRptTime.md)
