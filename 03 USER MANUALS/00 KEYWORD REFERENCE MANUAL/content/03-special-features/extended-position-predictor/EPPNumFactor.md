# EPPNumFactor

**Definition:**

EPPNumFactor is the overall numerator gain of the Extended Position Predictor. It is not folded into the stored numerator coefficients ([EPPNumInteg]/[EPPNumFract], which are kept small for accuracy); instead it multiplies the lead/lag filter output at run time, scaling the predictive correction added to [CurrRef]. EPPNumFactor is a single read/write value (not an array) and is stored to flash. Its default is 0, so EPP applies no learned correction until EPPNumFactor is set to a nonzero value.

**See also:**

[EPPNumFract](EPPNumFract.md), [EPPNumInteg](EPPNumInteg.md), [EPPDenFract](EPPDenFract.md)
