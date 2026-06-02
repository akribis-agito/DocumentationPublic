# AutoGVelTh

**Definition:**

AutoGVelTh sets the velocity threshold in user units per second below which motion data is excluded from the auto-gain identification process. A sample is skipped when the absolute velocity is below AutoGVelTh or the absolute acceleration is below AutoGAccTh, so both thresholds must be met for the sample to be collected. The default is 5000. It is an axis-related parameter expressed in user units, saved to flash, and can be changed at any time.

**See also:**

[AutoGAccTh](AutoGAccTh.md), [AutoGOn](AutoGOn.md), [AutoGMinLen](AutoGMinLen.md)
