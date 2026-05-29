# UPMDistSystem

**Definition:**

UPMDistSystem sets the scalar plant-gain estimate used by the UPM disturbance rejection algorithm. The controller multiplies the commanded current by this gain to predict the expected acceleration; it also scales the rejection strength inversely with this value. Its range is 1 to 100000000, with a default of 1000. It cannot be changed while the axis is in motion or with the motor on. It is an axis-related parameter saved to flash.

**See also:**

[UPMDistOn](UPMDistOn.md), [UPMDistReject](UPMDistReject.md), [UPMDistFilter](UPMDistFilter.md)
