# MotionStat

**Definition:**

MotionStat reports the detailed status of the current motion. Each bit represents a specific motion state, and multiple bits can be set at the same time. When the motor is not in motion, MotionStat = 0.

The following table describes MotionStat bits.

| MotionStat, bit \# | Motion state if bit is set (= 1). If bit is cleared (= 0), it represents otherwise. |
|----|----|
| 0 | Axis is in motion. |
| 1 | Axis is dwelling (only for point-to-point repetitive motion). See [RptWait](../../../02-keywords/10-motion/02-motion-configuration/RptWait.md) and [MotionMode](../../../02-keywords/10-motion/02-motion-configuration/MotionMode.md) for more information. |
| 2 | Axis is ending its point-to-point repetitive motion (following [StopRep](../../../02-keywords/10-motion/04-motion-command/StopRep.md) command). |
| 3 | [Stop](../../../02-keywords/10-motion/04-motion-command/Stop.md) command is requested. |
| 4 | Axis is accelerating. |
| 5 | Axis is decelerating. |
| 6 | Axis is in profile smoothing phase. See [Jerk](../../../02-keywords/10-motion/03-kinematics-configuration/Jerk.md) keyword. |
| 7 | Axis is in ECAM stop (following StopECAM command). |
| 8 | Axis is in FIFO stop (following StopFIFO command). |
| 9 | Axis is waiting for input (motion is suspended till the rising edge at user defined input). See [BeginDInOn](../../../02-keywords/10-motion/04-motion-command/BeginDInOn.md) for more information. |
| 10 | Axis is one of CNCA member axes. |
| 11 | Axis is now involved in CNCA motion. |
| 12 | Axis is ending its CNCA motion (following StopCNCA command). |
| 13 | Axis is one of CNCB member axes. |
| 14 | Axis is now involved in CNCB motion. |
| 15 | Axis is ending its CNCB motion (following StopCNCB command). |
| 16 | Controlled stop and motor off request due to fault condition is received (e.g. anomaly detection, fault from digital input, etc.). |
| 17 | Axis is ending its spline buffer motion (following StopBuff command). |
| 18 | Axis is ending its vector motion (following StopVec command). |
| 19 | Axis is one of the vector motion axes. |
| 20 | Axis is ending its jog motion as axis is approaching software limit. |
