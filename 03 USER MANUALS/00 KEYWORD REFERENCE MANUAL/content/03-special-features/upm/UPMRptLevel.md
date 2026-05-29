# UPMRptLevel

**Definition:**

UPMRptLevel sets the convergence level or learning gain for the UPM repetitive compensation algorithm, controlling how quickly the correction table converges to the steady-state error pattern. It cannot be changed while the axis is in motion or with the motor on. It is an axis-related parameter saved to flash.

> **Version note:** This is the v4 name for this parameter. In v5 the same parameter was renamed [UPMRptRange](UPMRptRange.md) and is expressed as a frequency range in Hz. They are the same underlying parameter — use `UPMRptLevel` on v4 controllers and `UPMRptRange` on v5 controllers.

**See also:**

[UPMRptRange](UPMRptRange.md), [UPMRptOn](UPMRptOn.md), [UPMRptCalc](UPMRptCalc.md), [UPMRptState](UPMRptState.md)
