# Kinematics configuration

Kinematics configuration shapes the velocity profile of a move. Most of these keywords can be set before and during motion, as the motion profile is calculated on-the-fly. The trajectory profiler ramps the axis up to the cruise speed at the acceleration rate, holds it, then brakes at the deceleration rate; the jerk settings round the corners to soften the start and end of the move.

![Velocity profile: trapezoid versus S-curve](velocity-profile.svg)

Below are the keywords related to motion kinematics.

| No. | Keyword | Summary |
|-----|---------|---------|
| 1 | [Accel](Accel.md) | Acceleration rate for the move (leading slope of the profile). |
| 2 | [Decel](Decel.md) | Deceleration rate for the move (trailing slope of the profile). |
| 3 | [Speed](Speed.md) | Cruise (target) velocity the profiler ramps toward. |
| 4 | [AccelFact](AccelFact.md) | Integer multiplier applied to both `Accel` and `Decel`. |
| 5 | [EmrgDec](EmrgDec.md) | Emergency deceleration rate used on limit / controlled-stop reasons. |
| 6 | [Jerk](Jerk.md) | Second-order S-curve smoothing window (`2^Jerk` cycles). |
| 7 | [JerkInAcc](JerkInAcc.md) | Jerk limit during the acceleration phase (third-order profile). |
| 8 | [JerkInDec](JerkInDec.md) | Jerk limit during the deceleration phase (third-order profile). |
| 9 | [JerkMode](JerkMode.md) | Selects the profiler order (see motion configuration). |
| 10 | [AccShapeOn](AccShapeOn.md) | Enables distance-to-target acceleration shaping. |
| 11 | [AccShapeDist](AccShapeDist.md) | Per-segment distance thresholds for acceleration shaping. |
| 12 | [AccShapeFact](AccShapeFact.md) | Per-segment acceleration scaling factors for acceleration shaping. |
| 13 | [SpeedChgOn](SpeedChgOn.md) | Enables a position-triggered speed change on the fly. |
| 14 | [SpeedChgPos](SpeedChgPos.md) | Position at which the speed change is triggered. |
| 15 | [SpeedChgNew](SpeedChgNew.md) | New speed applied at the trigger. |
| 16 | [SpeedChgDir](SpeedChgDir.md) | Direction in which the trigger is active. |
| 17 | [RefOffsetSamp](RefOffsetSamp.md) | Number of servo samples over which a reference offset is ramped in. |
| 18 | [RefOffsetStep](RefOffsetStep.md) | Per-sample magnitude of the reference offset. |
| 19 | [SetPosition](SetPosition.md) | Redefines the axis position without moving the motor. |
| 20 | [ZeroPosErr](ZeroPosErr.md) | Zeroes the position error by snapping the reference to the feedback. |

The point-to-point targets [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) and [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) are described under Motion mode – Point to point.
