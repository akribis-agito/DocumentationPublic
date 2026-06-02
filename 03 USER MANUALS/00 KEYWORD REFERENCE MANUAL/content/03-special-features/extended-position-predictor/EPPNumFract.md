# EPPNumFract

**Definition:**

EPPNumFract sets the fractional part of a numerator tap of the Extended Position Predictor transfer function, forming the numerator polynomial together with [EPPNumInteg]. Each tap is assembled as EPPNumInteg[k] + EPPNumFract[k]/65536, so EPPNumFract carries the 1/65536 fractional weight. Like EPPNumInteg, it is a read/write array indexed 1..[EPPFiltLength] (1-indexed) and is stored to flash.

**See also:**

[EPPNumInteg](EPPNumInteg.md), [EPPNumFactor](EPPNumFactor.md), [EPPDenFract](EPPDenFract.md)
