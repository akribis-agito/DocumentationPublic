# Motor and amplifier

**Overview:**

To set up an axis, user needs to provide amplifier and motor information. Depending on the type of amplifier and motor, additional keywords have to be configured.

[AmpType](AmpType.md) selects the drive mode (built-in amplifier or external), while [MotorType](MotorType.md) selects how the motor is commutated. Together with the pole pairs ([PolePrs](PolePrs.md)), encoder resolution, and stepping settings ([StepBits](StepBits.md)), these feed the commutation and current-generation stage, whose phase-current references are scaled by the full-scale settings ([AAmpFullScale](AAmpFullScale.md), [LAmpFullScale](LAmpFullScale.md)) before reaching the power stage.

![Motor and amplifier interface: AmpType sets the drive mode and MotorType sets commutation; with pole pairs, encoder resolution and stepping settings they feed commutation and current generation, which scales phase-current references by the full-scale settings and sends them to the power stage that drives the motor windings](motor-amplifier-interface.svg)

The following table shows the summary of motor and amplifier keywords.

| No. | Keywords                                                                   | Summary                                                   |
| --- | -------------------------------------------------------------------------- | --------------------------------------------------------- |
| 1   | [AAmpFullScale](../../02-keywords/02-motor-and-amplifier/AAmpFullScale.md) | Full-scale output value for external amplifier            |
| 2   | [AmpType](../../02-keywords/02-motor-and-amplifier/AmpType.md)             | Axis amplifier mode                                       |
| 3   | [LAmpFullScale](../../02-keywords/02-motor-and-amplifier/LAmpFullScale.md) | Full-scale output selection for built-in linear amplifier |
| 4   | [MagneticPitch](../../02-keywords/02-motor-and-amplifier/MagneticPitch.md) | Linear-motor magnetic pitch in millimetres                |
| 5   | [MotorType](../../02-keywords/02-motor-and-amplifier/MotorType.md)         | Axis motor type                                           |
| 6   | [PolePrs](../../02-keywords/02-motor-and-amplifier/PolePrs.md)             | Number of pole pairs of the motor                         |
| 7   | [StepBits](../../02-keywords/02-motor-and-amplifier/StepBits.md)           | Number of stepping bits per electrical cycle              |
| 8   | [StepInMotCurr](../../02-keywords/02-motor-and-amplifier/StepInMotCurr.md) | Stepper phase current used in motion                      |
| 9   | [StepInPosCurr](../../02-keywords/02-motor-and-amplifier/StepInPosCurr.md) | Stepper phase current used in standstill                  |
