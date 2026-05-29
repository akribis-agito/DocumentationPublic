# UPMDistOn

**Definition:**

UPMDistOn enables the UPM disturbance rejection function. When active, the controller runs a disturbance-observer-style acceleration-feedback loop: it compares the acceleration expected from the commanded current (scaled by the plant gain UPMDistSystem) against the measured acceleration, then integrates the difference and adds the result back into the current reference to reject the estimated disturbance. UPMDistOn is a 0/1 enable. It is an axis-related parameter and is not saved to flash; it can be changed at any time.

**See also:**

[UPMDistSystem](UPMDistSystem.md), [UPMDistReject](UPMDistReject.md), [UPMDistFilter](UPMDistFilter.md), [UPMVelOn](UPMVelOn.md)
