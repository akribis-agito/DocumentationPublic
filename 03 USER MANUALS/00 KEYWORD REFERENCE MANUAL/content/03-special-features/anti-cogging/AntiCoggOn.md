# AntiCoggOn

*Legacy keywords*

**Definition:**

`AntiCoggOn` was the switch for the legacy anti-cogging compensation feature (brushless motors only). It accepted three values: `0` (off), `1` (the legacy single-sinusoid model, set by `AntiCoggAmp` and `AntiCoggPhase`), and `2` (an early per-electrical-angle table form). The legacy single-sinusoid model was later removed; the table form is the surviving mechanism.

Through successive firmware renames the same enable carried forward as `AntiDistOn` and then [UPMVelOn](../upm/UPMVelOn.md), and the per-angle table carried forward to [UPMVelTable](../../02-keywords/09-current-and-voltage/03-current-compensation/UPMVelTable.md). The companion keywords `AntiCoggAmp`, `AntiCoggPhase` and `AntiCoggValue` were removed. For cogging cancellation, the direct replacement is `UPMVelOn` together with `UPMVelTable`: enable it with `UPMVelOn` and place one correction value per electrical degree in `UPMVelTable`.

**See also:**

[AntiCoggAmp](AntiCoggAmp.md), [AntiCoggPhase](AntiCoggPhase.md), [AntiCoggValue](AntiCoggValue.md)
