# MotorLearnRes

**Definition:**

MotorLearnRes is a read-only result reported after a motor-learning pass completes: the encoder resolution measured during the pass. For a rotary motor it is the encoder counts between two consecutive index (marker) pulses, i.e. the counts per mechanical revolution; the value is reported only after an automatic-mode pass finishes (MotorLearnSta = 3). For a linear motor it is the estimated resolution derived from the distance traveled over one electrical cycle. It is an axis-related status variable and is not saved to flash.

**See also:**

[MotorLearnOn](MotorLearnOn.md), [MotorLearnSta](MotorLearnSta.md), [MotorLearnPl](MotorLearnPl.md)
