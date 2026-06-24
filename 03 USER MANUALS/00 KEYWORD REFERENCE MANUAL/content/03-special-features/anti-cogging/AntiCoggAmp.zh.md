# AntiCoggAmp

*旧版关键字*

**定义：**

`AntiCoggAmp` 设置旧版正弦齿槽补偿项的**峰值幅值**。该旧版功能将齿槽效应建模为换相（电气）角的单一正弦波，并在每个控制周期将其叠加到电流参考值（仅限无刷电机，且 `AntiCoggOn = 1` 时）：

$$
\Delta\text{CurrRef} = \text{AntiCoggAmp}\times\sin\!\left(\theta_{\text{elec}} + \text{AntiCoggPhase}\right)
$$

其中 $\theta_{\text{elec}}$ 为换相角，`AntiCoggPhase` 为以电气度为单位的相位偏移。幅值以电流参考值单位表示（`AntiCoggValue` 报告每个周期对应的实时值）。该关键字已被移除。现代替代方案为按角度索引的表格 [UPMVelTable](../../02-keywords/09-current-and-voltage/03-current-compensation/UPMVelTable.md)（由 [UPMVelOn](../upm/UPMVelOn.md) 启用），表中每个电气度的幅值直接写入，而非以单一正弦幅值表示。

**另请参阅：**

[AntiCoggOn](AntiCoggOn.md)、[AntiCoggPhase](AntiCoggPhase.md)、[AntiCoggValue](AntiCoggValue.md)
