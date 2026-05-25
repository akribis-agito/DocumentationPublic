# VelFFW

**Definition:**

VelFFW is the velocity feedforward gain applied onto the first derivative of position reference (dPosRef). The velocity feedforward is scaled before the final summation.

This keyword is applicable for gain scheduling. By default (no gain scheduling), the gain value of the first array element (VelFFW\[1\]) is used for control. See [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md) for more information on which array elements are used, depending on gain scheduling method.
