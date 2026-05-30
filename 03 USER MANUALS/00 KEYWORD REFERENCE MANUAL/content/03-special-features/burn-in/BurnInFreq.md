# BurnInFreq

**Definition:**

BurnInFreq sets the electrical rotation (commutation) frequency of the burn-in motion in units of 0.01 Hz (for example, 1000 = 10 Hz). The range is 1 (0.01 Hz) to 100000 (1000 Hz); the default is 1000 (10 Hz). It cannot be changed while the axis is in motion; it can be changed with the motor on. It is an axis-related parameter saved to flash.

During burn-in, the controller rotates the motor's electrical (commutation) angle open-loop at this frequency, completing `BurnInFreq` x 0.01 electrical revolutions per second (for example, `1000` = 10 electrical Hz). This rate is independent of the control sample rate. On a rotary brushless motor the resulting mechanical shaft speed equals the electrical frequency divided by the number of pole pairs: shaft rev/s = (`BurnInFreq` x 0.01) / [PolePrs](../../02-keywords/02-motor-and-amplifier/PolePrs.md).

**See also:**

[BurnInMode](BurnInMode.md)
