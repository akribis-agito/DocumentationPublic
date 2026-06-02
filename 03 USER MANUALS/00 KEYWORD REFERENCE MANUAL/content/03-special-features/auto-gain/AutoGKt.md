# AutoGKt

**Definition:**

AutoGKt stores the motor torque constant (Kt) used by the automatic gain tuning algorithm to relate current command to force or torque when computing bandwidth-based gains. It works together with the motor inertia value in AutoGJm to estimate the load-to-motor inertia ratio. The valid range is 1 to 2147483647, with a default of 38231. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGBW](AutoGBW.md), [AutoGJm](AutoGJm.md), [AutoGOn](AutoGOn.md)
