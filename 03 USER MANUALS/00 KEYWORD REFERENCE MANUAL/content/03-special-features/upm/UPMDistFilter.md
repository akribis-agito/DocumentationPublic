# UPMDistFilter

**Definition:**

UPMDistFilter sets the cutoff frequency, in Hz, of the low-pass filter applied to the measured acceleration signal used by the UPM disturbance rejection loop, smoothing that feedback to prevent noise amplification. The filter is a second-order low-pass with a fixed damping of 0.8. Its range is 300 to 3000 with a default of 1000. It cannot be changed while the axis is in motion or with the motor on. It is an axis-related parameter saved to flash.

**See also:**

[UPMDistOn](UPMDistOn.md), [UPMDistReject](UPMDistReject.md), [UPMDistSystem](UPMDistSystem.md)
