# Vel

**Definition:**

Vel is an array that reports the feedback velocities.

Vel\[1\] is used for velocity loop feedback in non-gantry mode. Therefore, its definition will change depending on gantry mode and dual-loop condition.

Each array element is Vel is described below.

**Note:**

1. Vertical lines denote the controller sampling time instances.
2. The gap is 1 ( O n e O v e r T G a p = 0 ) and polling frequency is 300MHz ( O n e O v e r T F r e q = 0) .
3. Vel[4] = 0 in the zeroth control cycle/interrupt.
4. In between zeroth and first control interrupts, hardware records change of 1 count in 12000 polling cycles and saves this value. On the first control interrupt, controller reads this value from hardware and calculate Vel[4].
5. In between second and third control interrupts, hardware updates twice as 1 position count change happens twice. First updated value is 7200 polling counts. Second updated value is 4800 polling counts.
6. First updated value is 7200 polling counts.
7. Second updated value is 4800 polling counts.

Please refer to [Control tuning – Dual-loop control](../../../02-keywords/11-control-tuning/02-dual-loop-control/00-overview.md) for more information about the type of dual-loop control.
