# UPMRptState

**Definition:**

UPMRptState is a read-only parameter that reports the current operational state of the UPM repetitive compensation function. It cannot be changed while the axis is in motion; it can be changed with the motor on. It is an axis-related status variable and is not saved to flash.

The reported values are:

| Value | State | Meaning |
|-------|-------|---------|
| 0 | Idle | Repetitive compensation is not active (UPMRptOn is off, or the current motion has ended). This is the default. |
| 1 | Active, first cycle | UPMRptOn is set to 1 and a motion has started; the controller is recording the error of the first cycle. |
| 2 | Active, repetitive | UPMRptOn is set to 2 and a motion has started; the controller is replaying and adapting the learned correction over repeating cycles. |

The state is set to 1 or 2 at the start of a motion according to UPMRptOn, and returns to 0 (Idle) when that motion ends: for the first-cycle case after the recording tail set by UPMRptTime expires, when the playback index reaches the recorded cycle length, when the recording reaches the storage-array limit, or when the motor is turned off. UPMRptState reflects only this run state; it is not changed by UPMCalcCoeff or UPMRptCalc, and there is no separate "converged" or "error" state. The keyword's reported range is 0 to 4, but only the values 0, 1, and 2 occur in operation.

**See also:**

[UPMRptOn](UPMRptOn.md), [UPMRptCalc](UPMRptCalc.md), [UPMRptLevel](UPMRptLevel.md)
