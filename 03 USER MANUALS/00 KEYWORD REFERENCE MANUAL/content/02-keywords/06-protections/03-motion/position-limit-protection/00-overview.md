# Position limit protection

Agito supports both hardware and software position limits.

Software limits define the allowed range of motion. If a move command has target position outside of the software limits, it will be rejected and logged in [ErrLog](../../../../02-keywords/07-status-and-faults/ErrLog.md).

While in motion, the distance to safely decelerate and stop without exceeding the software limit is continuously checked for. If the axis is approaching the limits, in jog mode for example, the profiler decelerates and brings the axis to a stop at the limit position. The stop reason will be indicated in [MotionReason](../../../../02-keywords/10-motion/05-motion-status/MotionReason.md).

Hardware limits are external signals that indicate when an axis is at the end of the stroke. The configuration of limit sensors is done via [DInMode](../../../../02-keywords/05-inputs-outputs/04-digital-inputs/DInMode.md). [LimitsStat](LimitsStat.md) reflects the statuses (triggered/not triggered) of the limit sensors. While a hardware position limit sensor is triggered, motion command in the direction of the limit is rejected as command/message error, and the error code is indicated in ErrLog.

While in motion, the statuses of the limit sensors are continuously checked for. If the limit in the direction of motion is triggered, the profiler decelerates and bring the axis to a stop. The stop reason will be indicated in MotionReason.
