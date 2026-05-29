# AntiCoggAmp

*Legacy keywords*

**Definition:**

`AntiCoggAmp` set the **peak amplitude** of the legacy sinusoidal anti-cogging term. The legacy feature modelled cogging as a single sinusoid of the commutation (electrical) angle and added it to the current reference each cycle (brushless motors only, when `AntiCoggOn = 1`):

$$
\Delta\text{CurrRef} = \text{AntiCoggAmp}\times\sin\!\left(\theta_{\text{elec}} + \text{AntiCoggPhase}\right)
$$

where $\theta_{\text{elec}}$ is the commutation angle and `AntiCoggPhase` is the phase offset in electrical degrees. The amplitude was in current-reference units (`AntiCoggValue` reported the resulting per-cycle value). This keyword was removed. The modern replacement is the per-angle table [UPMVelTable](../../02-keywords/09-current-and-voltage/03-current-compensation/UPMVelTable.md) (enabled by [UPMVelOn](../upm/UPMVelOn.md)), where the magnitude at each electrical degree is set directly in the table rather than as a single sine amplitude.

**See also:**

[AntiCoggOn](AntiCoggOn.md), [AntiCoggPhase](AntiCoggPhase.md), [AntiCoggValue](AntiCoggValue.md)
