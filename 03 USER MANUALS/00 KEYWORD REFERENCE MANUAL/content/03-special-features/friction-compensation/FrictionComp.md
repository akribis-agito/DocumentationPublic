# FrictionComp

Friction compensation is activated when the user variable `FrictionComp` is non-zero. This parameter always takes positive values.

When motion starts (via the `Begin` command), a flag is set. Then, when `VelProfiler` is non-zero, this value is added to the velocity-control integral and the flag is cleared.

- A positive value is added if `VelProfiler` is positive.
- A negative value is added if `VelProfiler` is negative.

`FrictionComp` is in milliamps (mA).

**Note:**

This function is valid only for motion modes that use `VelProfiler`.
