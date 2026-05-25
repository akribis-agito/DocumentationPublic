# DualStuckTime

**Definition:**

DualStuckTime specifies the maximum number of consecutive controller cycles (1 cycle ≈ 61µs) of which the difference between the two feedback in dual-loop can be more than DualStuckVel.

If DualStuckVel is exceeded for consecutive controller cycle number of DualStuckTime, axis will be disabled, and error message will be thrown.
