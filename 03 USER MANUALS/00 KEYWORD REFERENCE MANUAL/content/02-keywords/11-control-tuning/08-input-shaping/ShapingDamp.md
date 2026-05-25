# ShapingDamp

**Definition:**

ShapingDamp is an array that stores the damping ratios for each resonance mode defined in ShapingFreq. Each element is the damping ratio (0 to 1) of the corresponding frequency, used by the input shaper to compute the impulse amplitudes. It is an axis-related array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[ShapingOn](ShapingOn.md), [ShapingFreq](ShapingFreq.md)
