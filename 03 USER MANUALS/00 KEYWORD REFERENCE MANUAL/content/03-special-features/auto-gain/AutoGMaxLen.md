# AutoGMaxLen

**Definition:**

AutoGMaxLen sets the per-region upper limit on the number of motion samples the auto-gain algorithm collects for inertia identification. Samples are sorted into four regions by direction of motion and direction of command; once a region has accumulated AutoGMaxLen samples it stops collecting further samples for that region, while the other regions continue. AutoGMinLen sets the per-region count at which a region is considered to have enough data. Range 20 to 100; default 30. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGMinLen](AutoGMinLen.md), [AutoGAccTh](AutoGAccTh.md), [AutoGOn](AutoGOn.md)
