# AntiCoggPhase

*Legacy keywords*

**Definition:**

`AntiCoggPhase` set the **phase offset, in whole electrical degrees (0-359)**, added to the commutation angle before the sine was evaluated in the legacy sinusoidal anti-cogging model:

$$
\Delta\text{CurrRef} = \text{AntiCoggAmp}\times\sin\!\left(\theta_{\text{elec}} + \text{AntiCoggPhase}\right)
$$

where $\theta_{\text{elec}}$ is the commutation angle. It aligned the compensating sine with the motor's actual cogging ripple. This keyword was removed. With the modern table-based replacement [UPMVelTable](../../02-keywords/09-current-and-voltage/03-current-compensation/UPMVelTable.md) (enabled by [UPMVelOn](../upm/UPMVelOn.md)) there is no separate phase parameter: the correction at each electrical degree is written directly into the table entry for that angle, so the alignment is implicit in where you place the values.

**See also:**

[AntiCoggOn](AntiCoggOn.md), [AntiCoggAmp](AntiCoggAmp.md), [AntiCoggValue](AntiCoggValue.md)
