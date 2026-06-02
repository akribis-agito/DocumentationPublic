# AutoGDownSm

**Definition:**

AutoGDownSm sets the downsampling exponent applied to the motion data collected during auto-gain identification. The actual downsampling factor is 2 raised to this value, so the effective sample time is multiplied by that factor (for example, a value of 4 downsamples by a factor of 16). Increasing it reduces computation load at the cost of frequency resolution. It cannot be changed while the axis is in motion or with the motor on. It is an axis-related parameter saved to flash.

**See also:**

[AutoGOn](AutoGOn.md), [AutoGPosFilt](AutoGPosFilt.md), [AutoGMinLen](AutoGMinLen.md)
