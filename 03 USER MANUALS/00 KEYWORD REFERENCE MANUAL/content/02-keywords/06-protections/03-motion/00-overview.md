# Motion

Motion protection prevents possible damage to the stage/motor even if current/voltage protection is not triggered. The following is the list of motion protection mechanisms.

| No. | Protection mechanisms |
|---|---|
| 1 | **Position limit protection** FwdPLim and RevPLim specify the forward and reverse software travel limit, respectively. LimitsStat specifies the status of hardware limit switch. |
| 2 | **Kinematics protection** MaxVel and MaxAcc specify the maximum absolute values of velocity and acceleration, respectively. |
| 3 | **Kinematics error protection** MaxPosErr and MaxVelErr specify the maximum position and velocity errors, respectively, while the axis is in closed-loop condition. MaxPosErrOL and MaxVelErrOL specify the same things, but with axis is open-loop condition. |
| 4 | **Stuck protection** StuckCurr, StuckVel, StuckTime specify the conditions for which a motor is considered stuck. |
| 5 | **Dual-loop protection** **Condition:** This feature is only applicable when dual-loop control is enabled (DualLoopOn is non-zero, or GantryDLoopOn is non-zero). In dual-loop conditions, the velocity difference of both feedback sources must not exceed DualStuckVel for DualStuckTime. This will protect against the case where one or both feedback sources returning abnormal values. |
| 6 | **Stalling protection** |
