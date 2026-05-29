# SpringPLow

**Definition:**

SpringPLow sets the lower position boundary, in user units, of the spring compensation region. Spring compensation is applied only while the position reference is within the band SpringPLow to [SpringPHigh](SpringPHigh.md); below SpringPLow no spring current is added. SpringPLow also serves as the reference point for the position-proportional term scaled by [SpringPosFFW](SpringPosFFW.md): that term is zero at SpringPLow and grows as the reference moves above it. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[SpringPHigh](SpringPHigh.md), [SpringOn](SpringOn.md), [SpringTable](SpringTable.md), [SpringTableGp](SpringTableGp.md)
