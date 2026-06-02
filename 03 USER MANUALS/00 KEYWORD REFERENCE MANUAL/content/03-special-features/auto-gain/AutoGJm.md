# AutoGJm

**Definition:**

AutoGJm holds the motor inertia value that you supply to the automatic gain tuning algorithm. Together with the motor torque constant set in AutoGKt, it is used to estimate the load-to-motor inertia ratio and to compute the velocity and position gains. The estimated ratio is reported through the auto-gain status, not through AutoGJratUs (which is itself a user-supplied input). It is a setup input to the algorithm, not a value the algorithm identifies. The valid range is 1 to 2147483647, with a default of 3993. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGBW](AutoGBW.md), [AutoGKt](AutoGKt.md), [AutoGJratUs](AutoGJratUs.md), [AutoGOn](AutoGOn.md)
