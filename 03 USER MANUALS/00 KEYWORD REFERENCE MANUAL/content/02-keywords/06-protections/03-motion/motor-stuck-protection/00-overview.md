# Motor stuck protection

Motor stuck protection works by comparing the current and velocity over a period of time. A stuck condition occurs when the velocity is less than a defined threshold, while the current is greater a defined threshold, over a defined period of time. If stuck condition occurs, the axis is disabled and the error code reported on ConFlt.

Criterion for stuck condition check:

- $abs(Vel\lbrack 3\rbrack)\  < \ StuckVel$, **and**

- $abs(MotorCurr)\  > \ StuckCurr$

for StuckTime.

This means that the axis is exerting force but not moving. The check is done over a period of time to ensure that the stuck condition persists, and to prevent false detection during acceleration or deceleration.
