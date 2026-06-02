# AutoGJratUs

**Definition:**

AutoGJratUs sets the user-supplied load-to-motor inertia ratio, expressed as a percentage, that the automatic gain tuning algorithm uses in place of its own estimate. In the auto-gain modes that take the user ratio, the gains are computed from a total inertia of motor inertia × (1 + AutoGJratUs / 100), and the user ratio is also reported as the final ratio. The user ratio is only applied when it falls within the AutoGMinRat to AutoGMaxRat window; otherwise the parameters are not updated for that cycle. The valid range is -50 to 20000, with a default of 140. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGJm](AutoGJm.md), [AutoGBW](AutoGBW.md), [AutoGOn](AutoGOn.md)
