# ShapingOn

**Definition:**

ShapingOn enables or disables the input shaping (command filtering) feature on the axis. When set to a non-zero value, the motion reference is convolved with an impulse sequence defined by ShapingFreq and ShapingDamp to suppress resonant vibration. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[ShapingFreq](ShapingFreq.md), [ShapingDamp](ShapingDamp.md)
