# BuffPos

**Definition:**

BuffPos is an array that stores the waypoint positions in user units for the spline buffer motion profile. The controller uses these positions together with the time values in BuffTime to compute and execute a smooth spline trajectory. It is an axis-related array, not saved to flash, and can be changed at any time.

**See also:**

[BuffTime](BuffTime.md), [BuffCalc](BuffCalc.md), [BuffSplineMod](BuffSplineMod.md)
