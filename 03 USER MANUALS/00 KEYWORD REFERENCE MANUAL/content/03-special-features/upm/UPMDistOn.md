# UPMDistOn

**Definition:**

UPMDistOn enables the UPM disturbance rejection function. When active, the controller runs a disturbance-observer-style acceleration-feedback loop: it compares the acceleration expected from the commanded current (the current reference scaled by the plant gain UPMDistSystem) against the low-pass-filtered measured acceleration, then integrates the difference; the integrator output becomes the new current reference, rejecting the estimated disturbance. UPMDistOn is a 0/1 enable. It is an axis-related parameter and is not saved to flash; it can be changed at any time.

**See also:**

[UPMDistSystem](UPMDistSystem.md), [UPMDistReject](UPMDistReject.md), [UPMDistFilter](UPMDistFilter.md), [UPMVelOn](UPMVelOn.md)
