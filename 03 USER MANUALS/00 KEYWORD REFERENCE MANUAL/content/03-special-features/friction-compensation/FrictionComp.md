# FrictionComp

Friction compensation is activated when the user variable `FrictionComp` is non-zero. This parameter always takes positive values.

When motion starts (via the `Begin` command), the friction-compensation flag is set. As soon as the motion begins and that flag is set, this value is used to seed (set) the velocity-loop integral, after which the flag is cleared. The seed is applied once per motion: the flag is cleared immediately after the single assignment, so normal velocity-loop integration resumes from the seeded value for the remainder of the move. For a repetitive move, the flag is re-armed before each repetition, so the integral is re-seeded at the start of every repeat.

The sign of the seed follows the direction of the commanded (profiler) velocity, using a strict boundary on the profiler velocity at the instant of seeding:

- A positive value (`+FrictionComp`) is applied when the profiler velocity is strictly greater than zero (positive direction).
- A negative value (`-FrictionComp`) is applied when the profiler velocity is zero or negative.

`FrictionComp` is in milliamps (mA) and maps one-to-one to the resulting velocity-loop current contribution: seeding the integral with `FrictionComp` produces a current contribution of `FrictionComp` mA. The keyword accepts values from 0 to 5000 mA, with a default of 0.

Friction compensation is applied only while `FrictionComp` is non-zero. A value of 0 does not overwrite the integrator at motion start, so on an unbalanced or gravity-loaded axis the standing (holding) current already in the integral is preserved rather than being reset to zero.

**Note:**

This function is valid only for motion modes driven by the velocity profiler.
