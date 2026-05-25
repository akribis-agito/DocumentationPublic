# BuffTime

**Definition:**

BuffTime is an array that stores the time duration (in servo samples) for each waypoint segment of the spline buffer. Together with BuffPos it defines the spline trajectory: the axis follows the position profile in BuffPos, spending BuffTime samples on each segment. It is an axis-related array, not saved to flash, and can be changed at any time.

**See also:**

[BuffPos](BuffPos.md), [BuffCalc](BuffCalc.md), [BuffStatus](BuffStatus.md)
