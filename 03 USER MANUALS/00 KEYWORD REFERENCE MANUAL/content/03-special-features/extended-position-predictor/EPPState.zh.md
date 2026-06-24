# EPPState

**定义：**

EPPState 是一个只读状态，报告 EPP（重复控制前馈）当前的运行状态。

| 值 | 含义 |
|-------|---------|
| 0 | 空闲：EPP 未运行。 |
| 1 | 激活，首次运行：新的学习过程正在运行。 |
| 2 | 激活，重复运行：持续学习运行，正在应用并更新存储的修正。 |

在运动开始时，EPPState 通过复制待处理的 [EPPRequest] 值被设置为 1 或 2。当电机关闭时，以及电机开启但不在运动中时，EPPState 被强制回 0（空闲）。EPPState 为只读，不保存至闪存。

**另请参阅：**

[EPPRequest](EPPRequest.md)、[EPPFiltLength](EPPFiltLength.md)、[EPPModelRange](EPPModelRange.md)
