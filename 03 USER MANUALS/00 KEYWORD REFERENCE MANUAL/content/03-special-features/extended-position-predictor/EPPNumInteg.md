# EPPNumInteg

**Definition:**

EPPNumInteg holds the integer part of a numerator tap of the EPP lead/lag (LL) filter, the IIR filter that EPP applies to the position error [PosErr]. Each tap is assembled from two keywords: the integer part [EPPNumInteg] and the 1/65536 fractional part [EPPNumFract], combined as

$$\text{numerator}[k] = \texttt{EPPNumInteg}[k] + \frac{\texttt{EPPNumFract}[k]}{65536}$$

The denominator taps are formed the same way from [EPPDenInteg] and [EPPDenFract]. These are arrays indexed 1..[EPPFiltLength] (1-indexed); only the first [EPPFiltLength] taps are used. The overall numerator gain [EPPNumFactor] is applied separately at run time and is not folded into these coefficients (this keeps the stored coefficient values small). EPPNumInteg is read/write and stored to flash.

**See also:**

[EPPNumFract](EPPNumFract.md), [EPPNumFactor](EPPNumFactor.md), [EPPDenInteg](EPPDenInteg.md), [EPPFiltLength](EPPFiltLength.md)
