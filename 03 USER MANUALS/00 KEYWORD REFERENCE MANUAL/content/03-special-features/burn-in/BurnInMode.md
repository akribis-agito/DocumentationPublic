# BurnInMode

**Definition:**

BurnInMode selects the operating mode of the burn-in motion function, which drives the axis in a repetitive pattern to stress-test the system over extended periods. It cannot be changed while the axis is in motion or with the motor on. It is an axis-related parameter and is not saved to flash.

Burn-in motion drives an open-loop commutation angle only on brushless motor types ([MotorType](../../02-keywords/02-motor-and-amplifier/MotorType.md) configured as brushless). For brush/DC, voice-coil, stepper, and simulation types the burn-in function drives no commutation angle.

**See also:**

[BurnInFreq](BurnInFreq.md)
