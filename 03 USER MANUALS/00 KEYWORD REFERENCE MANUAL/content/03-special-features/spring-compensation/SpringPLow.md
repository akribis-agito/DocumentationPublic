# SpringPLow

**Definition:**

SpringPLow sets the lower position boundary, in user units, of the spring compensation region. Spring compensation is applied only while the position reference is within the band SpringPLow to [SpringPHigh](SpringPHigh.md); below SpringPLow no spring current is added. SpringPLow also serves as the reference point for the position-proportional term scaled by [SpringPosFFW](SpringPosFFW.md): that term is zero at SpringPLow and grows as the reference moves above it. It is an axis-related parameter saved to flash and can be changed at any time.

The default is -10000 user units. The band test compares the shaped, filtered position reference (the commanded profile, not the measured feedback position) against SpringPLow and [SpringPHigh](SpringPHigh.md). There is no hysteresis: when the reference leaves the band the entire spring contribution (both the position-proportional [SpringPosFFW](SpringPosFFW.md) term and the constant [SpringCurrFFW](SpringCurrFFW.md) bias) is removed at once, rather than being held or clamped at the band edges.

**See also:**

[SpringPHigh](SpringPHigh.md), [SpringOn](SpringOn.md), [SpringTable](SpringTable.md), [SpringTableGp](SpringTableGp.md)
