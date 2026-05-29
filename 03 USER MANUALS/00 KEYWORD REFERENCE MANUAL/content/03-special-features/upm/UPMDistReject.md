# UPMDistReject

**Definition:**

UPMDistReject sets the rejection gain of the UPM disturbance rejection loop, controlling how aggressively the estimated disturbance is cancelled. Its range is 100 to 2000 with a default of 1000. It is an axis-related parameter saved to flash and can be changed at any time, including in motion and with the motor on.

When UPMDistOn is enabled, the controller runs a continuous (every control cycle) integrating disturbance-observer loop: it forms the difference between the acceleration expected from the commanded current (the current reference scaled by the plant gain UPMDistSystem) and the measured acceleration, low-pass filtered per UPMDistFilter, multiplies that difference by the effective gain set here, and integrates it; the integrator output becomes the new current reference. The effective integrator gain scales directly with UPMDistReject and inversely with UPMDistSystem, so a larger UPMDistReject rejects the disturbance more aggressively while a larger UPMDistSystem reduces it. The loop acts continuously on the estimated disturbance and is not specific to periodic disturbances.

**See also:**

[UPMDistOn](UPMDistOn.md), [UPMDistSystem](UPMDistSystem.md), [UPMDistFilter](UPMDistFilter.md)
