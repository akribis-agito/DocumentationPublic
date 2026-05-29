# SpringTable

**Definition:**

SpringTable is a reserved, not-yet-implemented array keyword (size 41, with usable indices 1 through 40). It currently has no effect on spring compensation. The active compensation is the linear model defined by [SpringPLow](SpringPLow.md), [SpringPHigh](SpringPHigh.md), [SpringPosFFW](SpringPosFFW.md), and [SpringCurrFFW](SpringCurrFFW.md). When implemented, its entries would hold per-segment current corrections, 1-indexed. It is an axis-related array parameter saved to flash and can be changed at any time.

**See also:**

[SpringOn](SpringOn.md), [SpringTableGp](SpringTableGp.md), [SpringPLow](SpringPLow.md), [SpringPHigh](SpringPHigh.md)
