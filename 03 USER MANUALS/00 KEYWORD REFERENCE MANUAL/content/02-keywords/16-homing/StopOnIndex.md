# StopOnIndex

**Definition:**

StopOnIndex configures the encoder index pulse to automatically stop axis motion when detected. When set to a non-zero value, the next encoder index pulse causes the axis to halt, which is useful for homing procedures that reference the encoder index position. It is an axis-related parameter, not saved to flash, and can be changed at any time.

**See also:**

[StopOnHome](StopOnHome.md), [HomeStat](HomeStat.md)
