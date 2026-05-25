# BuffCalc

**Definition:**

BuffCalc is a command that pre-computes the spline coefficients from the waypoint data in BuffPos and BuffTime before motion begins. It must be called after loading the waypoint arrays and before issuing a Begin command in spline buffer mode. It is an axis-related command function that cannot be issued while the axis is in motion.

**See also:**

[BuffPos](BuffPos.md), [BuffTime](BuffTime.md), [BuffSplineMod](BuffSplineMod.md), [BuffStatus](BuffStatus.md)
