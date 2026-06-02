# SpringPHigh

**Definition:**

SpringPHigh sets the upper position boundary, in user units, of the spring compensation region. Spring compensation is applied only while the position reference is within the band [SpringPLow](SpringPLow.md) to SpringPHigh; above SpringPHigh no spring current is added. It is an axis-related parameter saved to flash and can be changed at any time.

The default is 10000 user units. The band test compares the shaped, filtered position reference (the commanded profile, not the measured feedback position) against [SpringPLow](SpringPLow.md) and SpringPHigh, with both endpoints included. The boundaries are not range-checked against each other: if SpringPHigh is set below SpringPLow the band is empty and no spring compensation is ever applied.

**See also:**

[SpringPLow](SpringPLow.md), [SpringOn](SpringOn.md), [SpringTable](SpringTable.md), [SpringTableGp](SpringTableGp.md)
