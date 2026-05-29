# FrictionComp

Friction compensation is activated when the user variable `FrictionComp` is non-zero. This parameter always takes positive values.

When motion starts (via the `Begin` command), the friction-compensation flag is set. As soon as the motion begins and that flag is set, this value is used to seed (set) the velocity-loop integral, after which the flag is cleared. The sign follows the direction of the commanded (profiler) velocity.

- A positive value is applied when the commanded motion is in the positive direction.
- A negative value is applied when the commanded motion is in the negative direction.

`FrictionComp` is in milliamps (mA).

**Note:**

This function is valid only for motion modes driven by the velocity profiler.
