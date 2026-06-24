# AntiCoggValue

*旧版关键字*

**定义：**

`AntiCoggValue` 是一个**只读**值（单一标量，非用户可编辑的数组），报告控制器在当前换相（电气）角下所施加的齿槽补偿电流。在旧版功能中，补偿值遵循电气角的正弦模型：

$$
\text{AntiCoggValue} = \text{AntiCoggAmp}\times\sin\!\left(\theta_{\text{elec}} + \text{AntiCoggPhase}\right)
$$

其中 $\theta_{\text{elec}}$ 为换相角，`AntiCoggPhase` 为以电气度为单位的相位偏移（均以电气角表示；固件以弧度计算正弦值）。当电机为无刷类型且 `AntiCoggOn = 1` 时，该值在每个控制周期加入电流参考值（[CurrRef](../../02-keywords/09-current-and-voltage/02-motor-variables/CurrRef.md)）。用户无法写入该值；它仅用于观测实时补偿项。

该关键字已被移除。现代基于表格的替代方案为 [UPMVelTable](../../02-keywords/09-current-and-voltage/03-current-compensation/UPMVelTable.md)——一个以换相角（度）为索引的数组，在完整的 0-360 周期内每个电气度存储一个用户自定义修正值，由 [UPMVelOn](../upm/UPMVelOn.md) 启用。与旧版单正弦波模型不同，该表格可消除任意按角度周期变化的纹波形状，而不仅限于纯正弦波。

**另请参阅：**

[AntiCoggOn](AntiCoggOn.md)、[AntiCoggAmp](AntiCoggAmp.md)、[AntiCoggPhase](AntiCoggPhase.md)
