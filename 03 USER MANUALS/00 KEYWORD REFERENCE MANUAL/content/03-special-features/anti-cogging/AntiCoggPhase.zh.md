# AntiCoggPhase

*旧版关键字*

**定义：**

`AntiCoggPhase` 在旧版正弦齿槽补偿模型中，设置在求正弦值之前叠加到换相角上的**相位偏移，以整数电气度（0-359）为单位**：

$$
\Delta\text{CurrRef} = \text{AntiCoggAmp}\times\sin\!\left(\theta_{\text{elec}} + \text{AntiCoggPhase}\right)
$$

其中 $\theta_{\text{elec}}$ 为换相角。该参数用于将补偿正弦波与电机实际齿槽效应纹波对齐。该关键字已被移除。使用现代基于表格的替代方案 [UPMVelTable](../../02-keywords/09-current-and-voltage/03-current-compensation/UPMVelTable.md)（由 [UPMVelOn](../upm/UPMVelOn.md) 启用）时，不再需要单独的相位参数：每个电气度的修正值直接写入该角度对应的表格项，因此对齐关系隐含于所填入值的位置中。

**另请参阅：**

[AntiCoggOn](AntiCoggOn.md)、[AntiCoggAmp](AntiCoggAmp.md)、[AntiCoggValue](AntiCoggValue.md)
