# AntiCoggValue

*Legacy keywords*

**Definition:**

`AntiCoggValue` was a **read-only** value (a single scalar, not a user-editable array) that reported the cogging-compensation current the controller was applying at the present commutation (electrical) angle. In the legacy feature the compensation followed a sinusoidal model of the electrical angle:

$$
\text{AntiCoggValue} = \text{AntiCoggAmp}\times\sin\!\left(\theta_{\text{elec}} + \text{AntiCoggPhase}\right)
$$

where $\theta_{\text{elec}}$ is the commutation angle and `AntiCoggPhase` is a phase offset in electrical degrees (both taken as electrical angle; the firmware evaluates the sine in radians). This value was added to the current reference ([CurrRef](../../02-keywords/09-current-and-voltage/02-motor-variables/CurrRef.md)) every control cycle while the motor was a brushless type and `AntiCoggOn = 1`. It could not be written by the user; it only let you observe the live compensation term.

This keyword was removed. The modern, table-based replacement is [UPMVelTable](../../02-keywords/09-current-and-voltage/03-current-compensation/UPMVelTable.md) - an array indexed by the commutation angle in degrees that holds one user-defined correction value per electrical degree over the full 0-360 cycle, enabled by [UPMVelOn](../upm/UPMVelOn.md). Unlike the old single-sinusoid model, the table can cancel an arbitrary angle-periodic ripple shape, not just a pure sine.

**See also:**

[AntiCoggOn](AntiCoggOn.md), [AntiCoggAmp](AntiCoggAmp.md), [AntiCoggPhase](AntiCoggPhase.md)
