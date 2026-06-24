# AntiCoggOn

*旧版关键字*

**定义：**

`AntiCoggOn` 是旧版齿槽补偿功能的开关（仅限无刷电机）。它接受三个值：`0`（关闭）、`1`（旧版单正弦波模型，由 `AntiCoggAmp` 和 `AntiCoggPhase` 设定）和 `2`（早期的按电气角度索引的表格形式）。旧版单正弦波模型后来已被移除；表格形式为延续使用的机制。

经过后续固件版本的重命名，同一使能参数先后更名为 `AntiDistOn`，再到 [UPMVelOn](../upm/UPMVelOn.md)，按角度索引的表格则延续为 [UPMVelTable](../../02-keywords/09-current-and-voltage/03-current-compensation/UPMVelTable.md)。伴随关键字 `AntiCoggAmp`、`AntiCoggPhase` 和 `AntiCoggValue` 均已移除。进行齿槽抵消时，直接替代方案为 `UPMVelOn` 配合 `UPMVelTable`：使用 `UPMVelOn` 启用，并在 `UPMVelTable` 中为每个电气度填入一个修正值。

**另请参阅：**

[AntiCoggAmp](AntiCoggAmp.md)、[AntiCoggPhase](AntiCoggPhase.md)、[AntiCoggValue](AntiCoggValue.md)
