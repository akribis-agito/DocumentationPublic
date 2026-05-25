# JerkMode

**Condition:**

JerkMode is only used when MotionMode = 1 or 2 (point-to-point motion).

**Definition:**

JerkMode is used to define point-to-point motion profiler’s order, as shown below.

| JerkMode | Motion profiler’s order | Related keywords |
|----|----|----|
| 0 | 2 (Infinite jerk) | Speed, Accel, Decel, Jerk |
| 1 | 3 (Infinite snap) | Speed, Accel, Decel, Jerk, JerkInAcc, JerkInDec |
