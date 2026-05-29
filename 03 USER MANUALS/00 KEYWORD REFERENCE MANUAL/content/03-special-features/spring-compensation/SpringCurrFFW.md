# SpringCurrFFW

**Definition:**

SpringCurrFFW sets a constant, position-independent feedforward current, in microamps, that is added by the spring compensation. This bias current is applied whenever the position reference lies within the band defined by [SpringPLow](SpringPLow.md) and [SpringPHigh](SpringPHigh.md), and it does not vary with position; the position-proportional part of the spring compensation comes from [SpringPosFFW](SpringPosFFW.md). It is an axis-related parameter saved to flash and can be changed at any time.

The default is 0 (no constant bias). The allowed range spans from minus to plus the axis maximum current command (expressed in microamps, i.e. the maximum current command in mA scaled by 1000). The entered microamp value is scaled by 0.001 to convert it to milliamps before it is summed into the current reference, so it remains subject to the normal current and torque limits applied downstream.

**See also:**

[SpringOn](SpringOn.md), [SpringPosFFW](SpringPosFFW.md), [SpringTable](SpringTable.md)
