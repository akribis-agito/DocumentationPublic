# AutoGQualTh

**Definition:**

AutoGQualTh sets the maximum allowed value of the identification quality metric (an estimation-error figure expressed as a percentage, where lower is better). A calculation's result is accepted and folded into the estimate only when its quality metric is at or below this threshold and the estimated inertia ratio also falls within the AutoGMinRat to AutoGMaxRat range; results whose quality metric exceeds the threshold are discarded. The range is 1 to 1000, default 100. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGNumSet](AutoGNumSet.md), [AutoGMinRat](AutoGMinRat.md), [AutoGMaxRat](AutoGMaxRat.md)
