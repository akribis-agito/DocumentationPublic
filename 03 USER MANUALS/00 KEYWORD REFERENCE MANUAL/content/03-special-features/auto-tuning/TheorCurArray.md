# TheorCurArray

**Definition:**

TheorCurArray is an array parameter that stores the theoretical current-loop response used by the automatic current-loop PI tuning as a reference for computing the cost function. It holds the expected current step-response waveform that the recorded motor-current response is compared against; the firmware only reads it, so the reference points must be supplied by the host. The array holds up to 308 entries (indexes [1] to [308]). It is an axis-related array parameter saved to flash and can be changed at any time, including while the axis is in motion and with the motor on.

**See also:**

[CostFunction](CostFunction.md)
