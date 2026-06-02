# AutoGPosFilt

**Definition:**

AutoGPosFilt sets the cutoff frequency of the first-order low-pass filter used by the auto-gain identification algorithm. The same filter is applied to both the position and the current-command signals that the algorithm uses; changing this value recomputes the filter coefficients. A higher value gives a higher cutoff frequency. Range 1 to 1000; default 50. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGOn](AutoGOn.md), [AutoGAccTh](AutoGAccTh.md), [AutoGVelTh](AutoGVelTh.md)
