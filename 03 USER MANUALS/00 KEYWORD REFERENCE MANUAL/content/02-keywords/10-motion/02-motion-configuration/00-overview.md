# Motion configuration

Before commanding a move, the motion properties are configured. [MotionMode](MotionMode.md) selects what kind of motion runs when [Begin](../04-motion-command/Begin.md) is issued, and [JerkMode](JerkMode.md) selects the profiler order. For repetitive point-to-point motion the [RptMode](RptMode.md), [RptCycles](RptCycles.md) and [RptWait](RptWait.md) keywords control how the move repeats, as shown below.

![Repetitive point-to-point motion flow](repetition-flow.svg)

Below is the summary of all relevant keywords.

| No. | Keyword | Summary |
|-----|---------|---------|
| 1 | [MotionMode](MotionMode.md) | Selects the type of motion performed when `Begin` is issued. |
| 2 | [JerkMode](JerkMode.md) | Selects the point-to-point profiler order (second or third order). |
| 3 | [PTPKeepMoving](PTPKeepMoving.md) | Lets a new `Begin` blend into the existing move instead of stopping first. |
| 4 | [RptMode](RptMode.md) | Selects bidirectional or unidirectional repetitive motion. |
| 5 | [RptCycles](RptCycles.md) | Number of repetitions; `0` repeats indefinitely. |
| 6 | [RptWait](RptWait.md) | Dwell time, in milliseconds, between repetitions. |

The running repetition count is reported by [RptCounter](../05-motion-status/RptCounter.md) in the motion-status section.

## Shaping keywords versus limit keywords

Two groups of keywords interact with a move, and they have distinct roles:

- **Shaping keywords** — [Speed](../03-kinematics-configuration/Speed.md), [Accel](../03-kinematics-configuration/Accel.md) and [Decel](../03-kinematics-configuration/Decel.md) define the trajectory the profiler generates in the *profiled* (indirect) modes: the cruise velocity it ramps toward and the acceleration/deceleration slopes it plans. These are the only kinematic values the profiler itself uses to build the trajectory.
- **Limit keywords** — [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) and [MaxAcc](../../06-protections/03-motion/general-maximum-limits/MaxAcc.md) are protection ceilings. The profiler does **not** read them when generating the trajectory; they act in two separate places instead:
  - **At `Begin` (admission check).** [Begin](../04-motion-command/Begin.md) rejects an indirect move whose `Speed` exceeds `MaxVel` with error code 271, and on central-i v5 also rejects a jog or PTP-family move whose `Accel` or `Decel` exceeds `MaxAcc` with error code 324.
  - **In the velocity loop (continuous clamp).** Every control sample the velocity reference is hard-clamped to ±`MaxVel`; when it clamps, the velocity-saturation bit of [StatReg](../../07-status-and-faults/StatReg.md) (bit 23) is set. Because the clamped reference is the position-controller output plus velocity feedforward — not the raw profiled cruise speed — this clamp can engage even when `Speed` is at or below `MaxVel` (for example, on a large following error). Watch [StatReg](../../07-status-and-faults/StatReg.md) bit 23 and [VelRef](../01-kinematics-status/VelRef.md) to detect it.

The practical rule: keep `Speed` at or below `MaxVel` and (on v5) `Accel`/`Decel` at or below `MaxAcc` so the move passes the `Begin` admission check, and keep margin so the downstream velocity clamp does not engage during transients.
