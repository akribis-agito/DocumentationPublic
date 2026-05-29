# MotorLearnMod

**Definition:**

MotorLearnMod selects the mode used by the motor-learning routine, which drives the motor open-loop to measure the number of pole pairs and the encoder resolution. It cannot be changed while the axis is in motion; it can be changed with the motor on. It is an axis-related parameter and is not saved to flash.

| Value | Meaning |
|---|---|
| 0 | Automatic |
| 1 | Manual (manually find the number of pole pairs) |

**See also:**

[MotorLearnOn](MotorLearnOn.md), [MotorLearnInc](MotorLearnInc.md), [MotorLearnPl](MotorLearnPl.md)
