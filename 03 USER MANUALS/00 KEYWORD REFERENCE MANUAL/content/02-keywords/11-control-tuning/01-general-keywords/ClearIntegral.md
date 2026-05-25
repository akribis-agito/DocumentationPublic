# ClearIntegral

**Definition:**

ClearIntegral is a command that zeroes the integrator state of the position and velocity control loops. It is used to eliminate any accumulated integral wind-up, typically before enabling the motor or after a large position disturbance. It is an axis-related command function that cannot be issued while the axis is in motion.

**See also:**

[PosKi](../03-position-control/PosKi.md), [VelKi](../04-velocity-control/VelKi.md)
