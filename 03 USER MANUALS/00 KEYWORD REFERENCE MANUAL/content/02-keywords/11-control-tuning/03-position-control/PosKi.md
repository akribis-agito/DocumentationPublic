# PosKi

**Definition:**

PosKi is the integral gain in position loop, applied onto the output of PosGain before entering integral block. The integral saturation value is controlled internally.

This keyword is applicable for gain scheduling. By default (no gain scheduling), the gain value of the first array element (PosKi\[1\]) is used for control. See [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md) for more information on which array elements are used, depending on gain scheduling method.
