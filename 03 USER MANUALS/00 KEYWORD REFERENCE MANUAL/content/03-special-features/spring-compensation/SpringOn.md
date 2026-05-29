# SpringOn

**Definition:**

SpringOn enables the spring compensation feature, which injects a position-dependent feedforward current into the control loop to counteract elastic restoring forces acting on the load. It is an axis-related parameter and is not saved to flash; it can be changed at any time.

SpringOn accepts the values 0 to 2 and defaults to 0. The compensation is gated on a simple nonzero test, so any nonzero value (1 or 2) enables it identically; there is no difference in behavior between the two enabled values. Because the parameter is not saved to flash, it reverts to 0 (disabled) at power-up and must be set again to re-enable. It may be changed while the axis is in motion.

**See also:**

[SpringPLow](SpringPLow.md), [SpringPHigh](SpringPHigh.md), [SpringTable](SpringTable.md), [SpringPosFFW](SpringPosFFW.md)
